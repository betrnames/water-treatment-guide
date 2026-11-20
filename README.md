# Test First Water (working name) — preview

Whole-home water treatment guide. Static site, plain Python generator, no dependencies.

- Source: `src/build.py` (layout, CSS) + `src/content.py` (all copy, verified URLs, calculator JS)
- Output: `docs/` (served by GitHub Pages from main:/docs)
- Rebuild: `cd src && python3 build.py && cd .. && git add -A && git commit -m update && git push`
- Preview is `noindex,nofollow` + robots `Disallow: /`. To go live on a real domain: `PREVIEW_NOINDEX=0 SITE_ORIGIN=https://<domain> BASE_PATH=/ python3 build.py`
- Affiliate placeholders: every brand link has `data-affiliate="<program>"` and NO tag yet (`rg -n 'data-affiliate' docs`).
