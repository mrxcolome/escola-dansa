# -*- coding: utf-8 -*-
"""
Comprova que tots els enllaços interns de la web porten a una pàgina o fitxer que existeix.
Executa:  python comprova_enllacos.py   (després de regenerar)
Surt amb error (codi 1) si en troba cap de trencat: el desplegament s'atura i no es publica.
Les seccions internes (seo, dossier, memoria, google, backstage) no es revisen.
"""
import glob
import os
import re
import sys

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INTERNES = ("seo/", "dossier/", "memoria/", "google/", "backstage/", "generador/")


def existeix(href):
    cami = href.split("#")[0].split("?")[0].lstrip("/")
    if cami == "":
        return True
    ple = os.path.join(ARREL, cami)
    if "." in os.path.basename(cami):
        return os.path.isfile(ple)
    return os.path.isfile(os.path.join(ple, "index.html"))


def main():
    os.chdir(ARREL)
    pagines = [f for f in glob.glob("**/*.html", recursive=True) if not f.startswith(INTERNES)]
    trencats = {}
    for f in pagines:
        html = open(f, encoding="utf-8").read()
        for href in set(re.findall(r'(?:href|src)="(/[^"]*)"', html)):
            if not existeix(href):
                trencats.setdefault(href.split("#")[0], []).append(f)
    if trencats:
        print(f"ENLLAÇOS TRENCATS: {len(trencats)}")
        for href, fitxers in sorted(trencats.items()):
            print(f"  {href}  ← {', '.join(sorted(fitxers)[:3])}{' …' if len(fitxers) > 3 else ''}")
        sys.exit(1)
    print(f"enllaços interns: tots correctes ({len(pagines)} pàgines revisades)")


if __name__ == "__main__":
    main()
