# themari.blog

Personal website. Hand-drawn style, vibecoded with Claude.

## Estructura

- `index.html` — el sitio entero (fuentes embebidas, sin build de framework)
- `posts/<slug>.md` — cada post del blog (frontmatter: slug, title, category, date, order, excerpt)
- `build_posts.py` — genera `blog/<slug>.html` y rellena las cards del index entre `<!-- POSTS:START -->` y `<!-- POSTS:END -->`
- `assets/fonts.css` — fuentes compartidas por las páginas de posts
- `api/feedback.js` — función serverless del form de feedback anónimo (guarda en Vercel Blob privado)

## Publicar un cambio

1. Editar lo que sea
2. **REGLA DE ORO: si `index.html` fue regenerado desde plantilla, correr SIEMPRE `python3 build_posts.py` después** (si no, el blog queda sin artículos)
3. `git add -A && git commit && git push`
4. `npx vercel deploy --prod --yes`

## Publicar un post nuevo

1. Crear `posts/mi-post.md` con el frontmatter (order: 0 para que quede primero, o renumerar)
2. `python3 build_posts.py`
3. Commit + deploy (pasos 3 y 4 de arriba)

## Leer el feedback anónimo

Desde esta carpeta:

```
TOKEN=$(grep '^BLOB_READ_WRITE_TOKEN=' .env.local | cut -d'"' -f2)
npx vercel blob list --rw-token "$TOKEN"
```
