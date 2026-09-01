# -*- coding: utf-8 -*-
"""
Notifica a IndexNow (Bing, Yandex...) totes les URL del sitemap.
Executa:  python ping_indexnow.py
Requisit: el fitxer <clau>.txt ha d'estar pujat a l'arrel d'escoladansa.com.
"""
import io
import json
import os
import re
import urllib.request

ACI = os.path.dirname(os.path.abspath(__file__))
CLAU = io.open(os.path.join(ACI, "indexnow_clau.txt")).read().strip()
SITEMAP = os.path.join(os.path.dirname(ACI), "sitemap.xml")

urls = re.findall(r"<loc>(.*?)</loc>", io.open(SITEMAP, encoding="utf-8").read())
carrega = {
    "host": "escoladansa.com",
    "key": CLAU,
    "keyLocation": f"https://escoladansa.com/{CLAU}.txt",
    "urlList": urls,
}
peticio = urllib.request.Request(
    "https://api.indexnow.org/indexnow",
    data=json.dumps(carrega).encode(),
    headers={"Content-Type": "application/json; charset=utf-8"},
)
resposta = urllib.request.urlopen(peticio, timeout=30)
print(f"IndexNow: {resposta.status} · {len(urls)} URL notificades")
