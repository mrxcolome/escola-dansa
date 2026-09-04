# -*- coding: utf-8 -*-
"""
Generador del blog d'escoladansa.com (CA + ES).
Executa:  python genera_blog.py
- Escriu /blog/index.html i /blog/<slug>/index.html (+ versions /es/blog/).
- REESCRIU sitemap.xml amb totes les pàgines + el blog.
Reutilitza plantilla, CSS, nav i peu de genera_pagines.py: si canvia el disseny
de la web, el blog es regenera igual. Contingut dels posts a blog_posts.py.
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import genera_pagines as gp  # noqa: E402
from blog_posts import POSTS  # noqa: E402

ARREL, DOMINI = gp.ARREL, gp.DOMINI

# CSS propi del blog, afegit al de la plantilla (tokens de la guia d'estils, cap mida nova)
# El blog va EN CLAR per diferenciar-lo de la web: inversió dels tokens de color
# (mateixos noms de variable, valors girats — la resta de la plantilla no es toca).
BLOG_CSS = """
:root{--negre:#f7f4f0;--gris-fosc:#fffdfb;--blanc:#171310;--gris:#6f6862;--vora:rgba(23,19,16,.14)}
body::before{background:radial-gradient(55vmax 55vmax at 85% -10%,rgba(149,0,0,.06),transparent 65%),radial-gradient(45vmax 45vmax at -10% 80%,rgba(77,5,5,.05),transparent 70%)}
nav.solida{background:rgba(247,244,240,.88)}
::selection{color:#f5f2ef}
.boto-ple{color:#f5f2ef}
.cta-final{background:rgba(255,253,251,.85)}
.accio:hover,.idioma-menu a:hover,.post-card:hover{background:rgba(149,0,0,.06)}
.post-img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;display:block;border-radius:20px;margin:0 0 26px}
.article{max-width:760px}
.article .meta-post{font-size:var(--text);color:var(--gris);font-weight:400;font-style:italic;margin-bottom:38px}
.article p{font-size:var(--text);color:var(--gris);font-weight:400;margin:0 0 22px;max-width:720px}
.article h2{margin:54px 0 20px}
.article ul{margin:0 0 22px 20px;max-width:700px}
.article li{font-size:var(--text);color:var(--gris);font-weight:400;margin:10px 0}
.article p strong,.article li strong{color:var(--blanc);font-weight:600}
.article a{color:var(--granat-viu);font-weight:600}
.cat-post{font-size:var(--text-vermells);letter-spacing:.3em;text-transform:uppercase;color:var(--granat-viu);font-weight:600}
.blog-hero{position:relative;display:block;border-radius:24px;overflow:hidden;margin:6px 0 30px;box-shadow:0 18px 50px rgba(23,19,16,.14)}
.blog-hero img{width:100%;height:auto;aspect-ratio:21/9;object-fit:cover;display:block;transition:transform .7s cubic-bezier(.22,1,.36,1)}
.blog-hero:hover img{transform:scale(1.04)}
.blog-hero .vel-hero{position:absolute;inset:0;background:linear-gradient(180deg,rgba(23,19,16,.18) 0%,rgba(23,19,16,.12) 30%,rgba(23,19,16,.92) 100%)}
.blog-hero .hero-cos{position:absolute;left:0;right:0;bottom:0;padding:36px 40px}
.blog-hero .cat-chip{display:inline-block;background:var(--granat-viu);color:#f5f2ef;padding:6px 16px;border-radius:100px;font-size:var(--text-vermells);letter-spacing:.25em;text-transform:uppercase;font-weight:600}
.blog-hero h2{color:#f5f2ef;margin:16px 0 10px;max-width:820px;text-shadow:0 2px 18px rgba(23,19,16,.45)}
.blog-hero p{font-size:var(--text);color:rgba(245,242,239,.85);font-weight:400;max-width:640px;margin:0 0 12px}
.blog-hero .peu-card{font-size:var(--text);color:rgba(245,242,239,.65);font-weight:400;font-style:italic}
.blog-destacats{display:grid;grid-template-columns:1fr 1fr;gap:28px;margin-bottom:34px}
.blog-mig{position:relative;display:block;border-radius:20px;overflow:hidden;box-shadow:0 12px 34px rgba(23,19,16,.1)}
.blog-mig img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform .6s cubic-bezier(.22,1,.36,1)}
.blog-mig:hover img{transform:scale(1.05)}
.blog-mig .vel-hero{position:absolute;inset:0;background:linear-gradient(180deg,rgba(23,19,16,.12) 0%,rgba(23,19,16,.08) 38%,rgba(23,19,16,.9) 100%)}
.blog-mig .hero-cos{position:absolute;left:0;right:0;bottom:0;padding:24px 26px}
.blog-mig .cat-chip{display:inline-block;background:var(--granat-viu);color:#f5f2ef;padding:5px 13px;border-radius:100px;font-size:var(--text-vermells);letter-spacing:.25em;text-transform:uppercase;font-weight:600}
.blog-mig h3{color:#f5f2ef;font-size:var(--text);font-weight:800;margin:12px 0 6px}
.blog-mig .peu-card{font-size:var(--text);color:rgba(245,242,239,.65);font-weight:400;font-style:italic}
.posts-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(290px,1fr));gap:28px;margin-top:6px}
.post-card{background:var(--gris-fosc);padding:0;display:flex;flex-direction:column;border-radius:20px;overflow:hidden;box-shadow:0 8px 26px rgba(23,19,16,.07);transition:transform .35s cubic-bezier(.22,1,.36,1),box-shadow .35s}
.post-card:hover{transform:translateY(-5px);box-shadow:0 18px 44px rgba(23,19,16,.13);background:var(--gris-fosc)}
.pc-img{position:relative;overflow:hidden}
.pc-img img{width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;display:block;transition:transform .6s cubic-bezier(.22,1,.36,1)}
.post-card:hover .pc-img img{transform:scale(1.06)}
.pc-img .cat-chip{position:absolute;top:14px;left:14px;background:rgba(149,0,0,.92);color:#f5f2ef;padding:5px 13px;border-radius:100px;font-size:var(--text-vermells);letter-spacing:.25em;text-transform:uppercase;font-weight:600}
.pc-cos{padding:24px 26px 28px;display:flex;flex-direction:column;gap:12px;flex:1}
.post-card h3{font-size:var(--text);font-weight:800}
.post-card p{font-size:var(--text);color:var(--gris);font-weight:400;flex:1}
.post-card .peu-card,.pc-cos .peu-card{font-size:var(--text);color:var(--gris);font-weight:400;font-style:italic}
@media (max-width:700px){
.blog-hero{border-radius:20px}
.blog-hero img{aspect-ratio:16/10}
.blog-hero .vel-hero,.blog-mig .vel-hero{display:none}
.blog-hero .hero-cos{position:static;display:block;background:var(--gris-fosc);padding:20px 18px 24px}
.blog-hero h2{color:var(--blanc);text-shadow:none;margin:12px 0 8px}
.blog-hero p{color:var(--gris);margin:0 0 10px}
.blog-hero .peu-card{color:var(--gris)}
.blog-mig .hero-cos{position:static;display:block;background:var(--gris-fosc);padding:18px 18px 22px}
.blog-mig h3{color:var(--blanc)}
.blog-mig .peu-card{color:var(--gris)}
.blog-destacats{grid-template-columns:1fr;gap:22px}
.posts-grid{gap:22px}
}
"""
gp.CSS += BLOG_CSS

# registrar els slugs del blog perquè genera() resolgui les hreflang CA<->ES
for _p in POSTS:
    gp.SLUG_ES[f"blog/{_p['slug']}"] = f"blog/{_p['slug_es']}"

PER_SLUG = {p["slug"]: p for p in POSTS}
ESCOLA_LD = {
    "@type": "Organization",
    "name": "Escola de Dansa Cristina Colomé",
    "url": DOMINI + "/",
    "logo": DOMINI + "/assets/favicon-512.png",
}


def ld_post(p, lang):
    if lang == "ca":
        url, nom_blog, inici = f"{DOMINI}/blog/{p['slug']}/", "blog", ("inici", DOMINI + "/", DOMINI + "/blog/")
        titol, desc, faqs = p["h1"], p["desc"], p["faqs"]
    else:
        url, nom_blog, inici = f"{DOMINI}/es/blog/{p['slug_es']}/", "blog", ("inicio", DOMINI + "/es/", DOMINI + "/es/blog/")
        titol, desc, faqs = p["h1_es"], p["desc_es"], p["faqs_es"]
    graph = [
        {
            "@type": "BlogPosting",
            "@id": url + "#post",
            "headline": titol,
            "description": desc,
            "url": url,
            "mainEntityOfPage": url,
            "inLanguage": lang,
            "datePublished": p["data"],
            "dateModified": p["data"],
            "image": f"{DOMINI}/assets/{p['og']}",
            "author": ESCOLA_LD,
            "publisher": ESCOLA_LD,
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": inici[0], "item": inici[1]},
                {"@type": "ListItem", "position": 2, "name": nom_blog, "item": inici[2]},
                {"@type": "ListItem", "position": 3, "name": titol, "item": url},
            ],
        },
        {
            "@type": "FAQPage",
            "@id": url + "#faq",
            "mainEntity": [
                {"@type": "Question", "name": gp.cap(q),
                 "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in faqs
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, indent=1)


def chips_relacionats(p, lang):
    """Xips 'segueix llegint': altres posts + pàgines de l'escola relacionades."""
    chips = []
    for s in p.get("related_posts", []):
        rp = PER_SLUG.get(s)
        if not rp:
            continue
        if lang == "ca":
            chips.append(f'      <a href="/blog/{rp["slug"]}/">{gp.esc(rp["h1"])}</a>')
        else:
            chips.append(f'      <a href="/es/blog/{rp["slug_es"]}/">{gp.esc(rp["h1_es"])}</a>')
    per_slug_pag = {x["slug"]: x for x in gp.PAGINES}
    for s in p.get("related_pagines", []):
        pag = per_slug_pag.get(s)
        if not pag:
            continue
        if lang == "ca":
            chips.append(f'      <a href="/{s}/">{gp.esc(pag["nom"])}</a>')
        else:
            from traduccions_es import TRADUCCIONS_ES
            nom_es = TRADUCCIONS_ES.get(s, {}).get("nom", pag["nom"])
            chips.append(f'      <a href="/es/{gp.SLUG_ES[s]}/">{gp.esc(nom_es)}</a>')
    return "\n".join(chips)


def cos_post(p, lang):
    if lang == "ca":
        cos, cat, data, faqs = p["cos"], p["categoria"], p["data_ca"], p["faqs"]
        et_seguir, h2_seguir = "segueix llegint", "també et pot interessar"
        et_nl, h2_nl = "newsletter", "no et perdis cap article"
        txt_nl = ("Un cop al mes, els articles nous i les novetats de l'escola directes al teu correu. "
                  "Sense soroll, i et pots donar de baixa quan vulguis.")
        boto_nl, href_nl = "apunta-m'hi", "/#newsletter"
        lectura = f"{data} · {p['minuts']} min de lectura"
    else:
        cos, cat, data, faqs = p["cos_es"], p["categoria_es"], p["data_es"], p["faqs_es"]
        et_seguir, h2_seguir = "sigue leyendo", "también te puede interesar"
        et_nl, h2_nl = "newsletter", "no te pierdas ningún artículo"
        txt_nl = ("Una vez al mes, los artículos nuevos y las novedades de la escuela directos a tu correo. "
                  "Sin ruido, y puedes darte de baja cuando quieras.")
        boto_nl, href_nl = "apúntame", "/es/#newsletter"
        lectura = f"{data} · {p['minuts']} min de lectura"
    alt = p["img_alt"] if lang == "ca" else p["img_alt_es"]
    faqs_html = gp.bloc_faqs({"faqs": faqs})
    return f"""
  <section class="reveal article">
    <img class="post-img" src="/assets/{p['img']}" alt="{gp.esc(alt)}" width="1600" height="900">
    <p class="meta-post">{gp.esc(lectura)}</p>{cos}
  </section>
{faqs_html}
  <section class="reveal">
    <div class="etiqueta">{et_seguir}</div>
    <h2>{h2_seguir}</h2>
    <div class="relacionats">
{chips_relacionats(p, lang)}
    </div>
  </section>
  <section class="reveal">
    <div class="etiqueta">{et_nl}</div>
    <h2>{h2_nl}</h2>
    <p class="text-gran">{txt_nl}</p>
    <p style="margin-top:24px"><a class="boto boto-buit" href="{href_nl}">{boto_nl}</a></p>
  </section>"""


def pagina_post_ca(p):
    pd = {
        "slug": f"blog/{p['slug']}",
        "nom": p["h1"],
        "nom_wa": p["nom_wa"],
        "title": p["title"],
        "desc": p["desc"],
        "h1": p["h1"],
        "intro": p["intro"],
        "etiqueta_capsal": f"blog · {p['categoria']}",
        "molla_mig": '<a href="/blog/">blog</a> · ',
        "og": f"{DOMINI}/assets/{p['og']}",
        "cos": cos_post(p, "ca"),
        "ld": ld_post(p, "ca"),
    }
    return gp.genera(pd)


def pagina_post_es(p):
    pd = {
        "slug": f"es/blog/{p['slug_es']}",
        "slug_ca": f"blog/{p['slug']}",
        "lang": "es",
        "nom": p["h1_es"],
        "nom_wa": p["nom_wa_es"],
        "title": p["title_es"],
        "desc": p["desc_es"],
        "h1": p["h1_es"],
        "intro": p["intro_es"],
        "etiqueta_capsal": f"blog · {p['categoria_es']}",
        "molla_mig": '<a href="/es/blog/">blog</a> · ',
        "og": f"{DOMINI}/assets/{p['og']}",
        "cos": cos_post(p, "es"),
        "ld": ld_post(p, "es"),
    }
    pagina = gp.genera(pd)
    for a, b in gp.fixos_es():
        pagina = pagina.replace(a, b)
    return pagina


def _camps_targeta(p, lang):
    if lang == "ca":
        return (f"/blog/{p['slug']}/", p["categoria"], p["h1"], p["excerpt"],
                f"{p['data_ca']} · {p['minuts']} min de lectura", p["img_alt"])
    return (f"/es/blog/{p['slug_es']}/", p["categoria_es"], p["h1_es"], p["excerpt_es"],
            f"{p['data_es']} · {p['minuts']} min de lectura", p["img_alt_es"])


def targeta_hero(p, lang):
    href, cat, titol, exc, peu, alt = _camps_targeta(p, lang)
    return (f'      <a class="blog-hero" href="{href}">'
            f'<img src="/assets/{p["img"]}" alt="{gp.esc(alt)}" width="1600" height="900">'
            f'<span class="vel-hero"></span>'
            f'<span class="hero-cos"><span class="cat-chip">{gp.esc(cat)}</span>'
            f'<h2>{gp.esc(titol)}</h2><p>{gp.esc(exc)}</p>'
            f'<span class="peu-card">{gp.esc(peu)}</span></span></a>')


def targeta_mig(p, lang):
    href, cat, titol, exc, peu, alt = _camps_targeta(p, lang)
    return (f'      <a class="blog-mig" href="{href}">'
            f'<img src="/assets/{p["img"]}" alt="{gp.esc(alt)}" loading="lazy" width="1600" height="900">'
            f'<span class="vel-hero"></span>'
            f'<span class="hero-cos"><span class="cat-chip">{gp.esc(cat)}</span>'
            f'<h3>{gp.esc(titol)}</h3>'
            f'<span class="peu-card">{gp.esc(peu)}</span></span></a>')


def targeta(p, lang):
    if lang == "ca":
        href, cat, titol = f"/blog/{p['slug']}/", p["categoria"], p["h1"]
        exc, peu, alt = p["excerpt"], f"{p['data_ca']} · {p['minuts']} min de lectura", p["img_alt"]
    else:
        href, cat, titol = f"/es/blog/{p['slug_es']}/", p["categoria_es"], p["h1_es"]
        exc, peu, alt = p["excerpt_es"], f"{p['data_es']} · {p['minuts']} min de lectura", p["img_alt_es"]
    return (f'      <a class="post-card" href="{href}">'
            f'<span class="pc-img"><img src="/assets/{p["img"]}" alt="{gp.esc(alt)}" loading="lazy" width="1600" height="900">'
            f'<span class="cat-chip">{gp.esc(cat)}</span></span>'
            f'<div class="pc-cos">'
            f'<h3>{gp.esc(titol)}</h3><p>{gp.esc(exc)}</p>'
            f'<span class="peu-card">{gp.esc(peu)}</span></div></a>')


def ld_index(lang):
    if lang == "ca":
        url, inici = DOMINI + "/blog/", ("inici", DOMINI + "/")
        nom = "el blog de l'escola de dansa cristina colomé"
        desc = "Consells de dansa per a famílies i adults, i vida d'escola, des de Sant Gervasi (Barcelona)."
    else:
        url, inici = DOMINI + "/es/blog/", ("inicio", DOMINI + "/es/")
        nom = "el blog de la escola de dansa cristina colomé"
        desc = "Consejos de danza para familias y adultos, y vida de escuela, desde Sant Gervasi (Barcelona)."
    graph = [
        {
            "@type": "Blog",
            "@id": url + "#blog",
            "name": nom,
            "description": desc,
            "url": url,
            "inLanguage": lang,
            "publisher": ESCOLA_LD,
            "blogPost": [
                {"@type": "BlogPosting",
                 "headline": (p["h1"] if lang == "ca" else p["h1_es"]),
                 "url": (f"{DOMINI}/blog/{p['slug']}/" if lang == "ca"
                         else f"{DOMINI}/es/blog/{p['slug_es']}/"),
                 "datePublished": p["data"]}
                for p in POSTS
            ],
        },
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": inici[0], "item": inici[1]},
                {"@type": "ListItem", "position": 2, "name": "blog", "item": url},
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": graph},
                      ensure_ascii=False, indent=1)


def pagina_index(lang):
    posts_ordenats = sorted(POSTS, key=lambda p: p["data"], reverse=True)
    hero = targeta_hero(posts_ordenats[0], lang)
    mitjans = "\n".join(targeta_mig(p, lang) for p in posts_ordenats[1:3])
    grid = "\n".join(targeta(p, lang) for p in posts_ordenats[3:])
    if lang == "ca":
        pd = {
            "slug": "blog",
            "nom": "blog",
            "nom_wa": "dansa",
            "title": "el blog · consells de dansa per a famílies i adults · escola de dansa cristina colomé",
            "desc": "El blog de l'escola de dansa Cristina Colomé (Barcelona): consells per a famílies i adults, guies per triar estil i edat per començar, i vida d'escola. Un article nou cada setmana.",
            "h1": "el blog",
            "intro": "Consells de dansa per a famílies i adults, guies per començar i vida d'escola — escrit des de la sala, no des d'un despatx. Un article nou cada setmana.",
            "etiqueta_capsal": "consells, dansa i vida d'escola",
            "molla_mig": "",
            "cos": f"""
  <section>
{hero}
    <div class="blog-destacats reveal">
{mitjans}
    </div>
    <div class="posts-grid reveal">
{grid}
    </div>
  </section>""",
            "ld": ld_index("ca"),
        }
        return gp.genera(pd)
    pd = {
        "slug": "es/blog",
        "slug_ca": "blog",
        "lang": "es",
        "nom": "blog",
        "nom_wa": "danza",
        "title": "el blog · consejos de danza para familias y adultos · escola de dansa cristina colomé",
        "desc": "El blog de la escuela de danza Cristina Colomé (Barcelona): consejos para familias y adultos, guías para elegir estilo y edad para empezar, y vida de escuela. Un artículo nuevo cada semana.",
        "h1": "el blog",
        "intro": "Consejos de danza para familias y adultos, guías para empezar y vida de escuela — escrito desde la sala, no desde un despacho. Un artículo nuevo cada semana.",
        "etiqueta_capsal": "consejos, danza y vida de escuela",
        "molla_mig": "",
        "cos": f"""
  <section>
{hero}
    <div class="blog-destacats reveal">
{mitjans}
    </div>
    <div class="posts-grid reveal">
{grid}
    </div>
  </section>""",
        "ld": ld_index("es"),
    }
    pagina = gp.genera(pd)
    for a, b in gp.fixos_es():
        pagina = pagina.replace(a, b)
    return pagina


# ─────────────────────────────────────────────────────────────────────────────
# SITEMAP — font única: pàgines del generador + home + blog
# ─────────────────────────────────────────────────────────────────────────────
LASTMOD_PAGINES = "2026-09-02"  # actualitzar quan es toquin les pàgines estàtiques


def sitemap():
    files = [(DOMINI + "/", LASTMOD_PAGINES, "monthly", "1.0"),
             (DOMINI + "/es/", LASTMOD_PAGINES, "monthly", "1.0")]
    for p in gp.PAGINES:
        prio = "0.9" if p["slug"] in ("horaris", "preus") else "0.8"
        files.append((f"{DOMINI}/{p['slug']}/", LASTMOD_PAGINES, "monthly", prio))
        files.append((f"{DOMINI}/es/{gp.SLUG_ES[p['slug']]}/", LASTMOD_PAGINES, "monthly", prio))
    data_blog = max(p["data"] for p in POSTS)
    files.append((DOMINI + "/blog/", data_blog, "weekly", "0.8"))
    files.append((DOMINI + "/es/blog/", data_blog, "weekly", "0.8"))
    for p in POSTS:
        files.append((f"{DOMINI}/blog/{p['slug']}/", p["data"], "monthly", "0.7"))
        files.append((f"{DOMINI}/es/blog/{p['slug_es']}/", p["data"], "monthly", "0.7"))
    linies = "\n".join(
        f"  <url><loc>{u}</loc><lastmod>{lm}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>"
        for u, lm, cf, pr in files)
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
            f"{linies}\n</urlset>\n")


# ─────────────────────────────────────────────────────────────────────────────
# FEED RSS — /feed.xml (CA) i /es/feed.xml (ES)
# ─────────────────────────────────────────────────────────────────────────────
def _rfc822(data):
    """'2026-09-01' -> data RFC 822 (08:00 hora de Madrid)."""
    from datetime import datetime, timezone, timedelta
    from email.utils import format_datetime
    d = datetime.strptime(data, "%Y-%m-%d").replace(hour=8, tzinfo=timezone(timedelta(hours=2)))
    return format_datetime(d)


def feed_rss(lang):
    if lang == "ca":
        url_blog, url_feed = DOMINI + "/blog/", DOMINI + "/feed.xml"
        titol = "el blog de l'escola de dansa cristina colomé"
        desc = "Consells de dansa per a famílies i adults, i vida d'escola, des de Sant Gervasi (Barcelona)."
    else:
        url_blog, url_feed = DOMINI + "/es/blog/", DOMINI + "/es/feed.xml"
        titol = "el blog de la escola de dansa cristina colomé"
        desc = "Consejos de danza para familias y adultos, y vida de escuela, desde Sant Gervasi (Barcelona)."
    items = []
    for p in sorted(POSTS, key=lambda x: x["data"], reverse=True):
        if lang == "ca":
            u, t, e = f"{DOMINI}/blog/{p['slug']}/", p["h1"], p["desc"]
        else:
            u, t, e = f"{DOMINI}/es/blog/{p['slug_es']}/", p["h1_es"], p["desc_es"]
        items.append(f"""    <item>
      <title>{gp.esc(t)}</title>
      <link>{u}</link>
      <guid isPermaLink="true">{u}</guid>
      <pubDate>{_rfc822(p['data'])}</pubDate>
      <description>{gp.esc(e)}</description>
      <enclosure url="{DOMINI}/assets/{p['img']}" type="image/jpeg" length="150000"/>
    </item>""")
    data_max = _rfc822(max(p["data"] for p in POSTS))
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>{gp.esc(titol)}</title>
    <link>{url_blog}</link>
    <atom:link href="{url_feed}" rel="self" type="application/rss+xml"/>
    <description>{gp.esc(desc)}</description>
    <language>{lang}</language>
    <lastBuildDate>{data_max}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""


def retocs_head(pagina, lang):
    """Autodiscovery del feed + theme-color clar (el blog va en fons blanc)."""
    feed = "/feed.xml" if lang == "ca" else "/es/feed.xml"
    titol = "blog escola de dansa cristina colomé" + (" (es)" if lang == "es" else "")
    pagina = pagina.replace(
        '<link rel="icon"',
        f'<link rel="alternate" type="application/rss+xml" title="{titol}" href="{feed}">\n<link rel="icon"', 1)
    return pagina.replace('<meta name="theme-color" content="#0a0a0a">',
                          '<meta name="theme-color" content="#f7f4f0">', 1)


# ─────────────────────────────────────────────────────────────────────────────
# MÒDUL DEL BLOG A LA HOME — injecta els 3 posts més nous entre els marcadors
# <!-- BLOG-AUTO --> ... <!-- /BLOG-AUTO --> de index.html (CA; l'ES el fa
# genera_home_es.py amb parelles dinàmiques). Executa'l ABANS de genera_home_es.
# ─────────────────────────────────────────────────────────────────────────────
def modul_home():
    cami = os.path.join(ARREL, "index.html")
    with open(cami, encoding="utf-8") as f:
        h = f.read()
    inici, fi = "<!-- BLOG-AUTO -->", "<!-- /BLOG-AUTO -->"
    if inici not in h or fi not in h:
        print("AVIS: index.html sense marcadors BLOG-AUTO — modul de la home NO actualitzat")
        return
    posts3 = sorted(POSTS, key=lambda p: p["data"], reverse=True)[:3]
    cards = "\n".join(
        f'  <a class="bloc-post reveal" href="/blog/{p["slug"]}/">'
        f'<div><span class="cat-post">{gp.esc(p["categoria"])}</span><h3>{gp.esc(p["h1"])}</h3>'
        f'<p>{gp.esc(p["excerpt"])}</p><span class="peu-card">{gp.esc(p["data_ca"])}</span></div></a>'
        for p in posts3)
    pre, resta = h.split(inici, 1)
    _mig, post = resta.split(fi, 1)
    with open(cami, "w", encoding="utf-8", newline="\n") as f:
        f.write(pre + inici + "\n" + cards + "\n  " + fi + post)
    print(f"modul del blog injectat a index.html ({len(posts3)} targetes)")


def escriu(cami, contingut):
    os.makedirs(os.path.dirname(cami), exist_ok=True)
    with open(cami, "w", encoding="utf-8") as f:
        f.write(contingut)


def main():
    escriu(os.path.join(ARREL, "blog", "index.html"), retocs_head(pagina_index("ca"), "ca"))
    escriu(os.path.join(ARREL, "es", "blog", "index.html"), retocs_head(pagina_index("es"), "es"))
    for p in POSTS:
        escriu(os.path.join(ARREL, "blog", p["slug"], "index.html"),
               retocs_head(pagina_post_ca(p), "ca"))
        escriu(os.path.join(ARREL, "es", "blog", p["slug_es"], "index.html"),
               retocs_head(pagina_post_es(p), "es"))
    escriu(os.path.join(ARREL, "feed.xml"), feed_rss("ca"))
    escriu(os.path.join(ARREL, "es", "feed.xml"), feed_rss("es"))
    modul_home()
    with open(os.path.join(ARREL, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap())
    print(f"blog: {len(POSTS)} posts CA + {len(POSTS)} ES + 2 index + 2 feeds; sitemap.xml reescrit ({sitemap().count('<url>')} URLs)")


if __name__ == "__main__":
    main()
