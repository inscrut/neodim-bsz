# AGENTS.md

MkDocs + Material documentation site (Russian language) for Неодим БСЗ ignition-conversion kits. Content-only repo: Markdown under `docs/`, config in `mkdocs.yml`. No app code, no tests/lint/typecheck gates. Site: https://bsz.neodim.tech/. Deployed to GitHub Pages by CI (`push` → `main`).

## Commands

```bash
python3 -m venv .venv && source .venv/bin/activate   # setup
pip install -r requirements.txt
mkdocs serve -a 0.0.0.0:3000                          # dev server
mkdocs build --strict                                 # verification gate
```

- **`mkdocs build --strict` must pass before every commit/push.** CI runs exactly this command; broken links or missing pages fail the deploy. It is the only automated check in this repo.
- The red «MkDocs 2.0 is incompatible» banner printed on every build comes from the upstream `mkdocs-material` package itself (verified byte-identical to the PyPI wheel) — harmless noise; set `NO_MKDOCS_2_WARNING=1` to silence it. Judge success by exit code, not by that banner.
- CI additionally installs `pngquant` via apt (Material image optimization); local builds without it may optimize images differently.

## Non-obvious constraints

- Do NOT upgrade `mkdocs-redirects`: pinned at `==1.2.2` because 1.2.3 pulls in "properdocs", which injects ad messages into the build log (see comment in `requirements.txt`).
- Renaming/moving a page requires three edits: new file location, entry in `nav:` (mkdocs.yml), and an old→new mapping under `plugins.redirects.redirect_maps` (keeps the live URL working). Also update the section's index grid/table.
- `snippets/*.md` are excluded from the build (`exclude_docs`) and included only via pymdownx.snippets: ``--8<-- "snippets/file.md"`` (base_path = `docs`). Never add them to `nav:`.
- `legal/*.md` pages exist only in the footer (`not_in_nav`). Never delete them, never put them in `nav:`.
- Brand color `#EE781C` lives in `docs/stylesheets/extra.css`; don't change colors, or the analytics/VK scripts in `overrides/main.html`, without explicit approval.

## Writing conventions (full detail in `rules.md` at repo root — read it before writing content)

Content is Russian, formal «вы», technical tone. Key mechanical rules:

- Every heading gets an explicit English anchor: `# Title {#title-slug}`.
- Images use relative paths with explicit width: `![alt](../assets/wiki/foo.webp){ width="360" }`; prefer webp/jpg over PNG.
- Cross-page links are relative `.md` paths within `docs/`.
- New page checklist: create the file → add to `nav:` in mkdocs.yml → add a card to the section `index.md` grid (distributors also need a row in `docs/distributors/index.md`) → put images under `docs/assets/wiki/<section>/`.

## Ozon data script

`scripts/merge_ozon_export.py` merges Ozon seller exports from `items/*.csv` into the committed `scripts/ozon_merged.json`. The CSVs are gitignored and **not present in the repo** (products CSV: utf-8-sig; content CSVs: cp1251; all `;`-delimited). The script cannot run without those local files.

## Git workflow

Per `rules.md` §10: do not run `git commit` or `git push` yourself — prepare changes, verify the strict build, and let the human commit/push.
