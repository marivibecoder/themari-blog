"""Build blog post pages from posts/*.md and refresh the blog list in index.html.

Usage: python3 build_posts.py
- posts/<slug>.md (frontmatter: slug, title, date, order, excerpt) -> blog/<slug>.html
- index.html: replaces the block between <!-- POSTS:START --> and <!-- POSTS:END -->
- sitemap.xml + llms.txt: regenerated on every build so SEO/GEO stays fresh
"""
import datetime, glob, html, json, os, re

SITE = "https://www.themari.blog"
AUTHOR = "Mariana Flores Guillén"
OG_IMAGE = f"{SITE}/assets/og.png"
FAVICON = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Crect width='100' height='100' rx='22' fill='%23FFD139'/%3E%3Ctext x='50' y='74' font-size='68' text-anchor='middle' font-family='Marker Felt,Comic Sans MS,cursive' fill='%231A1A1A'%3Em%3C/text%3E%3C/svg%3E"

MONTHS = {"ene": 1, "feb": 2, "mar": 3, "abr": 4, "may": 5, "jun": 6,
          "jul": 7, "ago": 8, "sep": 9, "oct": 10, "nov": 11, "dic": 12}

TEMPLATE = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · mari</title>
<meta name="description" content="{excerpt}">
<meta name="author" content="Mariana Flores Guillén">
<link rel="canonical" href="{url}">
<link rel="icon" href="{favicon}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="themari.blog">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{excerpt}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="es_ES">
<meta property="article:published_time" content="{iso}">
<meta property="article:author" content="Mariana Flores Guillén">
<meta property="article:section" content="{category}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{excerpt}">
<meta name="twitter:image" content="{og_image}">
<link rel="stylesheet" href="/assets/fonts.css">
<script type="application/ld+json">{jsonld}</script>
<style>
:root {{
  --paper: #FFFFFF; --ink: #1A1A1A; --soft: #6E6E6E;
  --yellow: #FFD139; --yellow-dark: #DFAF1E;
  --keycap: #F6F5F1; --keycap-edge: #D5D3CB;
}}
@media (prefers-color-scheme: dark) {{
  :root {{ --paper: #17181A; --ink: #F2F0E9; --soft: #9A9A94; --keycap: #292A2E; --keycap-edge: #101113; }}
}}
:root[data-theme="light"] {{ --paper: #FFFFFF; --ink: #1A1A1A; --soft: #6E6E6E; --keycap: #F6F5F1; --keycap-edge: #D5D3CB; }}
:root[data-theme="dark"] {{ --paper: #17181A; --ink: #F2F0E9; --soft: #9A9A94; --keycap: #292A2E; --keycap-edge: #101113; }}
* {{ box-sizing: border-box; }}
html {{ background: var(--paper); }}
body {{
  margin: 0; background: var(--paper); color: var(--ink);
  font-family: 'Roboto Mono', ui-monospace, monospace; font-size: 15px; line-height: 1.8;
}}
.wrap {{ max-width: 680px; margin: 0 auto; padding: 30px 24px 90px; }}
.back {{
  display: inline-block; text-decoration: none; color: var(--ink);
  font-size: 13px; padding: 8px 16px 10px; border-radius: 6px;
  background: var(--keycap); box-shadow: 0 4px 0 var(--keycap-edge);
  transition: transform .06s ease, box-shadow .06s ease;
}}
.back:hover {{ transform: translateY(-1px); }}
.back:active {{ transform: translateY(3px); box-shadow: 0 1px 0 var(--keycap-edge); }}
h1 {{
  font-family: 'Gochi Hand', 'Chalkboard SE', cursive; font-weight: 400;
  font-size: clamp(34px, 6vw, 46px); line-height: 1.15; margin: 44px 0 6px;
  text-wrap: balance; transform: rotate(-0.5deg);
}}
.meta {{ color: var(--soft); font-size: 12.5px; text-transform: uppercase; letter-spacing: .5px; margin-bottom: 40px; }}
.meta .hl {{ background: linear-gradient(transparent 55%, var(--yellow) 55%, var(--yellow) 92%, transparent 92%); color: var(--ink); padding: 0 2px; }}
article p {{ margin: 0 0 1.25em; }}
footer {{ margin-top: 70px; color: var(--soft); font-size: 12.5px; }}
a:focus-visible {{ outline: 2.5px solid var(--yellow-dark); outline-offset: 3px; }}
</style>
</head>
<body>
<div class="wrap">
  <a class="back" href="/#blog">&larr; blog</a>
  <h1>{title}</h1>
  <p class="meta"><time datetime="{iso}">{date}</time> · {category} · <span class="hl">publicado en LinkedIn</span></p>
  <article>
{body}
  </article>
  <footer>© 2026 Mari · hand-drawn on the internet</footer>
</div>
</body>
</html>
"""


def iso_date(date_str):
    """'sep 2025' -> '2025-09-01'"""
    mon, year = date_str.strip().split()
    return f"{int(year):04d}-{MONTHS[mon.lower()]:02d}-01"


def parse(path):
    raw = open(path).read()
    m = re.match(r"---\n(.*?)\n---\n\n?(.*)", raw, re.S)
    meta = dict(line.split(": ", 1) for line in m.group(1).strip().split("\n"))
    meta["order"] = int(meta["order"])
    return meta, m.group(2).strip()


def body_html(text):
    out = []
    for para in text.split("\n\n"):
        p = html.escape(para).replace("\n", "<br>\n")
        out.append(f"    <p>{p}</p>")
    return "\n".join(out)


def post_jsonld(meta):
    url = f"{SITE}/blog/{meta['slug']}"
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "headline": meta["title"],
        "description": meta["excerpt"],
        "datePublished": iso_date(meta["date"]),
        "inLanguage": "es",
        "url": url,
        "mainEntityOfPage": url,
        "isPartOf": {"@id": f"{SITE}/#blogfeed"},
        "articleSection": meta.get("category", ""),
        "image": OG_IMAGE,
        "author": {"@type": "Person", "name": AUTHOR, "url": f"{SITE}/"},
        "publisher": {"@type": "Person", "name": AUTHOR},
    }, ensure_ascii=False)


def build_sitemap(posts):
    today = datetime.date.today().isoformat()
    urls = [
        f"  <url>\n    <loc>{SITE}/</loc>\n    <lastmod>{today}</lastmod>\n"
        f"    <changefreq>weekly</changefreq>\n    <priority>1.0</priority>\n  </url>"
    ]
    for meta, _ in posts:
        urls.append(
            f"  <url>\n    <loc>{SITE}/blog/{meta['slug']}</loc>\n"
            f"    <lastmod>{iso_date(meta['date'])}</lastmod>\n  </url>"
        )
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
           + "\n".join(urls) + "\n</urlset>\n")
    open("sitemap.xml", "w").write(xml)


def build_llms(posts):
    lines = [
        "# themari.blog",
        "",
        '> Personal website and blog of Mariana Flores Guillén ("mari") — Chief of Staff at an AI startup, Venezuelan living in Buenos Aires, working in tech since she was a teenager (operations, not code). Short, direct blog posts written in Spanish about work, AI, careers, startups and mindset.',
        "",
        "The site UI is bilingual (English/Spanish); all blog posts are written in Spanish. Posts were originally published on LinkedIn and are archived here in full.",
        "",
        "## Blog posts (newest first)",
        "",
    ]
    for meta, _ in posts:
        cat = meta.get("category", "")
        lines.append(
            f"- [{meta['title']}]({SITE}/blog/{meta['slug']}): {meta['excerpt']} "
            f"({cat}, {iso_date(meta['date'])[:7]})"
        )
    lines += [
        "",
        "## Site sections (single page)",
        "",
        f"- [about]({SITE}/#about): who mari is and what she's up to now",
        f"- [blog]({SITE}/#blog): the full post list",
        f"- [vibecoded]({SITE}/#vibecoded): personal coding projects (coming soon)",
        f"- [bookshelf]({SITE}/#bookshelf): the books on her shelf, in three themed rows",
        "",
        "## Contact",
        "",
        "- [LinkedIn](https://www.linkedin.com/in/mariana-flores-guillen/)",
        "- Email: mari@pacifg.com",
        "",
    ]
    open("llms.txt", "w").write("\n".join(lines))


posts = []
for path in glob.glob("posts/*.md"):
    meta, body = parse(path)
    posts.append((meta, body))
posts.sort(key=lambda x: x[0]["order"])

os.makedirs("blog", exist_ok=True)
for meta, body in posts:
    page = TEMPLATE.format(
        title=html.escape(meta["title"]), date=meta["date"],
        category=meta.get("category", ""), body=body_html(body),
        excerpt=html.escape(meta["excerpt"]), slug=meta["slug"],
        url=f"{SITE}/blog/{meta['slug']}", iso=iso_date(meta["date"]),
        og_image=OG_IMAGE, favicon=FAVICON, jsonld=post_jsonld(meta),
    )
    open(f"blog/{meta['slug']}.html", "w").write(page)

cards = []
for meta, _ in posts:
    cat = meta.get("category", "")
    cards.append(f"""      <article class="entry" data-cat="{cat}">
        <div class="meta">{meta['date']}<span class="cat">{cat}</span></div>
        <div>
          <h3 class="hand"><a href="/blog/{meta['slug']}">{html.escape(meta['title'])}</a></h3>
          <p>{html.escape(meta['excerpt'])}</p>
        </div>
      </article>""")
cards_html = "\n".join(cards)

index = open("index.html").read()
new_index = re.sub(
    r"(<!-- POSTS:START -->).*?(<!-- POSTS:END -->)",
    lambda m: m.group(1) + "\n" + cards_html + "\n      " + m.group(2),
    index, flags=re.S,
)
open("index.html", "w").write(new_index)

build_sitemap(posts)
build_llms(posts)
print(f"built {len(posts)} post pages, index updated, sitemap.xml + llms.txt regenerated")
