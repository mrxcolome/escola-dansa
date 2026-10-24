# -*- coding: utf-8 -*-
"""
Connexió amb la fitxa de Google (API de Perfil d'Empresa). Python 3 sense dependències.
L'executa el workflow .github/workflows/gbp.yml amb tres secrets del repo:
  GBP_CLIENT_ID, GBP_CLIENT_SECRET, GBP_REFRESH_TOKEN (client OAuth del projecte escoladansa-gbp).

  python3 gbp.py prova       # mostra el compte, la fitxa i les ressenyes (no canvia res)
  python3 gbp.py ressenyes   # actualitza la nota i el nombre d'opinions de la portada (CA i ES)
  python3 gbp.py publica     # publica a la fitxa els posts del blog que encara no hi són
  python3 gbp.py llista      # mostra les 10 ressenyes més recents i si tenen resposta (no canvia res)
  python3 gbp.py edita       # aplica a la fitxa els canvis de gbp_canvis.json (camps de l'API: websiteUri, profile…) i el buida
  python3 gbp.py fitxa       # mostra les dades de la fitxa: categories, web, horari, descripció (no canvia res)
  python3 gbp.py respon      # contesta les ressenyes de gbp_respostes.json que encara no tenen resposta
  python3 gbp.py fotos       # puja a la fitxa les fotos de gbp_fotos.json que encara no hi són i llista les que hi ha

Els posts ja publicats a la fitxa es guarden a gbp_publicats.json (el workflow el desa al repo).
"""
import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from zoneinfo import ZoneInfo

AQUI = os.path.dirname(os.path.abspath(__file__))
ARREL = os.path.dirname(AQUI)
DOMINI = "https://escoladansa.com"
NOM_FITXA = "cristina colom"  # per trobar la fitxa si el compte en té més d'una
PUBLICATS = os.path.join(AQUI, "gbp_publicats.json")
RESPOSTES = os.path.join(AQUI, "gbp_respostes.json")
FOTOS = os.path.join(AQUI, "gbp_fotos.json")  # [{"fitxer": "assets/fitxa/x.jpg", "categoria": "INTERIOR"}, …]
CANVIS = os.path.join(AQUI, "gbp_canvis.json")  # camps de la fitxa per canviar amb `edita`  # {"nom de qui l'ha escrit": "resposta"}
HOME_CA = os.path.join(ARREL, "index.html")
HOME_ES_GEN = os.path.join(AQUI, "genera_home_es.py")

RE_CA = re.compile(r"<strong>\d,\d</strong> a Google · \d+ opinions")
RE_ES = re.compile(r"<strong>\d,\d</strong> en Google · \d+ opiniones")


def crida(url, dades=None, token=None, formulari=False, metode=None):
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
    req = urllib.request.Request(url, data=cos, headers=capcaleres, method=metode)
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


def ordre_fitxa():
    token = token_acces()
    _, fitxa, _ = troba_fitxa(token)
    camps = "title,categories,websiteUri,regularHours,profile,storefrontAddress,phoneNumbers,metadata,openInfo,latlng"
    r = crida(f"https://mybusinessbusinessinformation.googleapis.com/v1/{fitxa}?readMask={camps}", token=token)
    cat = r.pop("categories", {})
    pc = cat.get("primaryCategory", {})
    print("categoria principal:", pc.get("displayName"), pc.get("name"))
    print("categories addicionals:", [(c.get("displayName"), c.get("name")) for c in cat.get("additionalCategories", [])])
    # categories de Google que tenen a veure amb la dansa, en castellà (com les veu qui cerca)
    llista = crida("https://mybusinessbusinessinformation.googleapis.com/v1/categories?regionCode=ES&languageCode=es"
                   "&view=BASIC&pageSize=100&filter=displayName%3Dbaile", token=token).get("categories", [])
    llista += crida("https://mybusinessbusinessinformation.googleapis.com/v1/categories?regionCode=ES&languageCode=es"
                    "&view=BASIC&pageSize=100&filter=displayName%3Ddanza", token=token).get("categories", [])
    print("categories ES amb «baile»/«danza»:", [(c.get("displayName"), c.get("name")) for c in llista])
    r.pop("regularHours", None)
    print(json.dumps(r, ensure_ascii=False, indent=1))
    if r.get("metadata", {}).get("hasGoogleUpdated"):
        # Google ha canviat dades de la fitxa pel seu compte: quins camps i amb quins valors
        g = crida(f"https://mybusinessbusinessinformation.googleapis.com/v1/{fitxa}:getGoogleUpdated?readMask={camps}",
                  token=token)
        print("canvis de Google pendents de revisar (camps):", g.get("diffMask"), "| pendents:", g.get("pendingMask"))
        loc = g.get("location", {})
        for camp in (g.get("diffMask") or "").split(","):
            camp = camp.strip().split(".")[0]
            if camp:
                print(f"  {camp} segons Google:", json.dumps(loc.get(camp), ensure_ascii=False)[:600])


def ordre_edita():
    canvis = json.load(open(CANVIS, encoding="utf-8"))
    if not canvis:
        print("cap canvi pendent")
        return
    token = token_acces()
    _, fitxa, _ = troba_fitxa(token)
    mascara = ",".join("profile.description" if k == "profile" else k for k in canvis)
    r = crida(f"https://mybusinessbusinessinformation.googleapis.com/v1/{fitxa}?updateMask={mascara}", canvis,
              token=token, metode="PATCH")
    print("fitxa actualitzada:", mascara)
    print(json.dumps({k: r.get(k) for k in canvis}, ensure_ascii=False, indent=1))
    json.dump({}, open(CANVIS, "w", encoding="utf-8"))


def ordre_llista():
    token = token_acces()
    compte, fitxa, _ = troba_fitxa(token)
    r = crida(f"https://mybusiness.googleapis.com/v4/{compte}/{fitxa}/reviews?pageSize=10&orderBy=updateTime%20desc",
              token=token)
    estrelles = {"ONE": 1, "TWO": 2, "THREE": 3, "FOUR": 4, "FIVE": 5}
    for rv in r.get("reviews", []):
        print(f"--- {rv.get('createTime', '')[:10]} · {rv.get('reviewer', {}).get('displayName', '?')} · "
              f"{estrelles.get(rv.get('starRating'), '?')}★ · {'respost' if rv.get('reviewReply') else 'SENSE RESPOSTA'}")
        print(rv.get("comment", "(sense text)"))
        if rv.get("reviewReply"):
            print(f"  resposta: {rv['reviewReply'].get('comment', '')}")


def ordre_respon():
    """Contesta les ressenyes sense resposta dels autors de gbp_respostes.json i treu del fitxer les ja fetes."""
    respostes = json.load(open(RESPOSTES, encoding="utf-8"))
    if not respostes:
        print("cap resposta pendent")
        return
    token = token_acces()
    compte, fitxa, _ = troba_fitxa(token)
    r = crida(f"https://mybusiness.googleapis.com/v4/{compte}/{fitxa}/reviews?pageSize=50&orderBy=updateTime%20desc",
              token=token)
    pendents = {k.strip().lower(): k for k in respostes}
    for rv in r.get("reviews", []):
        autor = rv.get("reviewer", {}).get("displayName", "").strip().lower()
        if autor not in pendents:
            continue
        nom = pendents.pop(autor)
        if rv.get("reviewReply"):
            print(f"ja tenia resposta: {nom}")
        else:
            crida(f"https://mybusiness.googleapis.com/v4/{rv['name']}/reply", {"comment": respostes[nom]},
                  token=token, metode="PUT")
            print(f"contestada: {nom}")
        del respostes[nom]
    for nom in pendents.values():
        print(f"no trobada: {nom} (es queda al fitxer)")
    json.dump(respostes, open(RESPOSTES, "w", encoding="utf-8"), ensure_ascii=False, indent=1)


def ordre_fotos():
    """Puja les fotos de gbp_fotos.json sense «media» (han d'estar ja publicades a la web) i hi apunta el resultat."""
    fotos = json.load(open(FOTOS, encoding="utf-8"))
    token = token_acces()
    compte, fitxa, _ = troba_fitxa(token)
    for f in fotos:
        if f.get("media"):
            continue
        # categories de Google: COVER, PROFILE, LOGO, EXTERIOR, INTERIOR, AT_WORK, TEAMS, ADDITIONAL
        cos = {"mediaFormat": "PHOTO", "locationAssociation": {"category": f.get("categoria", "ADDITIONAL")},
               "sourceUrl": f"{DOMINI}/{f['fitxer']}"}
        if f.get("descripcio"):
            cos["description"] = f["descripcio"]
        r = crida(f"https://mybusiness.googleapis.com/v4/{compte}/{fitxa}/media", cos, token=token)
        f["media"] = r.get("name", "?")
        print(f"pujada: {f['fitxer']} ({cos['locationAssociation']['category']})")
        json.dump(fotos, open(FOTOS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    r = crida(f"https://mybusiness.googleapis.com/v4/{compte}/{fitxa}/media?pageSize=100", token=token)
    print(f"fotos a la fitxa: {r.get('totalMediaItemCount', 0)}")
    for m in r.get("mediaItems", []):
        print(f"  {m.get('createTime', '')[:10]} · {m.get('locationAssociation', {}).get('category', '?')} · "
              f"{m.get('mediaFormat')} · {m.get('googleUrl', '')}")


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
    avui = datetime.now(ZoneInfo("Europe/Madrid")).date().isoformat()  # el runner va en UTC
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
    ordres = {"prova": ordre_prova, "ressenyes": ordre_ressenyes, "publica": ordre_publica, "llista": ordre_llista, "respon": ordre_respon, "fitxa": ordre_fitxa, "edita": ordre_edita, "fotos": ordre_fotos}
    if len(sys.argv) != 2 or sys.argv[1] not in ordres:
        sys.exit(f"ús: python3 gbp.py {'|'.join(ordres)}")
    ordres[sys.argv[1]]()
