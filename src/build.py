#!/usr/bin/env python3
"""Static site generator for Test First Water (working name). Plain Python, no dependencies.
Rebuild:  cd /workspace/water-site/src && python3 build.py   (writes ../docs, served by GitHub Pages)
Move hosts: set SITE_ORIGIN / BASE_PATH env vars. Remove the preview noindex: PREVIEW_NOINDEX=0."""
import json, os, shutil, html, datetime

SITE_ORIGIN = os.environ.get("SITE_ORIGIN", "https://betrnames.github.io")
BASE_PATH = os.environ.get("BASE_PATH", "/water-treatment-guide/")  # must start and end with /
PREVIEW_NOINDEX = os.environ.get("PREVIEW_NOINDEX", "1") == "1"      # keep ON until Gabe picks a domain
SITE_NAME = "Test First Water"
SITE_DESC = "Plain-English help for picking a whole-home water filter or softener: test your water first, skip the door-to-door pitch, then buy the right system."
CHECKED = "Nov 19, 2026"
TODAY = datetime.date.today().isoformat()
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")
CONTACT_EMAIL = "info@betrnames.com"

def url(path): return SITE_ORIGIN + BASE_PATH + path
def href(path): return BASE_PATH + path

def link(label, dest, program=None):
    """Outbound brand link. NO affiliate tags yet. data-affiliate marks where an approved tag goes later."""
    attr = f' data-affiliate="{program}"' if program else ""
    return f'<a href="{html.escape(dest)}"{attr} rel="nofollow noopener" target="_blank">{label}</a>'

def cite(label, dest):
    return f'<a href="{html.escape(dest)}" rel="noopener" target="_blank">{label}</a>'

DISCLOSURE = (f'<p class="disclosure"><strong>Heads up:</strong> we plan to join some brands\' affiliate programs. '
              f'If we do, we may earn a commission when you buy through a link here, at no extra cost to you. '
              f'It never changes what we recommend, including telling you not to buy. '
              f'<a href="{href("affiliate-disclosure/")}">How this works</a>.</p>')

NAV = [("", "Start here"), ("test-your-water/", "Test your water"), ("softener-vs-salt-free/", "Softener vs salt-free"),
       ("whole-house-water-filter/", "City water"), ("well-water/", "Well water"), ("softener-size-calculator/", "Calculator")]

CSS = """
:root{--b:#0f5c78;--d:#0b3d50;--a:#1f8a70;--bg:#f7fafb;--t:#1d2329;--m:#5b6670;--line:#dbe4e8}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--t);background:var(--bg)}
a{color:var(--b)}a:hover{color:var(--d)}
header{background:var(--d);color:#fff}header a{color:#fff;text-decoration:none}
.wrap{max-width:780px;margin:0 auto;padding:0 18px}
.top{display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:8px;padding:12px 18px}
.brand{font-weight:800;font-size:1.15rem;letter-spacing:.2px}.brand span{color:#8fd3e8}
nav.main{display:flex;flex-wrap:wrap;gap:4px 14px;font-size:.92rem}nav.main a{opacity:.92}nav.main a:hover{opacity:1;text-decoration:underline}
.preview{background:#fff4d6;color:#5a4300;font-size:.85rem;text-align:center;padding:6px 12px}
main{padding:22px 0 40px}h1{font-size:2rem;line-height:1.2;margin:.4rem 0 .6rem;color:var(--d)}
h2{margin-top:2.1rem;color:var(--d);font-size:1.4rem;line-height:1.3}h3{margin:1.4rem 0 .3rem;font-size:1.1rem}
.crumbs{font-size:.85rem;color:var(--m)}.crumbs a{color:var(--m)}.meta{color:var(--m);font-size:.88rem;margin-top:0}
.lede{font-size:1.1rem}
.card{background:#fff;border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin:14px 0}
.card h3{margin:.2rem 0 .3rem}.card p{margin:.3rem 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px}
.note{background:#e9f5f8;border-left:4px solid var(--b);padding:10px 14px;margin:16px 0;border-radius:0 8px 8px 0}
.warn{background:#fff3f0;border-left:4px solid #c2412d;padding:10px 14px;margin:16px 0;border-radius:0 8px 8px 0}
.disclosure{font-size:.9rem;background:#fff;border:1px dashed #b9c7cd;padding:8px 12px;border-radius:8px;color:#38434c}
.price{font-size:.85rem;color:var(--m)}
.table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:12px 0}
table{border-collapse:collapse;width:100%;background:#fff;font-size:.95rem;min-width:520px}
th,td{border:1px solid var(--line);padding:8px 10px;text-align:left;vertical-align:top}th{background:#eef4f6}
.btn{display:inline-block;background:var(--b);color:#fff!important;text-decoration:none;padding:10px 16px;border-radius:8px;font-weight:600}
.calc{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:16px 0}
.calc label{display:block;font-weight:600;margin-top:12px}.calc .hint{font-weight:400;color:var(--m);font-size:.85rem}
.calc input,.calc select{font-size:1rem;padding:9px 10px;border:1px solid #b9c7cd;border-radius:8px;width:100%;max-width:260px;background:#fff}
.row{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.result{margin-top:16px;background:#eef8f4;border:1px solid #b7dfcf;border-radius:10px;padding:12px 16px}
.result .big{font-size:1.6rem;font-weight:800;color:var(--a)}
.small{font-size:.85rem;color:var(--m)}ol li,ul li{margin:.25rem 0}
footer{background:var(--d);color:#d7e6ec;padding:22px 0;font-size:.9rem}footer a{color:#fff;margin-right:14px}
@media (max-width:600px){h1{font-size:1.6rem}body{font-size:16.5px}}
"""

def page(path, title, desc, h1, body, crumbs=None, schema=None, og_type="article", extra_head=""):
    canon = url(path)
    crumbs = crumbs or []
    ld = list(schema or [])
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": url("")}]
        for i, (p, n) in enumerate(crumbs, start=2):
            items.append({"@type": "ListItem", "position": i, "name": n, "item": url(p)})
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    crumb_html = ""
    if crumbs:
        parts = [f'<a href="{href("")}">Home</a>'] + [
            (f'<a href="{href(p)}">{html.escape(n)}</a>' if i < len(crumbs) - 1 else html.escape(n))
            for i, (p, n) in enumerate(crumbs)]
        crumb_html = '<nav class="crumbs" aria-label="Breadcrumb">' + " › ".join(parts) + "</nav>"
    ld_html = "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    nav = "".join(f'<a href="{href(p)}">{n}</a>' for p, n in NAV)
    robots = ('<meta name="robots" content="noindex,nofollow">' if PREVIEW_NOINDEX
              else '<meta name="robots" content="index,follow,max-image-preview:large">')
    banner = ('<div class="preview">Preview build. Not indexed yet, and no affiliate links are active.</div>'
              if PREVIEW_NOINDEX else "")
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
{robots}
<link rel="canonical" href="{canon}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{canon}">
<link rel="icon" href="{href('favicon.svg')}" type="image/svg+xml">
<style>{CSS}</style>
{ld_html}
{extra_head}
</head>
<body>
<header><div class="top"><a class="brand" href="{href('')}">Test First <span>Water</span></a>
<nav class="main" aria-label="Main">{nav}</nav></div>{banner}</header>
<main><div class="wrap">
{crumb_html}
<h1>{html.escape(h1)}</h1>
{body}
</div></main>
<footer><div class="wrap">
<p><strong>{SITE_NAME}</strong>: test first, then treat. We don't sell water systems and we don't do in-home visits.</p>
<p><a href="{href('about/')}">About</a><a href="{href('affiliate-disclosure/')}">Affiliate disclosure</a><a href="{href('privacy/')}">Privacy</a><a href="{href('door-to-door-water-sales/')}">Sales red flags</a><a href="{href('springwell-review/')}">SpringWell review</a></p>
<p class="small">General information, not medical, legal, or plumbing advice. Prices and policies change; we show the date we checked each one.</p>
</div></footer>
</body>
</html>'''

def article_schema(path, h1, desc):
    return {"@context": "https://schema.org", "@type": "Article", "headline": h1, "description": desc,
            "dateModified": TODAY, "mainEntityOfPage": url(path),
            "author": {"@type": "Organization", "name": SITE_NAME}, "publisher": {"@type": "Organization", "name": SITE_NAME}}

def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

def faq_html(faqs):
    return "<h2>Quick questions</h2>" + "".join(f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>" for q, a in faqs)

PAGES = []
def add(path, **kw): PAGES.append((path, kw))

from content import register  # noqa: E402
register(add=add, href=href, url=url, link=link, cite=cite, DISCLOSURE=DISCLOSURE, CHECKED=CHECKED,
         article_schema=article_schema, faq_schema=faq_schema, faq_html=faq_html, SITE_NAME=SITE_NAME, EMAIL=CONTACT_EMAIL)

def build():
    os.makedirs(OUT, exist_ok=True)
    for e in os.listdir(OUT):
        fp = os.path.join(OUT, e)
        shutil.rmtree(fp) if os.path.isdir(fp) else os.remove(fp)
    for path, kw in PAGES:
        target = os.path.join(OUT, path, "index.html")
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w") as f: f.write(page(path, **kw))
    with open(os.path.join(OUT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p, _ in PAGES: f.write(f"  <url><loc>{url(p)}</loc><lastmod>{TODAY}</lastmod></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(OUT, "robots.txt"), "w") as f:
        f.write("User-agent: *\nDisallow: /\n" if PREVIEW_NOINDEX else f"User-agent: *\nAllow: /\n\nSitemap: {url('sitemap.xml')}\n")
    open(os.path.join(OUT, ".nojekyll"), "w").close()
    from content import CALC_JS
    with open(os.path.join(OUT, "calc.js"), "w") as f: f.write(CALC_JS)
    with open(os.path.join(OUT, "favicon.svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0b3d50"/>'
                '<path d="M32 10C24 22 18 30 18 38a14 14 0 0 0 28 0c0-8-6-16-14-28z" fill="#8fd3e8"/>'
                '<path d="M25 39l5 5 9-11" stroke="#0b3d50" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    print(f"built {len(PAGES)} pages -> {os.path.abspath(OUT)}")

if __name__ == "__main__":
    build()
