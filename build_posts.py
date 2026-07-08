"""Build blog post pages from posts/*.md and refresh the blog list in index.html.

Usage: python3 build_posts.py
- posts/<slug>.md (frontmatter: slug, title, date, order, excerpt) -> blog/<slug>.html
- index.html: replaces the block between <!-- POSTS:START --> and <!-- POSTS:END -->
"""
import glob, html, os, re

TEMPLATE = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · mari</title>
<link rel="stylesheet" href="/assets/fonts.css">
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
  <p class="meta">{date} · {category} · <span class="hl">publicado en LinkedIn</span></p>
  <article>
{body}
  </article>
  <footer>© 2026 Mari · hand-drawn on the internet</footer>
</div>
</body>
</html>
"""


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
print(f"built {len(posts)} post pages, index updated")
