# -*- coding: utf-8 -*-
"""
Connexió amb la fitxa de Google (API de Perfil d'Empresa). Python 3 sense dependències.
L'executa el workflow .github/workflows/gbp.yml amb tres secrets del repo:
  GBP_CLIENT_ID, GBP_CLIENT_SECRET, GBP_REFRESH_TOKEN (client OAuth del projecte escoladansa-gbp).

  python3 gbp.py prova       # mostra el compte, la fitxa i les ressenyes (no canvia res)
  python3 gbp.py ressenyes   # actualitza la nota i el nombre d'opinions de la portada (CA i ES)
  python3 gbp.py publica     # publica a la fitxa els posts del blog que encara no hi són

Els posts ja publicats a la fitxa es guarden a gbp_publicats.json (el workflow el desa al repo).
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import date

AQUI = os.path.dirname(os.path.abspath(__file__))
ARREL = os.path.dirname(AQUI)
DOMINI = "https://escoladansa.com"
NOM_FITXA = "cristina colom"  # per trobar la fitxa si el compte en té més d'una
PUBLICATS = os.path.join(AQUI, "gbp_publicats.json")
HOME_CA = os.path.join(ARREL, "index.html")
HOME_ES_GEN = os.path.join(AQUI, "genera_home_es.py")

RE_CA = re.compile(r"<strong>\d,\d</strong> a Google · \d+ opinions")
RE_ES = re.compile(r"<strong>\d,\d</strong> en Google · \d+ opiniones")


def crida(url, dades=None, token=None, formulari=False):
    capcaleres = {}
    if token:
        capcaleres["Authorization"] = f"Bearer {token}"
    cos = None
    if dades is not None:
        if formulari:
            cos = urllib.parse.urlencode(dades).encode()
        else:
            cos = json.dumps(dades).encode()
            capcaleres["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=cos, headers=capcaleres)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        sys.exit(f"ERROR {e.code} a {url.split('?')[0]}\n{e.read().decode(errors='replace')}")


def token_acces():
    falten = [k for k in ("GBP_CLIENT_ID", "GBP_CLIENT_SECRET", "GBP_REFRESH_TOKEN") if not os.environ.get(k)]
    if falten:
        sys.exit(f"falten els secrets: {', '.join(falten)}")
    r = crida("https://oauth2.googleapis.com/token", {
        "client_id": os.environ["GBP_CLIENT_ID"],
        "client_secret": os.environ["GBP_CLIENT_SECRET"],
        "refresh_token": os.environ["GBP_REFRESH_TOKEN"],
        "grant_type": "refresh_token",
    }, formulari=True)
    return r["access_token"]


def troba_fitxa(token):
    """Retorna (accounts/X, locations/Y, títol) de la fitxa de l'escola."""
    comptes = crida("https://mybusinessaccountmanagement.googleapis.com/v1/accounts", token=token).get("accounts", [])
    trobades = []
    for c in comptes:
        url = (f"https://mybusinessbusinessinformation.googleapis.com/v1/{c['name']}/locations"
               "?readMask=name,title&pageSize=100")
        for loc in crida(url, token=token).get("locations", []):
            trobades.append((c["name"], loc["name"], loc.get("title", "")))
    if not trobades:
        sys.exit(f"cap fitxa trobada ({len(comptes)} comptes)")
    for t in trobades:
        if NOM_FITXA in t[2].lower():
            return t
    return trobades[0]


def ressenyes(token, compte, fitxa):
    r = crida(f"https://mybusiness.googleapis.com/v4/{compte}/{fitxa}/reviews?pageSize=1", token=token)
    return r.get("averageRating"), r.get("totalReviewCount")


def ordre_prova():
    token = token_acces()
    compte, fitxa, titol = troba_fitxa(token)
    nota, total = ressenyes(token, compte, fitxa)
    print(f"compte: {compte}\nfitxa: {fitxa} ({titol})\nressenyes: {nota} de mitjana, {total} en total")


def ordre_ressenyes():
    token = token_acces()
    compte, fitxa, _ = troba_fitxa(token)
    nota, total = ressenyes(token, compte, fitxa)
    if not nota or not total:
        sys.exit(f"resposta sense ressenyes ({nota}, {total}): no es toca res")
    n = f"{nota:.1f}".replace(".", ",")
    nou_ca = f"<strong>{n}</strong> a Google · {total} opinions"
    nou_es = f"<strong>{n}</strong> en Google · {total} opiniones"
    canvis = 0
    for cami, patro, nou in ((HOME_CA, RE_CA, nou_ca), (HOME_ES_GEN, RE_CA, nou_ca), (HOME_ES_GEN, RE_ES, nou_es)):
        text = open(cami, encoding="utf-8").read()
        if not patro.search(text):
            sys.exit(f"no trobo el bloc d'opinions a {os.path.basename(cami)}")
        nou_text = patro.sub(nou, text)
        if nou_text != text:
            open(cami, "w", encoding="utf-8", newline="\n").write(nou_text)
            canvis += 1
    print(f"ressenyes: {n} · {total}" + (" (actualitzat)" if canvis else " (sense canvis)"))


def ordre_publica():
    sys.path.insert(0, AQUI)
    from blog_posts import POSTS
    publicats = json.load(open(PUBLICATS, encoding="utf-8"))
    avui = date.today().isoformat()
    nous = [p for p in POSTS if p["slug"] not in publicats and p["data"] <= avui]
    if not nous:
        print("cap post nou per publicar a la fitxa")
        return
    token = token_acces()
    compte, fitxa, _ = troba_fitxa(token)
    for p in nous:
        url = f"{DOMINI}/blog/{p['slug']}/"
        cos = {
            "languageCode": "ca",
            "topicType": "STANDARD",
            "summary": f"{p['excerpt']}\n\nT'ho expliquem al blog de l'escola.",
            "callToAction": {"actionType": "LEARN_MORE", "url": url},
            "media": [{"mediaFormat": "PHOTO", "sourceUrl": f"{DOMINI}/assets/{p['img']}"}],
        }
        r = crida(f"https://mybusiness.googleapis.com/v4/{compte}/{fitxa}/localPosts", cos, token=token)
        print(f"publicat a la fitxa: {p['slug']} ({r.get('state', '?')})")
        publicats.append(p["slug"])
        json.dump(publicats, open(PUBLICATS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    ordres = {"prova": ordre_prova, "ressenyes": ordre_ressenyes, "publica": ordre_publica}
    if len(sys.argv) != 2 or sys.argv[1] not in ordres:
        sys.exit(f"ús: python3 gbp.py {'|'.join(ordres)}")
    ordres[sys.argv[1]]()
