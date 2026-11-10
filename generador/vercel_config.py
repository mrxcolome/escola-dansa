"""Genera vercel.json a partir de les mateixes regles que el .htaccess de Webempresa.

Les redireccions es mantenen aquí en format llegible (regex estil Apache) i es
tradueixen al format de Vercel. Si s'afegeix una redirecció, s'afegeix a REDIRECCIONS
i es torna a executar:  python3 generador/vercel_config.py
"""
import json
import os

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# (regex del camí sense la barra inicial, destí) — el mateix ordre que el .htaccess:
# guanya la primera que coincideix. Els grups han de ser no capturadors (?:…).
REDIRECCIONS = [
    # seccions principals de la web antiga (WordPress)
    (r"inici/?", "/"),
    (r"escola/?", "/#escola"),
    (r"(?:activitats|category/activitats)/?", "/#activitats"),
    (r"contacte/?", "/#contacte"),
    # subpàgines antigues d'horaris -> pàgina d'horaris nova
    (r"horaris/(?!index\.(?:html|md)$).+", "/horaris/"),
    # articles del blog amb destí millor que la home
    (r"blog/classes-de-dansa-per-als-mes-petits/?", "/dansa-infantil/"),
    (r"blog/modalitats-de-dansa-a-lescola-de-dansa-cristina-colome/?", "/#activitats"),
    (r"blog/guia-dels-millors-maillots-de-dansa-i-on-comprar-los/?", "/ballet-classic/"),
    (r"blog/escola-de-dansa-cristina-colome/?", "/#escola"),
    (r"blog/beneficis-de-la-dansa-per-a-la-salut-fisica-i-mental/?", "/dansa-adults/"),
    (r"(?:tag|author|category)/.+", "/"),
    (r"inici_xmas(?:/.*)?", "/"),
    (r"casal-infantil-diver-dansa(?:/.*)?", "/dansa-infantil/"),
    (r"stage-juvenil-global-dance(?:/.*)?", "/"),
    # 2a tanda (20 set 2026)
    (r"blog/(?:tag|category)/.+", "/blog/"),
    (r"html/horaris\.htm/?", "/horaris/"),
    (r"html/preus\.htm/?", "/preus/"),
    (r"html/situacio\.htm/?", "/#contacte"),
    (r"html/(?:escola|cristina)\.htm/?", "/#escola"),
    (r"html/.+", "/"),
    (r"estiu[0-9]+(?:/.*)?", "/dansa-infantil/"),
    (r"nadal[0-9]+(?:/.*)?", "/"),
    # 3a tanda (11 oct 2026)
    (r"benvinguda(?:/.*)?", "/"),
    (r"es/bienvenida(?:/.*)?", "/es/"),
    (r"blog/dansa-contemporania-a-barcelona-[^/]*/?", "/dansa-contemporania/"),
    (r"blog/ballet-classic-a-barcelona-[^/]*/?", "/ballet-classic/"),
    (r"blog/hip-hop-a-barcelona-[^/]*/?", "/hip-hop/"),
    (r"blog/torna-el-casal-destiu-[^/]*/?", "/dansa-infantil/"),
    (r"blog/descobreix-lescola-de-dansa-cristina-colome-[^/]*/?", "/#escola"),
    (r"blog/escola-de-dansa-cristina-colome/.+", "/#escola"),
    # 4a tanda (7 nov 2026)
    (r"es/escuela/?", "/es/#escola"),
    (r"blog/author/.+", "/blog/"),
    (r"blog/beneficis-de-la-dansa-per-a-la-salut-fisica-i-mental/.+", "/dansa-adults/"),
    # portades velles del lloc estàtic
    (r"(?:default\.htm|index\.html)/?", "/"),
    # document intern reanomenat (Tramoia -> Backstage)
    (r"tramoia(?:/.*)?", "/backstage/"),
]

LINK = ('<https://escoladansa.com/llms.txt>; rel="describedby llms-txt", '
        '<https://escoladansa.com/sitemap.xml>; rel="sitemap", '
        '<https://escoladansa.com/llms.txt>; rel="service-doc"')

ES_MARKDOWN = [{"type": "header", "key": "accept", "value": ".*text/markdown.*"}]

config = {
    "$schema": "https://openapi.vercel.sh/vercel.json",
    "framework": None,
    "installCommand": "npm install",
    "buildCommand": "python3 generador/vercel_build.py",
    "outputDirectory": "_web",
    "trailingSlash": True,
    "redirects": [
        # www → arrel, en un sol salt (com feia el .htaccess de Webempresa)
        {"source": "/:cami*", "has": [{"type": "host", "value": "www.escoladansa.com"}],
         "destination": "https://escoladansa.com/:cami*", "statusCode": 301},
    ] + [
        {"source": f"/:cami({regex})", "destination": desti, "statusCode": 301}
        for regex, desti in REDIRECCIONS
    ],
    "rewrites": [
        # el formulari de contacte de la home envia a /contacte.php: ara és una funció
        {"source": "/contacte.php", "destination": "/api/contacte"},
        # (el Markdown per a agents, Accept: text/markdown, el fa middleware.js)
    ],
    "headers": [
        {"source": "/(.*)", "headers": [{"key": "Link", "value": LINK}]},
        {"source": "/(robots|llms)\\.txt", "headers": [{"key": "Cache-Control", "value": "public, max-age=3600"}]},
        {"source": "/(.*)\\.md", "headers": [{"key": "Content-Type", "value": "text/markdown; charset=utf-8"}]},
        # la còpia de *.vercel.app no s'ha d'indexar (contingut duplicat)
        {"source": "/(.*)", "has": [{"type": "host", "value": ".*\\.vercel\\.app"}],
         "headers": [{"key": "X-Robots-Tag", "value": "noindex"}]},
    ],
}

if __name__ == "__main__":
    desti = os.path.join(ARREL, "vercel.json")
    with open(desti, "w", encoding="utf-8", newline="\n") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"vercel.json: {len(config['redirects'])} redireccions")
