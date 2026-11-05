# -*- coding: utf-8 -*-
"""
Porta la graella del Backstage a la web. El Backstage (backstage.escoladansa.com)
n'és l'única font: aquí només es llegeix /graella-publica i es desa a graella.json,
que és d'on genera_pagines.py treu /horaris/ i els horaris de cada activitat.

  python3 sincronitza_graella.py     # escriu graella.json si ha canviat i diu què

Surt amb codi 0 sempre; imprimeix «CANVIS» si n'hi ha (el workflow «graella» ho fa
servir per decidir si regenera i publica). Si el Backstage no respon o torna una
graella buida, no toca res.
"""
import json
import os
import sys
import urllib.request

URL = "https://backstage.escoladansa.com/graella-publica"
CAMI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "graella.json")
DIES = ["dilluns", "dimarts", "dimecres", "dijous", "divendres", "dissabte"]


def llegeix_backstage():
    req = urllib.request.Request(URL, headers={"User-Agent": "escoladansa-web/graella"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())["classes"]


def main():
    try:
        classes = llegeix_backstage()
    except Exception as e:
        print(f"el Backstage no respon ({e}): no es toca la graella")
        return
    if len(classes) < 10:
        print(f"el Backstage torna només {len(classes)} classes: sembla un error, no es toca la graella")
        return
    nova = {}
    for c in classes:  # ja venen ordenades per dia, hora i sala
        nova.setdefault(c["dia"], []).append([c["hora"], c["activitat"], c["grup"], c["sala"]])
    nova = {d: nova[d] for d in DIES if d in nova}

    with open(CAMI, encoding="utf-8") as f:
        vella = json.load(f)
    if nova == vella:
        print(f"graella igual que la del Backstage ({len(classes)} classes)")
        return

    claus = lambda g: {f"{d} {' · '.join(x for x in f if x)}" for d, fs in g.items() for f in fs}
    for x in sorted(claus(vella) - claus(nova)):
        print(f"  − {x}")
    for x in sorted(claus(nova) - claus(vella)):
        print(f"  + {x}")
    with open(CAMI, "w", encoding="utf-8", newline="\n") as f:
        json.dump(nova, f, ensure_ascii=False, indent=1)
    print(f"CANVIS: graella.json actualitzada ({len(classes)} classes)")


if __name__ == "__main__":
    sys.exit(main())
