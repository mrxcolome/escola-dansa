# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Web estàtica de l'Escola de Dansa Cristina Colomé (https://escoladansa.com), en català (per defecte) i castellà (`/es/`). Tot el repo, els comentaris i els missatges de commit són en català.

## Publicar

- Cada push a `main` desplega la web a Webempresa per FTPS (`.github/workflows/deploy.yml`, només fitxers canviats). El que hi ha a `main` és el que surt publicat. `generador/` no es puja.
- Després d'un desplegament que afegeixi o canviï URLs: `python3 generador/ping_indexnow.py` (notifica totes les URL del sitemap a IndexNow/Bing).
- El servidor serveix les imatges amb `max-age` d'un any: per substituir una imatge, crea un fitxer amb **nom nou** (p. ex. `blog-x-2.jpg`) en lloc de sobreescriure'l.
- Previsualització local: `python3 -m http.server` des de l'arrel.

## Generadors (`generador/`, Python 3 sense dependències)

La majoria de l'HTML és **generat**: no editis a mà els `index.html` de les pàgines d'activitat, horaris, preus, blog ni `/es/`, edita el generador i regenera. Ordre:

```bash
cd generador
python3 genera_pagines.py   # 16 pàgines CA + 16 ES (activitats, públics, horaris, preus)
python3 genera_blog.py      # blog CA/ES, feeds, mòdul del blog a la home i REESCRIU sitemap.xml
python3 genera_home_es.py   # es/index.html a partir d'index.html
python3 genera_markdown.py  # un index.md al costat de cada index.html
```

Comprovació bàsica: regenerar sense haver tocat res no ha de produir cap diff (`git status`). `genera_home_es.py` avisa si alguna cadena de la taula `PARELLES` ja no es troba.

Com encaixa:
- `genera_pagines.py` té el contingut CA de les pàgines (`PAGINES`), la plantilla, el CSS i el JS comuns, la graella d'horaris (`GRAELLA`) i les tarifes (`TARIFA_*`). Constants a revisar cada curs: `CURS`.
- `traduccions_es.py` té el contingut ES per slug. El que no hi és s'hereta del CA. Les cadenes fixes de la plantilla es tradueixen amb les parelles de `fixos_es()`: **un text nou a la plantilla necessita la seva parella ES allà**. Els slugs ES són a `SLUG_ES`.
- `genera_blog.py` reutilitza plantilla i CSS de `genera_pagines.py` (amb `BLOG_CSS` per sobre, tema clar). Els posts són a `blog_posts.py` (llista `POSTS`, un diccionari per post amb camps CA i `*_es`; vegeu-ne un d'existent com a model). Les imatges van a `assets/` a 1600×900. `LASTMOD_PAGINES` (data del sitemap per a les pàgines estàtiques) s'ha d'actualitzar quan es toquen aquestes pàgines.
- La home CA (`index.html`) és **feta a mà** i porta una còpia pròpia del CSS i del JS comuns: un canvi de disseny global s'ha d'aplicar a `genera_pagines.py` i a `index.html`. Només la zona entre `<!-- BLOG-AUTO -->` i `<!-- /BLOG-AUTO -->` la reescriu `genera_blog.py`.
- `.htaccess`: redireccions 301 de la web antiga (WordPress i pre-WordPress), canònic https sense www, i negociació `Accept: text/markdown` → `index.md`.

## Convencions

- Estil de la casa en minúscula (títols, botons, navegació). Excepció: dins dels posts del blog els titulars i el cos van amb majúscula inicial (`maj()` i `cos_amb_majuscules()` a `genera_blog.py`).
- Google Analytics (GA4) només es carrega si l'usuari accepta l'avís de galetes (`localStorage` `galetes`). Rebutjar ha de ser tan fàcil com acceptar.
- Formulari de contacte: `contacte.php`. Newsletter: Mailchimp per JSONP des de la plantilla.
- Missatges de commit: `àrea: descripció` (`blog:`, `seo:`, `galetes:`, `dossier:`…), en català.

## Seccions internes (noindex, bloquejades a `robots.txt`)

- `seo/index.html`: dashboard i pla SEO, editat a mà. Les xifres de Google Search Console i Bing les aporta el Xavi (l'agent no hi té accés). Quan es fa una tasca del pla, es marca la `<li>` com a `class="fet"`.
- `dossier/`, `backstage/`, `google/`: documents interns.
- `memoria/`: àrea privada amb un arxiu xifrat (`memoria-claude.zip.aes`).
