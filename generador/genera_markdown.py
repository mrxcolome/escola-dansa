# -*- coding: utf-8 -*-
"""
Markdown per a agents d'IA: genera un index.md al costat de cada index.html
(home, 16 pàgines CA + 16 ES, portada del blog i cada post CA/ES).
El .htaccess serveix aquests .md quan la petició porta Accept: text/markdown
(negociació de contingut — Cloudflare «Markdown for Agents»).

Us: python genera_markdown.py   (després de genera_pagines i genera_blog)
"""
import html
import io
import os
import re

import blog_posts as bp
import genera_pagines as gp
from traduccions_es import TRADUCCIONS_ES

ARREL = gp.ARREL
PEU_CA = (f"\n---\n\nescola de dansa cristina colomé · Carrer de Craywinckel, 25, "
          f"08022 Barcelona (Sant Gervasi) · tel. {gp.TEL} · https://escoladansa.com\n"
          f"la primera classe de prova és gratuïta.\n")
PEU_ES = (f"\n---\n\nescola de dansa cristina colomé · Carrer de Craywinckel, 25, "
          f"08022 Barcelona (Sant Gervasi) · tel. {gp.TEL} · https://escoladansa.com/es/\n"
          f"la primera clase de prueba es gratuita.\n")


def escriu(cami_rel, text):
    ruta = os.path.join(ARREL, cami_rel)
    os.makedirs(os.path.dirname(ruta), exist_ok=True)
    io.open(ruta, 'w', encoding='utf-8', newline='\n').write(text)


def html_a_md(s):
    """Conversor petit i suficient per al cos HTML dels posts del blog."""
    s = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', s, flags=re.S)
    s = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', s, flags=re.S)
    s = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>', r'**\1**', s, flags=re.S)
    s = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>', r'*\1*', s, flags=re.S)
    s = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', s, flags=re.S)
    s = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', s, flags=re.S)
    s = re.sub(r'</?(?:ul|ol)[^>]*>', '\n', s)
    s = re.sub(r'<p[^>]*>', '\n', s)
    s = re.sub(r'</p>', '\n', s)
    s = re.sub(r'<br\s*/?>', '\n', s)
    s = re.sub(r'<[^>]+>', '', s)  # qualsevol resta de marcatge
    s = html.unescape(s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    return s.strip()


def taula_md(capcalera, files):
    linies = []
    if capcalera:
        linies.append('| ' + ' | '.join(capcalera) + ' |')
        linies.append('|' + '---|' * len(capcalera))
    for f in files:
        linies.append('| ' + ' | '.join(str(v) for v in f) + ' |')
    return '\n'.join(linies)


def md_pagina(p, es=False):
    t = TRADUCCIONS_ES.get(p['slug'], {}) if es else {}
    camp = lambda k: t.get(k, p.get(k, ''))
    beneficis = t.get('beneficis', p.get('beneficis', []))
    faqs = t.get('faqs', p.get('faqs', []))
    linies = [f"# {camp('h1')}", '', camp('intro'), '']
    linies += [('## para quién' if es else '## per a qui'), '', camp('per_a_qui'), '']
    if beneficis:
        linies.append('## beneficis' if not es else '## beneficios')
        linies.append('')
        for titol, text in beneficis:
            linies.append(f"- **{titol}**: {text}")
        linies.append('')
    horaris = p.get('horaris') or []
    if horaris:
        linies.append(f"## {'horarios' if es else 'horaris'} · {'curso' if es else 'curs'} {gp.CURS}")
        linies.append('')
        files = []
        for dia, hora, grup, sala in horaris:
            if es:
                dia = gp.TRAD_DIES.get(dia, dia)
                grup = gp._trad_grup(grup)
                for a, b in sorted(gp.TRAD_ACT.items(), key=lambda x: -len(x[0])):
                    grup = grup.replace(a, b)
                sala = sala.replace('sala', 'sala')
            files.append((dia, hora, grup, sala))
        capc = ('día', 'hora', 'grupo', 'sala') if es else ('dia', 'hora', 'grup', 'sala')
        linies.append(taula_md(capc, files))
        linies.append('')
    if es:
        linies += ['## precios', '',
                   'cuotas por número de días semanales: desde 56 €/mes (infantil) y 60 €/mes '
                   '(juvenil y adultos). Todas las tarifas: https://escoladansa.com/es/precios/', '']
    else:
        linies += ['## preus', '',
                   'quotes pel nombre de dies setmanals: des de 56 €/mes (infantil) i 60 €/mes '
                   '(juvenil i adults). Totes les tarifes: https://escoladansa.com/preus/', '']
    if faqs:
        linies.append('## preguntas frecuentes' if es else '## preguntes freqüents')
        linies.append('')
        for q, a in faqs:
            linies += [f"### {q}", '', a, '']
    return '\n'.join(linies) + (PEU_ES if es else PEU_CA)


def md_horaris(es=False):
    linies = [f"# {'horarios' if es else 'horaris'} · {'curso' if es else 'curs'} {gp.CURS}", '']
    for dia, files in gp.GRAELLA.items():
        linies.append(f"## {gp.TRAD_DIES.get(dia, dia) if es else dia}")
        linies.append('')
        fs = []
        for h, nom, grup, sala in files:
            if es:
                nom = gp.TRAD_ACT.get(nom, nom)
                grup = gp._trad_grup(grup) if grup else grup
            fs.append((h, nom, grup or '', sala))
        linies.append(taula_md(('hora', 'actividad', 'grupo', 'sala') if es else ('hora', 'activitat', 'grup', 'sala'), fs))
        linies.append('')
    return '\n'.join(linies) + (PEU_ES if es else PEU_CA)


def md_preus(es=False):
    def trad_fila(f):
        if not es:
            return f
        nom = f[0].replace('infantil', 'infantil').replace('juvenil i adults', 'juvenil y adultos')
        nom = nom.replace("més d'1 h", 'más de 1 h').replace('fins 1 h', 'hasta 1 h')
        return (nom,) + tuple(f[1:])
    capc = ('', '1 día', '2 días', '3 días', '4 días') if es else ('', '1 dia', '2 dies', '3 dies', '4 dies')
    linies = [f"# {'precios' if es else 'preus'} · {'curso' if es else 'curs'} {gp.CURS}", '',
              '## cuota mensual' if es else '## quota mensual', '',
              taula_md(capc, [trad_fila(f) for f in gp.TARIFA_MENSUAL]), '',
              '## cuota trimestral' if es else '## quota trimestral', '',
              taula_md(capc, [trad_fila(f) for f in gp.TARIFA_TRIMESTRAL]), '',
              '## matrícula i altres' if not es else '## matrícula y otros', '',
              taula_md(None, gp.TARIFA_ALTRES), '']
    return '\n'.join(linies) + (PEU_ES if es else PEU_CA)


def md_home(es=False):
    activitats = [p for p in gp.PAGINES if p.get('horaris')]
    linies = [
        '# escola de dansa cristina colomé · Sant Gervasi, Barcelona', '',
        ('Escuela de danza en Barcelona con más de 25 años de historia: clásico, contemporáneo, '
         'jazz, hip-hop, claqué, español, danza oriental y más, para todas las edades y niveles.'
         if es else
         'Escola de dansa a Barcelona amb més de 25 anys d’història: clàssic, contemporani, '
         'jazz, hip-hop, claqué, espanyol, dansa oriental i més, per a totes les edats i nivells.'), '',
        '## actividades' if es else '## activitats', '',
    ]
    for p in gp.PAGINES:
        if p['slug'] in ('horaris', 'preus'):
            continue
        slug = f"es/{gp.SLUG_ES[p['slug']]}" if es else p['slug']
        t = TRADUCCIONS_ES.get(p['slug'], {}) if es else {}
        linies.append(f"- [{t.get('h1', p['h1'])}](https://escoladansa.com/{slug}/)")
    del activitats
    mes = 'es/' if es else ''
    linies += ['',
               f"## {'información práctica' if es else 'informació pràctica'}", '',
               f"- {'horarios' if es else 'horaris'}: https://escoladansa.com/{mes}{'horarios' if es else 'horaris'}/",
               f"- {'precios' if es else 'preus'}: https://escoladansa.com/{mes}{'precios' if es else 'preus'}/",
               f"- blog: https://escoladansa.com/{mes}blog/",
               f"- {'dirección' if es else 'adreça'}: Carrer de Craywinckel, 25, 08022 Barcelona (Sant Gervasi – la Bonanova, FGC Av. Tibidabo)",
               f"- {'teléfono' if es else 'telèfon'}: {gp.TEL}",
               ('- la primera clase de prueba es gratuita' if es else '- la primera classe de prova és gratuïta'), '']
    return '\n'.join(linies) + (PEU_ES if es else PEU_CA)


def md_post(p, es=False):
    suf = '_es' if es else ''
    linies = [f"# {p['h1' + suf]}", '',
              f"*{p['data_es' if es else 'data_ca']} · {p['minuts']} min*", '',
              p['intro' + suf], '',
              html_a_md(p['cos' + suf]), '']
    faqs = p.get('faqs' + suf) or []
    if faqs:
        linies += ['## preguntas frecuentes' if es else '## preguntes freqüents', '']
        for q, a in faqs:
            linies += [f"### {q}", '', a, '']
    return '\n'.join(linies) + (PEU_ES if es else PEU_CA)


def md_blog_index(es=False):
    linies = [('# blog · consejos de danza y vida de escuela' if es
               else '# blog · consells de dansa i vida d’escola'), '']
    for p in sorted(bp.POSTS, key=lambda x: x['data'], reverse=True):
        slug = f"es/blog/{p['slug_es']}" if es else f"blog/{p['slug']}"
        suf = '_es' if es else ''
        linies.append(f"- [{p['h1' + suf]}](https://escoladansa.com/{slug}/) — {p['excerpt' + suf]}")
    return '\n'.join(linies) + '\n' + (PEU_ES if es else PEU_CA)


def main():
    n = 0
    # pàgines generades CA + ES
    for p in gp.PAGINES:
        if p['slug'] == 'horaris':
            ca, es = md_horaris(False), md_horaris(True)
        elif p['slug'] == 'preus':
            ca, es = md_preus(False), md_preus(True)
        else:
            ca, es = md_pagina(p, False), md_pagina(p, True)
        escriu(os.path.join(p['slug'], 'index.md'), ca)
        escriu(os.path.join('es', gp.SLUG_ES[p['slug']], 'index.md'), es)
        n += 2
    # home CA + ES
    escriu('index.md', md_home(False))
    escriu(os.path.join('es', 'index.md'), md_home(True))
    n += 2
    # blog: portada + posts
    escriu(os.path.join('blog', 'index.md'), md_blog_index(False))
    escriu(os.path.join('es', 'blog', 'index.md'), md_blog_index(True))
    n += 2
    for p in bp.POSTS:
        escriu(os.path.join('blog', p['slug'], 'index.md'), md_post(p, False))
        escriu(os.path.join('es', 'blog', p['slug_es'], 'index.md'), md_post(p, True))
        n += 2
    print(f'{n} fitxers index.md generats')


if __name__ == '__main__':
    main()
