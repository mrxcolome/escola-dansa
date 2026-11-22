# -*- coding: utf-8 -*-
"""
Tauler visual de visibilitat: /seo/ (intern, noindex).
Llegeix seo/dades.json i els posts de blog_posts.py, i escriu seo/index.html.
El diari detallat de feina (fet a mà) és a seo/diari/index.html.
Executa:  python genera_seo.py

A cada revisió: s'afegeix la mesura nova a dades.json (google, posicions, zones, ia, fitxa,
blog_transit), s'actualitzen «valoracio» (què fem bé / què cal millorar) i «toca_ara», i es regenera.
"""
import collections
import datetime
import html
import io
import json
import os
import sys

ARREL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ARREL, "generador"))
from blog_posts import POSTS  # noqa: E402

DADES = os.path.join(ARREL, "seo", "dades.json")
SORTIDA = os.path.join(ARREL, "seo", "index.html")
MESOS = ["gen", "febr", "març", "abr", "maig", "juny", "jul", "ag", "set", "oct", "nov", "des"]


def esc(t):
    return html.escape(str(t), quote=True)


def dia(d):
    a, m, dd = d.split("-")
    return f"{int(dd)} {MESOS[int(m) - 1]}"


def num(v, dec=1):
    if isinstance(v, int) or dec == 0:
        return f"{round(v):,}".replace(",", ".")
    return f"{v:.{dec}f}".replace(".", ",")


def gran(v):
    return f"{v / 1000:.1f}".replace(".", ",") + " mil" if v >= 10000 else num(v, 0)


# ── gràfic amb dates ───────────────────────────────────────────────────────

def grafic(valors, fmt=lambda v: num(v, 0), invers=False, w=320):
    """línia amb el valor a sobre de cada punt i la data a sota. invers: el valor petit és el bo (va a dalt)."""
    if not valors:
        return ""
    h, pl, pr, pt, pb = (118 if w > 260 else 112), 20, 20, 22, 26
    ts = [datetime.date.fromisoformat(d).toordinal() for d, _ in valors]
    vs = [v for _, v in valors]
    t0, t1 = min(ts), max(ts) if max(ts) > min(ts) else min(ts) + 1
    lo, hi = min(vs), max(vs)
    if hi == lo:
        hi = lo + 1

    def xy(t, v):
        x = pl + (w - pl - pr) * (t - t0) / (t1 - t0)
        f = (v - lo) / (hi - lo)
        y = pt + (h - pt - pb) * (f if invers else 1 - f)
        return x, y
    pts = [xy(t, v) for t, v in zip(ts, vs)]
    s = [f'<line x1="{pl}" y1="{h - pb + 6}" x2="{w - pr}" y2="{h - pb + 6}" class="eix"/>']
    if len(pts) > 1:
        s.append('<polyline points="' + " ".join(f"{x:.1f},{y:.1f}" for x, y in pts) + '" class="ln"/>')
    darrer_x = -99
    for i, ((x, y), (d, v)) in enumerate(zip(pts, valors)):
        ultim = i == len(pts) - 1
        s.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{4 if ultim else 3}" class="{"pt" if ultim else "dt"}"/>')
        if ultim or i == 0 or x - darrer_x > 36:
            if not ultim and (w - pr) - x < 34:
                continue
            s.append(f'<text x="{x:.1f}" y="{y - 8:.1f}" class="vl">{esc(fmt(v))}</text>')
            s.append(f'<text x="{x:.1f}" y="{h - 6}" class="dtx">{dia(d)}</text>')
            darrer_x = x
    return f'<svg class="graf" viewBox="0 0 {w} {h}" role="img" aria-label="evolució">{"".join(s)}</svg>'


def delta(ara, abans, invers=False, dec=0, unitat=""):
    if abans is None or ara is None:
        return ""
    d = ara - abans
    if abs(d) < (0.05 if dec else 0.5):
        return '<span class="dl igual">= igual</span>'
    bo = (d < 0) if invers else (d > 0)
    sig = "▲" if d > 0 else "▼"
    if not dec and abans:
        txt = f"{'+' if d > 0 else '−'}{abs(d) / abans * 100:.0f} %"
    else:
        txt = f"{'+' if d > 0 else '−'}{num(abs(d), dec)}{unitat}"
    return f'<span class="dl {"bo" if bo else "dolent"}">{sig} {txt}</span>'


def valoracio(v):
    be = "".join(f"<li>{esc(x)}</li>" for x in v.get("be", []))
    mi = "".join(f"<li>{esc(x)}</li>" for x in v.get("millorar", []))
    return (f'<div class="val"><div class="be"><div class="vt">✓ què fem bé</div><ul>{be}</ul></div>'
            f'<div class="mi"><div class="vt">→ què cal millorar</div><ul>{mi}</ul></div></div>')


# ── seccions ───────────────────────────────────────────────────────────────

def kpis(g):
    def serie(k):
        return [(m["data"], m[k]) for m in g if k in m]
    out = []
    for k, nom, inv, fmt, dec, expl in [
        ("clics", "visites des de Google", False, lambda v: num(v, 0), 0, "clics en els últims 28 dies"),
        ("impressions", "cops que sortim a Google", False, gran, 0, "impressions en els últims 28 dies"),
        ("posicio", "posició mitjana", True, lambda v: num(v, 1), 1, "de totes les cerques: com més baixa, millor"),
        ("indexades", "pàgines que Google té", False, lambda v: num(v, 0), 0, "pàgines indexades"),
    ]:
        s = serie(k)
        ara, ant = s[-1], (s[-2] if len(s) > 1 else None)
        dl = delta(ara[1], ant[1] if ant else None, invers=inv, dec=dec if k == "posicio" else 0)
        out.append(f'<div class="kpi"><div class="k-nom">{nom}</div><div class="k-val">{fmt(ara[1])}</div>'
                   f'<div class="k-sub">{dl}<span>respecte del {dia(ant[0]) if ant else "–"}</span></div>'
                   f'<div class="k-expl">{expl}</div>{grafic(s, fmt=fmt, invers=inv, w=210)}</div>')
    return '<div class="kpis">' + "".join(out) + "</div>"


def cel(v, nom):
    """cel·la de les zones: número = posició, 0 = no hi sortim, None = no hi ha aquesta zona"""
    if v is None:
        return f'<td class="z na" data-l="{nom}"><span>no n\'hi ha</span></td>'
    if v == 0:
        return f'<td class="z no" data-l="{nom}"><b>✗</b><span>no sortim</span></td>'
    return f'<td class="z si" data-l="{nom}"><b>{v}r</b><span>{"ens cita" if nom == "IA de Google" else "sortim"}</span></td>'


def zones(d):
    z = d["zones"]
    files = []
    for c in z["cerques"]:
        nota = f'<small class="znota">{esc(c["nota"])}</small>' if c.get("nota") else ""
        altres = f'<small>davant nostre: {esc(c["altres"])}</small>' if c.get("altres") else ""
        files.append(f'<tr><th>{esc(c["q"])}{altres}{nota}</th>{cel(c["mapa"], "mapa")}{cel(c["ia"], "IA de Google")}{cel(c["org"], "resultats")}</tr>')
    n = len(z["cerques"])
    nmap = sum(1 for c in z["cerques"] if c["mapa"])
    nia = sum(1 for c in z["cerques"] if c["ia"])
    norg = sum(1 for c in z["cerques"] if c["org"])
    return f"""
<div class="zones-intro">
<div class="zi"><b>1 · mapa</b><span>els 3 negocis que Google ensenya amb el mapa. Depèn molt de <em>des d'on</em> es busca: a prop de l'escola sortim; lluny, no.</span><strong>sortim en {nmap} de {n}</strong></div>
<div class="zi"><b>2 · IA de Google</b><span>el resum fet amb IA (Gemini) que surt a dalt de tot en moltes cerques, amb les webs que cita.</span><strong>ens cita en {nia} de {n}</strong></div>
<div class="zi"><b>3 · resultats normals</b><span>la llista de webs de la 1a pàgina (sense comptar els anuncis).</span><strong>sortim en {norg} de {n}</strong></div>
</div>
<table class="zt"><thead><tr><th>cerca</th><th>mapa</th><th>IA de Google</th><th>resultats</th></tr></thead><tbody>{"".join(files)}</tbody></table>
<p class="nota">Revisat el {dia(z["data"])} des de {esc(z["on"])}. «No n'hi ha»: per a aquesta cerca Google no ensenya aquesta zona. Cada persona ho pot veure una mica diferent segons on és i què ha buscat abans.</p>"""


def posicions(d):
    dates = sorted(d["posicions"])

    def pos(v):
        return v[0] if isinstance(v, list) else v

    def serie(c):
        return [(dt, pos(d["posicions"][dt][c])) for dt in dates if c in d["posicions"][dt]]

    def volum(c):
        for dt in reversed(dates):
            v = d["posicions"][dt].get(c)
            if isinstance(v, list):
                return v[1], v[2]
        return None

    def nivell(p):
        if p is None:
            return "cap", "sense dades"
        if p <= 3.5:
            return "top", "top 3"
        if p <= 10.5:
            return "pag1", "1a pàgina"
        if p <= 20.5:
            return "pag2", "2a pàgina"
        return "lluny", "3a pàgina o més"
    totes = [c for g in d["grups"] for c in g["cerques"]]
    amb = [c for c in totes if serie(c)]
    p1 = [c for c in amb if serie(c)[-1][1] <= 10.5]
    compta = collections.Counter(nivell(serie(c)[-1][1] if serie(c) else None)[0] for c in totes)
    barra = "".join(f'<span class="seg {k}" style="flex:{compta[k]}"></span>' for k in ("top", "pag1", "pag2", "lluny", "cap") if compta[k])
    vols = d.get("volums", {})
    grups = []
    for g in d["grups"]:
        files = []
        for c in g["cerques"]:
            s = serie(c)
            p = s[-1][1] if s else None
            cls, txt = nivell(p)
            hist = "".join(f'<span class="hp">{dia(dt)} <b>{num(v)}</b></span>' for dt, v in s[:-1][-3:])
            fl = ""
            if len(s) > 1:
                dif = s[-2][1] - s[-1][1]
                fl = ('<span class="fl igual">=</span>' if abs(dif) < 0.5 else
                      f'<span class="fl puja">▲ puja {num(dif)}</span>' if dif > 0 else f'<span class="fl baixa">▼ baixa {num(-dif)}</span>')
            vol = volum(c)
            vist = (f'{num(vol[0], 0)} cops vista' + (f' · {vol[1]} clic' + ('s' if vol[1] > 1 else '') if vol[1] else "")) if vol else ""
            vm = vols.get(c)
            files.append(
                f'<tr class="{cls}"><td class="pos">{num(p) if p is not None else "–"}</td>'
                f'<td class="cerca"><strong>{esc(c)}</strong><span class="niv">{txt}</span></td>'
                f'<td class="vol">{("<span class=pend>molt poques</span>" if vm == "—" else esc(vm)) if vm else "<span class=pend>–</span>"}</td>'
                f'<td class="vist">{vist}</td>'
                f'<td class="hist">{hist}{fl}</td></tr>')
        grups.append(f'<tr class="gr"><td colspan="5">{esc(g["nom"])}</td></tr>' + "".join(files))
    return f"""
<div class="resum3">
<div class="r pag1"><b>{len(p1)}<small> / {len(totes)}</small></b><span>cerques a la 1a pàgina (posició 1-10)</span></div>
<div class="r"><b>{compta["pag2"]}</b><span>a la 2a pàgina (11-20): les més fàcils de pujar</span></div>
<div class="r lluny"><b>{compta["lluny"]}</b><span>a la 3a pàgina o més avall</span></div>
</div>
<div class="barra">{barra}</div>
<div class="llegenda"><span><i class="top"></i>top 3</span><span><i class="pag1"></i>1a pàgina</span><span><i class="pag2"></i>2a pàgina</span><span><i class="lluny"></i>més avall</span></div>
<details class="plega" open><summary>veure les {len(totes)} cerques, amb les posicions anteriors</summary>
<div class="taula-scroll"><table class="pt"><thead><tr><th>posició</th><th>cerca</th><th>cerques/mes a Barcelona</th><th>a Google (28 dies)</th><th>abans</th></tr></thead><tbody>{"".join(grups)}</tbody></table></div>
</details>
<p class="nota"><strong>Per què aquestes cerques:</strong> de les {d.get("total_consultes", 485)} cerques per les quals Google ens ha ensenyat en els últims 28 dies, són les que faria una família o un alumne que busca escola o classes (s'han tret les del nom de l'escola i les que no hi tenen a veure). «Cops vista»: quantes vegades hem sortit en aquesta cerca. La posició és la mitjana de Search Console; a «abans» hi ha les posicions anteriors amb la data del dia que es van mirar. <strong>Cerques/mes a Barcelona</strong>: quanta gent de Barcelona ciutat la busca cada mes (Planificador de paraules clau de Google Ads, {dia(d["volums_info"]["data"])}). Google només dona franges («10 - 100») si no hi ha cap anunci actiu.</p>
{oportunitats(d)}"""


def oportunitats(d):
    o = d.get("oportunitats")
    if not o:
        return ""
    def estat(p):
        if p is None:
            return '<span class="op-no">no hi sortim</span>'
        if p <= 10.5:
            return f'<span class="op-si">posició {num(p)} ✓</span>'
        return f'<span class="op-no">posició {num(p)}</span>'
    files = "".join(f'<tr><td><strong>{esc(x["q"])}</strong>' + (f'<small>{esc(x["nota"])}</small>' if x.get("nota") else "") +
                    f'</td><td class="vol">{esc(x["vol"])}</td><td>{estat(x["pos"])}</td></tr>' for x in o["barcelona"])
    esp = "".join(f'<span class="chip">{esc(q)} <b>{esc(v)}</b></span>' for q, v in o["espanya"])
    return f"""
<h3>les cerques amb més gent (100 a 1.000 al mes a Barcelona)</h3>
<table class="pt op"><thead><tr><th>cerca</th><th>cerques/mes</th><th>on sortim</th></tr></thead><tbody>{files}</tbody></table>
<p class="nota">A tota Espanya, les cerques generals més fetes són aquestes (cerques/mes). Les «cerca de mi» («a prop meu») es resolen amb el mapa: per sortir-hi, la clau és la fitxa de Google.</p>
<div class="chips">{esp}</div>"""


def ia(d):
    i = d["ia"]
    cit = i["citacions_bing"]
    pags = i["pagines_citades"]
    mx = max(v for _, v in pags)
    barres = "".join(f'<div class="hb"><span class="hb-nom">{esc(n)}</span><span class="hb-bar"><i style="width:{v / mx * 100:.0f}%"></i></span><b>{v}</b></div>' for n, v in pags)
    fets = "".join(
        f'<li class="{"si" if f[1] else "no"}"><span class="ic">{"✓" if f[1] else "✗"}</span>{esc(f[0])}'
        + (f'<small>{esc(f[2])}</small>' if not f[1] and len(f) > 2 and f[2] else "") + "</li>"
        for f in i["que_diu"]["fets"])
    bons = sum(1 for f in i["que_diu"]["fets"] if f[1])
    return f"""
<div class="dues">
<div class="carta"><div class="k-nom">cops que Copilot (la IA de Bing) ens cita</div>
<div class="k-val">{cit[-1][1]}</div><div class="k-sub">{delta(cit[-1][1], cit[-2][1])}<span>respecte del {dia(cit[-2][0])}</span></div>
<div class="k-expl">acumulat dels últims 3 mesos (Bing Webmaster Tools)</div>
{grafic(cit)}
<div class="k-nom" style="margin-top:14px">pàgines que més cita</div>{barres}</div>
<div class="carta"><div class="k-nom">prova: què diu la IA de l'escola ({dia(i["que_diu"]["data"])})</div>
<div class="k-val">{bons}<small> de {len(i["que_diu"]["fets"])} bé</small></div>
<div class="k-expl">Fem preguntes a ChatGPT, Perplexity i Google com les faria una família («escola de dansa a Sant Gervasi», «quin horari fan», «quins estils fan») i comprovem si la resposta és correcta. <b class="vd">✓</b> = respon bé. <b class="vm">✗</b> = respon malament o no ens nomena; a sota hi ha d'on treu l'error.</div>
<ul class="fets">{fets}</ul></div>
</div>"""


def fitxa(d):
    f = d["fitxa"]
    r = f["ressenyes"]
    estrelles = "★" * round(r[-1][2]) + "☆" * (5 - round(r[-1][2]))
    it = f["interaccions"]
    z = d["zones"]["cerques"]
    nmap = [c["q"] for c in z if c["mapa"]]
    return f"""
<div class="tres">
<div class="carta"><div class="k-nom">ressenyes a Google</div>
<div class="k-val">{num(r[-1][2])} <span class="estr">{estrelles}</span></div>
<div class="k-sub">{delta(r[-1][1], r[-2][1])}<span>{r[-1][1]} opinions · respecte del {dia(r[-2][0])}</span></div>
<div class="k-expl">nombre d'opinions</div>{grafic([(a, b) for a, b, _ in r])}</div>
<div class="carta"><div class="k-nom">sortim al mapa?</div>
<div class="k-val">{len(nmap)}<small> de {len(z)} cerques</small></div>
<div class="k-expl">De les cerques clau de l'apartat 2, només sortim entre els 3 del mapa en: <b>{esc(", ".join(nmap)) or "cap"}</b>. A les altres, el mapa ensenya escoles més a prop de qui busca o amb més ressenyes recents.</div></div>
<div class="carta"><div class="k-nom">què fa la gent a la fitxa ({it["periode"]})</div>
<div class="accions"><div><b>{it["vistes"]}</b><span>la veuen</span></div><div><b>{it["web"]}</b><span>van a la web</span></div><div><b>{it["com_arribar"]}</b><span>com arribar</span></div><div><b>{it["trucades"]}</b><span>truquen</span></div></div>
<div class="k-expl">{f["posts_publicats"]} posts del blog publicats sols a la fitxa.</div></div>
</div>"""


def blog(d):
    b = d["blog_transit"]
    per_slug = {}
    for p in POSTS:
        per_slug[f"/blog/{p['slug']}/"] = p
        per_slug[f"/es/blog/{p['slug_es']}/"] = p
    agg = {}
    for url, cl, im, ps in b["pagines"]:
        p = per_slug.get(url)
        if not p:
            continue
        a = agg.setdefault(p["slug"], {"t": p["h1"], "cl": 0, "im": 0, "data": p["data"]})
        a["cl"] += cl
        a["im"] += im
    llista = sorted(agg.values(), key=lambda a: (-a["cl"], -a["im"]))
    tot_cl = sum(a["cl"] for a in llista)
    mx = max(a["cl"] for a in llista) or 1
    top = "".join(
        f'<div class="hb gran"><span class="hb-nom">{esc(a["t"])}<small>{num(a["im"], 0)} cops vist · publicat el {dia(a["data"])}</small></span>'
        f'<span class="hb-bar"><i style="width:{a["cl"] / mx * 100:.0f}%"></i></span><b>{a["cl"]}</b></div>' for a in llista[:10])
    sense = [a for a in llista if a["cl"] == 0]
    return f"""
<div class="dues">
<div class="carta"><div class="k-nom">visites des de Google per article (català + castellà)</div>
<div class="k-val">{tot_cl}<small> visites en {b["dies"]} dies</small></div>
<div class="k-expl">Els 10 articles que porten més gent des de Google (Search Console, fins al {dia(b["data"])}). El número de la dreta són visites (clics).</div>
{top}
<div class="k-expl" style="margin-top:10px">{len(sense)} articles surten a Google però encara no hi ha clicat ningú.</div></div>
<div class="carta"><div class="k-nom">i d'aquestes visites, quantes acaben en alumne?</div>
<div class="k-val">aviat ho sabrem</div>
<div class="k-expl">Des del 23 de novembre la web compta cada clic al WhatsApp, al telèfon, al correu i al formulari, i per quina pàgina havia entrat la persona.</div>
<ul class="passos"><li><b>✓</b>Comptar els clics a WhatsApp, telèfon, correu i formulari (fet).</li><li><b>✓</b>El correu del formulari diu per quina pàgina va entrar la persona (fet).</li><li><b>3</b>Quan hi hagi dades: aquí, per a cada article, visites → contactes.</li></ul>
<div class="k-expl">A Analytics només compten els que accepten les galetes; el correu del formulari ho diu sempre.</div></div>
</div>"""


def salut(d):
    t = d["tecnic"]
    ix = d["indexacio"]
    oks = sum(1 for _, ok in t["checks"] if ok)
    chips = "".join(f'<span class="chip {"ok" if ok else "ko"}">{"✓" if ok else "✗"} {esc(n)}</span>' for n, ok in t["checks"])
    total = ix["indexades"] + sum(v for _, v in ix["motius"])
    segs = f'<span class="seg top" style="flex:{ix["indexades"]}"></span>' + "".join(
        f'<span class="seg cap" style="flex:{v}"></span>' for _, v in ix["motius"])
    motius = "".join(f"<li><b>{v}</b> {esc(n)}</li>" for n, v in ix["motius"])
    return f"""
<div class="dues">
<div class="carta"><div class="k-nom">revisió tècnica ({dia(t["data"])})</div><div class="k-val bo">{oks}<small> de {len(t["checks"])} bé</small></div>
<div class="chips">{chips}</div></div>
<div class="carta"><div class="k-nom">pàgines a Google ({dia(ix["data"])})</div>
<div class="k-val">{ix["indexades"]}<small> de {total} que coneix</small></div>
<div class="barra">{segs}</div><ul class="motius"><li class="si"><b>{ix["indexades"]}</b> indexades (surten a Google)</li>{motius}</ul></div>
</div>"""


CSS = """
:root{--fons:#f6f2ea;--paper:#fffdf8;--tinta:#221a15;--gris:#75675c;--vora:#e5dcce;--granat:#950000;
--top:#2e7d4f;--pag1:#c99a06;--pag2:#d9772b;--lluny:#c0392b;--cap:#d8d0c4}
*{box-sizing:border-box}
body{margin:0;background:var(--fons);color:var(--tinta);font-family:'Montserrat',system-ui,sans-serif;font-size:15px;line-height:1.5}
main{max-width:1000px;margin:0 auto;padding:34px 16px 70px}
.eti{font-size:.68rem;letter-spacing:.22em;text-transform:uppercase;color:var(--granat);font-weight:600}
h1{font-size:2.1rem;font-weight:800;letter-spacing:-.02em;margin:4px 0 0}h1 em{font-style:normal;color:var(--granat)}
.sub{color:var(--gris);margin:6px 0 0;font-size:.9rem}
h2{font-size:1.2rem;font-weight:800;margin:46px 0 4px;display:flex;align-items:baseline;gap:10px}
h2 .n{font-size:.7rem;color:#fff;background:var(--granat);border-radius:100px;padding:2px 9px}
.intro{color:var(--gris);font-size:.86rem;margin:0 0 14px;max-width:760px}
.toca{background:var(--tinta);color:#fff;border-radius:16px;padding:18px 20px;margin-top:22px}
.toca .k-nom{color:#f0b9b9}
.toca ol{margin:8px 0 0;padding:0;list-style:none;counter-reset:t}
.toca li{counter-increment:t;display:flex;gap:12px;align-items:flex-start;padding:8px 0;border-top:1px solid #ffffff22}
.toca li:first-child{border-top:none}.toca li::before{content:counter(t);font-weight:800;color:#f0b9b9;min-width:14px}
.qui{font-size:.66rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;border-radius:100px;padding:2px 8px;white-space:nowrap;margin-top:2px}
.qui.Xavi{background:#f0b9b9;color:var(--tinta)}.qui.Claude{background:#ffffff26;color:#fff}
.kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.kpi,.carta{background:var(--paper);border:1px solid var(--vora);border-radius:16px;padding:14px 16px;min-width:0}
.k-nom{font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--granat);font-weight:600}
.k-val{font-size:2.1rem;font-weight:800;line-height:1.15;font-variant-numeric:tabular-nums}
.k-val small{font-size:.9rem;color:var(--gris);font-weight:600;margin-left:4px}
.k-val.bo{color:var(--top)}.k-val.dolent{color:var(--lluny);font-size:1.6rem}
.k-sub{font-size:.74rem;color:var(--gris);display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-top:2px}
.k-expl{font-size:.76rem;color:var(--gris);margin-top:6px}
.vd{color:var(--top)}.vm{color:var(--lluny)}
.dl{font-weight:800;border-radius:100px;padding:1px 7px;font-size:.72rem}
.dl.bo{background:#2e7d4f1f;color:var(--top)}.dl.dolent{background:#c0392b1a;color:var(--lluny)}.dl.igual{background:#0000000d;color:var(--gris)}
.graf{width:100%;height:auto;margin-top:6px;display:block;overflow:visible}
.graf .ln{fill:none;stroke:var(--granat);stroke-width:2;stroke-linejoin:round}
.graf .dt{fill:var(--granat);opacity:.55}.graf .pt{fill:var(--granat)}
.graf .eix{stroke:var(--vora);stroke-width:1}
.graf .vl{font:700 10px Montserrat,sans-serif;fill:var(--tinta);text-anchor:middle}
.graf .dtx{font:500 9px Montserrat,sans-serif;fill:var(--gris);text-anchor:middle}
.dues{display:grid;grid-template-columns:1fr 1fr;gap:10px}.tres{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.val{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
.val>div{border-radius:14px;padding:12px 16px;font-size:.84rem}
.val .be{background:#2e7d4f12;border:1px solid #2e7d4f33}.val .mi{background:#95000010;border:1px solid #95000030}
.vt{font-weight:800;font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;margin-bottom:4px}
.be .vt{color:var(--top)}.mi .vt{color:var(--granat)}
.val ul{margin:0;padding-left:18px}.val li{margin:4px 0}
.zones-intro{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-bottom:10px}
.zi{background:var(--paper);border:1px solid var(--vora);border-radius:14px;padding:12px 14px;display:flex;flex-direction:column;gap:4px}
.zi b{font-size:.9rem}.zi span{font-size:.74rem;color:var(--gris)}.zi strong{font-size:1.05rem;font-weight:800;margin-top:auto;color:var(--granat)}
table{width:100%;border-collapse:separate;border-spacing:0;background:var(--paper);border:1px solid var(--vora);border-radius:14px;overflow:hidden}
.zt th,.zt td{padding:9px 12px;border-top:1px solid var(--vora);text-align:left;vertical-align:middle}
.zt thead th{border-top:none;font-size:.66rem;letter-spacing:.12em;text-transform:uppercase;color:var(--gris)}
.zt tbody th{font-weight:600;font-size:.88rem}.zt th small{display:block;font-weight:400;color:var(--gris);font-size:.72rem}
.zt .znota{color:var(--granat)!important}
.z{text-align:center!important;width:16%}.z b{display:block;font-size:1.15rem;font-weight:800}.z span{font-size:.68rem;color:var(--gris)}
.z.si b{color:var(--top)}.z.no b{color:var(--lluny)}.z.na span{color:#b9ad9e}
.resum3{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.r{background:var(--paper);border:1px solid var(--vora);border-radius:16px;padding:12px 16px}
.r b{display:block;font-size:2rem;font-weight:800;line-height:1.1}.r b small{font-size:1rem;color:var(--gris)}.r span{font-size:.76rem;color:var(--gris)}
.r.pag1 b{color:var(--pag1)}.r.lluny b{color:var(--lluny)}
.barra{display:flex;height:12px;border-radius:100px;overflow:hidden;margin:12px 0 8px;gap:2px}
.seg.top{background:var(--top)}.seg.pag1{background:var(--pag1)}.seg.pag2{background:var(--pag2)}.seg.lluny{background:var(--lluny)}.seg.cap{background:var(--cap)}
.llegenda{display:flex;flex-wrap:wrap;gap:14px;font-size:.74rem;color:var(--gris)}
.llegenda i{display:inline-block;width:10px;height:10px;border-radius:3px;margin-right:5px;vertical-align:-1px}
.llegenda i.top{background:var(--top)}.llegenda i.pag1{background:var(--pag1)}.llegenda i.pag2{background:var(--pag2)}.llegenda i.lluny{background:var(--lluny)}
.plega summary{cursor:pointer;font-weight:700;font-size:.86rem;color:var(--granat);margin:14px 0 8px}
.taula-scroll{overflow-x:auto}
.pt td,.pt th{padding:7px 10px;border-top:1px solid var(--vora);font-size:.82rem;text-align:left;vertical-align:middle}
.pt thead th{border-top:none;font-size:.64rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gris)}
.pt tr.gr td{background:#f1ebe0;font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;font-weight:800;color:var(--gris)}
.pt tr.top{--c:var(--top)}.pt tr.pag1{--c:var(--pag1)}.pt tr.pag2{--c:var(--pag2)}.pt tr.lluny{--c:var(--lluny)}.pt tr.cap{--c:var(--cap)}
.pt .pos{font-size:1.15rem;font-weight:800;text-align:center;width:64px;border-left:5px solid var(--c);color:var(--c)}
.cerca strong{display:block;font-weight:600}.niv{font-size:.64rem;font-weight:800;color:var(--c);text-transform:uppercase;letter-spacing:.08em}
.vol,.vist{color:var(--gris);white-space:nowrap}.pend{font-size:.7rem;color:#b9ad9e}
.op td{padding:9px 12px}.op small{display:block;color:var(--gris);font-size:.7rem}.op-si{color:var(--top);font-weight:800}.op-no{color:var(--lluny);font-weight:800}.chip b{color:var(--granat)}
.hist{white-space:nowrap}.hp{display:inline-block;font-size:.7rem;color:var(--gris);background:#0000000a;border-radius:6px;padding:1px 6px;margin-right:4px}
.hp b{color:var(--tinta)}.fl{font-weight:800;font-size:.74rem;margin-left:4px}.puja{color:var(--top)}.baixa{color:var(--lluny)}.igual{color:var(--gris)}
.hb{display:grid;grid-template-columns:1fr 90px 30px;gap:8px;align-items:center;font-size:.78rem;margin:6px 0}
.hb.gran{grid-template-columns:1fr 70px 26px}.hb-nom small{display:block;color:var(--gris);font-size:.68rem}
.hb-bar{background:#0000000a;border-radius:100px;height:8px;overflow:hidden}.hb-bar i{display:block;height:100%;background:var(--granat);border-radius:100px}
.hb b{text-align:right}
.fets{list-style:none;padding:0;margin:10px 0 0}
.fets li{display:flex;flex-wrap:wrap;gap:4px 8px;align-items:baseline;padding:6px 0;border-top:1px solid var(--vora);font-size:.84rem}
.fets li small{flex-basis:100%;padding-left:26px;color:var(--gris);font-size:.74rem}
.ic{display:inline-grid;place-items:center;width:18px;height:18px;border-radius:50%;font-size:.7rem;font-weight:800;color:#fff}
.si .ic{background:var(--top)}.no .ic{background:var(--lluny)}
.estr{font-size:1.1rem;color:var(--pag1);letter-spacing:1px}
.accions{display:grid;grid-template-columns:repeat(4,1fr);gap:6px;margin:8px 0}
.accions div{text-align:center}.accions b{display:block;font-size:1.4rem;font-weight:800}.accions span{font-size:.68rem;color:var(--gris)}
.passos{list-style:none;padding:0;margin:10px 0}.passos li{display:flex;gap:10px;font-size:.82rem;padding:4px 0}
.passos b{display:inline-grid;place-items:center;min-width:22px;height:22px;border-radius:50%;background:var(--granat);color:#fff;font-size:.72rem}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.chip{font-size:.72rem;font-weight:600;border:1px solid var(--vora);border-radius:100px;padding:4px 10px;background:#fff}
.chip.ok{color:var(--top)}.chip.ko{color:var(--lluny);border-color:var(--lluny)}
.motius{list-style:none;padding:0;margin:6px 0 0;font-size:.78rem;color:var(--gris)}
.motius li{padding:3px 0}.motius b{color:var(--tinta);display:inline-block;min-width:30px}.motius li.si b{color:var(--top)}
.nota{color:var(--gris);font-size:.74rem;margin-top:10px}
.peu{margin-top:44px;padding-top:16px;border-top:1px solid var(--vora);font-size:.82rem;color:var(--gris)}
a{color:var(--granat)}
@media(max-width:860px){.kpis{grid-template-columns:1fr 1fr}.tres,.dues,.val,.zones-intro{grid-template-columns:1fr}}
@media(max-width:600px){.kpis{grid-template-columns:1fr}.resum3{gap:6px}.r{padding:10px}.r b{font-size:1.6rem}h1{font-size:1.7rem}
.zt thead{display:none}.zt tr{display:grid;grid-template-columns:1fr 1fr 1fr}.zt tbody th{grid-column:1/-1}.zt td{border-top:none;width:auto}
.zt td::before{content:attr(data-l);display:block;font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--gris)}}
"""


def main():
    d = json.load(io.open(DADES, encoding="utf-8"))
    v = d["valoracio"]
    toca = "".join(f'<li><span class="qui {esc(t["qui"])}">{esc(t["qui"])}</span><span>{esc(t["que"])}</span></li>' for t in d["toca_ara"])
    pagina = f"""<!doctype html>
<html lang="ca"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Visibilitat escoladansa.com</title>
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800&display=swap">
<style>{CSS}</style></head><body><main>
<span class="eti">tauler de visibilitat · Google, IA i fitxa</span>
<h1>com ens troben<em>.</em></h1>
<p class="sub">Actualitzat el {dia(d["actualitzat"])} {d["actualitzat"][:4]}. Cada fletxa compara amb la mesura anterior, i cada gràfica porta la data de cada mesura.</p>

<div class="toca"><div class="k-nom">què toca ara</div><ol>{toca}</ol></div>

<h2><span class="n">1</span>Google en xifres</h2>
<p class="intro">Dades de Search Console: quants cops sortim a Google, quanta gent hi clica i a quina posició sortim de mitjana.</p>
{kpis(d["google"])}
{valoracio(v["google"])}

<h2><span class="n">2</span>què veu qui ens busca: mapa, IA i resultats</h2>
<p class="intro">Quan algú busca «escola de dansa» o «extraescolar», Google ensenya tres zones. Per a les cerques més importants, mirem si sortim a cadascuna i en quina posició.</p>
{zones(d)}
{valoracio(v["zones"])}

<h2><span class="n">3</span>a quina posició sortim per a cada cerca</h2>
<p class="intro">Les cerques que fan les famílies i els alumnes, ordenades per tema. L'objectiu és que totes siguin a la 1a pàgina (posició 1 a 10).</p>
{posicions(d)}
{valoracio(v["cerques"])}

<h2><span class="n">4</span>la IA ens coneix?</h2>
<p class="intro">ChatGPT, Copilot, Perplexity i el resum amb IA de Google responen amb el que llegeixen de la nostra web i de fitxes d'altres webs (directoris, l'Ajuntament…).</p>
{ia(d)}
{valoracio(v["ia"])}

<h2><span class="n">5</span>fitxa de Google i ressenyes</h2>
<p class="intro">La fitxa és el que surt al mapa: nota, opinions, fotos, horari i botons per trucar o arribar.</p>
{fitxa(d)}
{valoracio(v["fitxa"])}

<h2><span class="n">6</span>blog: quina gent porta cada article</h2>
<p class="intro">El que importa no és quants articles fem, sinó quanta gent porten i si aquesta gent acaba contactant.</p>
{blog(d)}
{valoracio(v["blog"])}

<h2><span class="n">7</span>salut tècnica</h2>
<p class="intro">Si tot és verd, Google i la IA poden llegir bé la web.</p>
{salut(d)}
{valoracio(v["tecnic"])}

<p class="peu">El diari detallat de la feina feta, revisió a revisió: <a href="/seo/diari/">/seo/diari/</a>. Les dades d'aquest tauler són a <code>seo/dades.json</code>.</p>
</main></body></html>
"""
    io.open(SORTIDA, "w", encoding="utf-8", newline="\n").write(pagina)
    print("seo/index.html generat")


if __name__ == "__main__":
    main()
