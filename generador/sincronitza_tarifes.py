# -*- coding: utf-8 -*-
"""
Porta les tarifes del Backstage a la web. El Backstage (backstage.escoladansa.com,
/tarifes/edita) n'és l'única font: aquí només es llegeix /tarifes-publica i es desa
a tarifes.json, que és d'on tarifes.py treu /preus i els preus de tots els textos.

  python3 sincronitza_tarifes.py     # escriu tarifes.json si ha canviat i diu què

Surt amb codi 0 sempre; imprimeix «CANVIS» si n'hi ha (el workflow «graella i
tarifes del backstage» ho fa servir per decidir si regenera i publica). Si el
Backstage no respon o torna alguna tarifa buida, no toca res.
"""
import json
import os
import sys
import urllib.request

URL = "https://backstage.escoladansa.com/tarifes-publica"
CAMI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tarifes.json")
TAULES = ["45", "60", "mes60"]
SOLTS = ["matriculaRenovacio", "matriculaNova", "ballsSalo"]


def llegeix_backstage():
    req = urllib.request.Request(URL, headers={"User-Agent": "escoladansa-web/tarifes"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def valid(n):
    # cap quota ni matrícula de l'escola passa de 1.000 €: una xifra així és un error de picar (p. ex. «5600»)
    return isinstance(n, (int, float)) and not isinstance(n, bool) and 0 < n < 1000


def main():
    try:
        d = llegeix_backstage()
    except Exception as e:
        print(f"el Backstage no respon ({e}): no es toquen les tarifes")
        return
    try:
        nova = {"taules": {t: {"mensual": d["taules"][t]["mensual"], "trimestral": d["taules"][t]["trimestral"]}
                           for t in TAULES}}
        for c in SOLTS:
            nova[c] = d[c]
    except (KeyError, TypeError) as e:
        print(f"resposta del Backstage incompleta ({e}): no es toquen les tarifes")
        return
    tots = [v for t in TAULES for f in ("mensual", "trimestral") for v in nova["taules"][t][f]] + [nova[c] for c in SOLTS]
    if len(tots) != 3 * 8 + 3 or not all(valid(v) for v in tots):
        print("alguna tarifa del Backstage és buida o estranya: no es toquen les tarifes")
        return
    # 56.0 → 56 perquè el json quedi igual que el de sempre
    neteja = lambda v: int(v) if float(v).is_integer() else v
    nova = json.loads(json.dumps(nova), parse_float=lambda s: neteja(float(s)))

    with open(CAMI, encoding="utf-8") as f:
        vella = json.load(f)
    if nova == vella:
        print("tarifes iguals que les del Backstage")
        return

    for t in TAULES:
        for f in ("mensual", "trimestral"):
            a, b = vella["taules"][t][f], nova["taules"][t][f]
            if a != b:
                print(f"  {t} {f}: {a} → {b}")
    for c in SOLTS:
        if vella.get(c) != nova[c]:
            print(f"  {c}: {vella.get(c)} → {nova[c]}")
    with open(CAMI, "w", encoding="utf-8", newline="\n") as f:
        json.dump(nova, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("CANVIS: tarifes.json actualitzat")


if __name__ == "__main__":
    sys.exit(main())
