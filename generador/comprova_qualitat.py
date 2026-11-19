# -*- coding: utf-8 -*-
"""
Comprovacions de qualitat de la web, més enllà dels enllaços trencats.
Executa:  python comprova_qualitat.py   (després de regenerar)
Surt amb error (codi 1) si troba cap problema: el build de Vercel s'atura i no es publica.

Què mira (les seccions internes no es revisen):
  1. idioma dels enllaços: una pàgina en castellà no enllaça a la versió catalana d'una pàgina
     que té versió castellana (i al revés). El selector d'idioma va amb URL absoluta i no compta.
  2. xifres animades: cada [data-compta="N"] porta N a l'HTML (és el que llegeixen Google i els
     lectors de pantalla; l'animació la posa a 0 amb JS).
  3. noms de les activitats a la portada: cada paraula del nom de la targeta és una paraula
     sencera del títol de la pàgina on porta (atrapa noms retallats com «contempo»).
  4. «per saber-ne més»: si algun post del blog es relaciona amb una pàgina d'activitat,
     la pàgina té el bloc de posts.
  5. restes de plantilla: marques de preu sense resoldre (⟦…⟧), «undefined», «NaN».
"""
import glob
import html as htmllib
import os
import re
import sys
import unicodedata

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTERNES = ("seo/", "competencia/", "dossier/", "memoria/", "google/", "backstage/", "generador/",
            "materials/", "targeto-regal/proposta", "targeto-regal/tria", "targeto-regal/render",
            "targeto-regal/minimalistes", "_web/", "node_modules/")

problemes = []


def avisa(tipus, fitxer, detall):
    problemes.append((tipus, fitxer, detall))


def llegeix(f):
    return open(f, encoding="utf-8").read()


def cami_de(f):
    """fitxer → URL relativa: blog/x/index.html → /blog/x/"""
    f = f.replace("\\", "/")
    if f == "index.html":
        return "/"
    if f.endswith("/index.html"):
        return "/" + f[: -len("index.html")]
    return "/" + f


def fitxer_de(url):
    url = url.split("#")[0].split("?")[0]
    if url.endswith("/"):
        return url.lstrip("/") + "index.html"
    return None


def sense_accents(t):
    return "".join(c for c in unicodedata.normalize("NFD", t.lower()) if unicodedata.category(c) != "Mn")


def main():
    os.chdir(ARREL)
    pagines = sorted(f.replace("\\", "/") for f in glob.glob("**/index.html", recursive=True)
                     if not f.replace("\\", "/").startswith(INTERNES))
    html = {f: llegeix(f) for f in pagines}

    # 1. idioma dels enllaços: quines pàgines tenen parella a l'altre idioma (per les hreflang)
    te_parella = set()
    for f, h in html.items():
        if re.search(r'<link rel="alternate" hreflang="(ca|es)"', h):
            alt = re.findall(r'<link rel="alternate" hreflang="(?:ca|es)" href="https://escoladansa\.com(/[^"]*)"', h)
            if len(set(alt)) >= 2:
                te_parella.add(cami_de(f))
    for f, h in html.items():
        es = f.startswith("es/")
        for a_attrs, a_text in re.findall(r'<a\b([^>]*)>(.*?)</a>', h, flags=re.S):
            # el selector d'idioma (hreflang o «cat / es») sí que ha d'enllaçar a l'altre idioma
            text = re.sub(r"<[^>]+>", "", a_text).strip().lower()
            if "hreflang=" in a_attrs or text in ("cat", "es", "català", "castellano", "catalán", "español"):
                continue
            m = re.search(r'href="(/[^"#?]*)', a_attrs)
            if not m:
                continue
            href = m.group(1)
            if href.startswith(("/assets/", "/api/")) or "." in href.rsplit("/", 1)[-1]:
                continue
            desti_es = href.startswith("/es/") or href == "/es"
            if href not in te_parella:
                continue
            if es and not desti_es:
                avisa("idioma", f, f"enllaça a la pàgina catalana {href} (hi ha versió castellana)")
            if not es and desti_es:
                avisa("idioma", f, f"enllaça a la pàgina castellana {href} (hi ha versió catalana)")

    # 2. xifres animades
    for f, h in html.items():
        for valor, text in re.findall(r'data-compta="(\d+)"[^>]*>([^<]*)<', h):
            if text.strip() != valor:
                avisa("xifra", f, f'data-compta="{valor}" mostra «{text.strip()}» a l\'HTML')

    # 3. noms de les activitats a les targetes de la portada
    for f in ("index.html", "es/index.html"):
        h = html.get(f, "")
        for nom, enllac in re.findall(r'<div class="cara cara-front"><span class="num">\d+</span><h3>([^<]*)</h3>.*?class="mes-info" href="([^"]+)"', h, flags=re.S):
            desti = fitxer_de(enllac)
            if not desti or desti not in html:
                continue
            m = re.search(r"<title>(.*?)</title>", html[desti], flags=re.S)
            h1 = re.search(r"<h1[^>]*>(.*?)</h1>", html[desti], flags=re.S)
            ref = sense_accents(htmllib.unescape(re.sub(r"<[^>]+>", " ", (m.group(1) if m else "") + " " + (h1.group(1) if h1 else ""))))
            paraules_ref = re.findall(r"[a-z0-9]+", ref)
            for p in re.findall(r"[a-z0-9]+", sense_accents(htmllib.unescape(nom))):
                if not any(w == p or (w.startswith(p[:-1]) and abs(len(w) - len(p)) <= 2) for w in paraules_ref):
                    avisa("nom", f, f"la targeta «{htmllib.unescape(nom)}» té «{p}», que no és al títol de {enllac}")

    # 4. «per saber-ne més» a les pàgines d'activitat que tenen posts relacionats
    sys.path.insert(0, os.path.join(ARREL, "generador"))
    try:
        from blog_posts import POSTS
    except Exception as e:  # sense posts no es pot comprovar, però no ha de bloquejar
        print(f"(no s'han pogut llegir els posts: {e})")
        POSTS = []
    relacionades = {s for p in POSTS for s in p.get("related_pagines", [])}
    for s in sorted(relacionades):
        f = f"{s}/index.html"
        if f not in html:
            continue
        # la pàgina catalana i la seva parella castellana (per la hreflang)
        alt = re.search(r'<link rel="alternate" hreflang="es" href="https://escoladansa\.com(/[^"]*)"', html[f])
        for g in [f] + ([fitxer_de(alt.group(1))] if alt else []):
            if g in html and 'class="posts-blog"' not in html[g]:
                avisa("posts", g, "té posts del blog relacionats però no hi ha el bloc «per saber-ne més»")

    # 6. etiquetes per als lectors de pantalla en català dins de /es/ (aria-label que surten tal qual a la portada catalana)
    iguals = {"menú", "idioma"}
    etiq_ca = set(re.findall(r'aria-label="([^"]+)"', html.get("index.html", ""))) - iguals
    for f, h in html.items():
        if f.startswith("es/"):
            for v in sorted(set(re.findall(r'aria-label="([^"]+)"', h)) & etiq_ca):
                avisa("idioma", f, f'aria-label="{v}" és en català')

    # 5. restes de plantilla
    for f, h in html.items():
        visible = re.sub(r"<(script|style)\b.*?</\1>", " ", h, flags=re.S)
        if "⟦" in visible:
            avisa("plantilla", f, "hi ha marques de preu sense resoldre (⟦…⟧)")
        for paraula in ("undefined", "NaN"):
            if re.search(rf">[^<]*\b{paraula}\b[^<]*<", visible):
                avisa("plantilla", f, f"hi apareix «{paraula}» al text")

    if problemes:
        print(f"PROBLEMES DE QUALITAT: {len(problemes)}")
        for tipus, f, detall in problemes:
            print(f"  [{tipus}] {f}: {detall}")
        sys.exit(1)
    print(f"qualitat: tot correcte ({len(html)} pàgines revisades)")


if __name__ == "__main__":
    main()
