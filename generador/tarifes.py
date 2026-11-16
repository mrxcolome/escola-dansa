# -*- coding: utf-8 -*-
"""
Tarifes del curs per als generadors. La font és el Backstage (/tarifes/edita):
sincronitza_tarifes.py les desa a tarifes.json i aquí se'n fan les taules de /preus
i es resolen les marques de preu dels textos.

Marques (en qualsevol text dels generadors: pàgines, FAQ, posts, markdown):
  ⟦m45.1⟧      quota mensual, classes de 45 min, 1 activitat         → 56
  ⟦t60.2⟧      quota trimestral, classes d'1 hora, 2 activitats       → 212
  ⟦mmes60.4⟧   mensual, classes de més d'1 hora, 4 activitats         → 104
  ⟦dm45.1-2⟧   diferència mensual entre 1 i 2 activitats (45 min)     → 12
  ⟦renovacio⟧  matrícula alumnes antics · ⟦nova⟧ nous alumnes · ⟦salo⟧ balls de saló
La home CA (index.html) és feta a mà: les seves frases amb preus les reescriu
actualitza_home() amb els patrons de FRASES_HOME.
"""
import io
import json
import os
import re

CAMI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tarifes.json")
with io.open(CAMI, encoding="utf-8") as _f:
    T = json.load(_f)

TAULES = ["45", "60", "mes60"]


def fmt(n):
    """56 → «56», 56.5 → «56,50» (format català)."""
    if n is None:
        return "—"
    if float(n).is_integer():
        return str(int(n))
    return f"{n:.2f}".replace(".", ",")


def valor(clau):
    if clau in ("renovacio", "nova", "salo"):
        return {"renovacio": T["matriculaRenovacio"], "nova": T["matriculaNova"], "salo": T["ballsSalo"]}[clau]
    m = re.fullmatch(r"(dm|m|t)(45|60|mes60)\.(\d)(?:-(\d))?", clau)
    if not m:
        raise ValueError(f"marca de preu desconeguda: ⟦{clau}⟧")
    tipus, taula, a, b = m.group(1), m.group(2), int(m.group(3)), m.group(4)
    if tipus == "dm":
        fila = T["taules"][taula]["mensual"]
        return fila[int(b) - 1] - fila[a - 1]
    return T["taules"][taula]["mensual" if tipus == "m" else "trimestral"][a - 1]


MARCA = re.compile(r"⟦([^⟧]+)⟧")


def preus(text):
    """Resol totes les marques ⟦…⟧ d'un text."""
    return MARCA.sub(lambda m: fmt(valor(m.group(1))), text)


# files de /preus: (concepte, 1 dia, 2, 3, 4)
ETIQUETES = {"45": "classes de 45 min", "60": "classes d'1 hora", "mes60": "classes de més d'1 hora"}
TARIFA_MENSUAL = [(ETIQUETES[t],) + tuple(f"{fmt(v)} €" for v in T["taules"][t]["mensual"]) for t in TAULES]
TARIFA_TRIMESTRAL = [(ETIQUETES[t],) + tuple(f"{fmt(v)} €" for v in T["taules"][t]["trimestral"]) for t in TAULES]
TARIFA_ALTRES = [
    ("matrícula alumnes antics", f"{fmt(T['matriculaRenovacio'])} €"),
    ("matrícula nous alumnes", f"{fmt(T['matriculaNova'])} €"),
    ("balls de saló (10 sessions)", f"{fmt(T['ballsSalo'])} €/persona"),
]

# frases amb preus de la home CA (index.html, feta a mà): (patró, text amb marques)
_N = r"\d+(?:,\d+)?"
FRASES_HOME = [
    (rf'"priceRange": "{_N} € – {_N} € al mes"', '"priceRange": "⟦m45.1⟧ € – ⟦mmes60.4⟧ € al mes"'),
    (rf"les quotes mensuals van dels {_N} € \(1 dia per setmana de classes de 45 min\) als {_N} € \(4 dies de classes de més d'1 hora\)",
     "les quotes mensuals van dels ⟦m45.1⟧ € (1 dia per setmana de classes de 45 min) als ⟦mmes60.4⟧ € (4 dies de classes de més d'1 hora)"),
    (rf"quotes mensuals des de {_N} €\. paga per mes", "quotes mensuals des de ⟦m45.1⟧ €. paga per mes"),
]


def actualitza_home(cami):
    """Posa els preus vigents a les frases de FRASES_HOME d'index.html. Torna True si ha canviat."""
    with io.open(cami, encoding="utf-8") as f:
        h = f.read()
    nou = h
    for patro, plantilla in FRASES_HOME:
        nou, n = re.subn(patro, lambda _m, p=plantilla: preus(p), nou)
        if n == 0:
            print(f"AVÍS tarifes: a index.html no es troba la frase «{plantilla[:60]}…»")
    if nou != h:
        with io.open(cami, "w", encoding="utf-8", newline="\n") as f:
            f.write(nou)
        return True
    return False
