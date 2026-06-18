# COTHROM — Democratic Redistricting Education

An interactive [Jupyter Book](https://jupyterbook.org) that explains **democratic
redistricting and electoral boundaries in Ireland** — how constituency boundaries
are drawn, why they matter for fair representation, and how computational methods
can help. It is the public-facing educational companion to the **COTHROM** project
by [The Problem Solving Association (TPSA)](https://tpsa.ie/problemsolving).

> *Cothrom* is Irish for "fairness" or "balance".

## What's inside

- **Module 0 — Getting Started**: why redistricting affects your vote, how to find
  your Electoral Division (ED), and what drives boundary changes.
- **Interactive tools** (`_static/interactive/`): a map-based ED finder and a set of
  visual explainers for population variance, contiguity, compactness, county
  boundaries, and trade-offs.

> ⚠️ **Data note**: the constituency/ED datasets in `_static/data/` are currently
> **illustrative sample data**, not official figures, and the tools display a banner
> to that effect. Headline statistics in the prose are sourced from the Electoral
> Commission's 2023 review and CSO Census 2022 (see `references.bib`). Replace the
> sample data with official datasets via `scripts/` before treating tool output as
> authoritative.

## Repository layout

```
content/            # MyST-markdown lessons (the book)
  index.md
  module_0/
_static/
  interactive/      # self-contained interactive HTML widgets (loaded via iframe)
  data/             # sample datasets consumed by the widgets
scripts/            # data download / processing helpers
_config.yml         # Jupyter Book configuration
_toc.yml            # table of contents
references.bib      # citations for statistics used in the content
```

## Building locally

A Unix-like shell is assumed. Windows users: configure your editor to use **LF**
line endings (this repo enforces `* text=auto eol=lf` via `.gitattributes`).

```bash
# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Build the book
jupyter-book build .
```

The built site is written to `_build/html`. Open `_build/html/index.html`, or serve
it (recommended, so iframes/fetch work):

```bash
python -m http.server -d _build/html 8000   # then visit http://localhost:8000
```

To force a clean rebuild: `jupyter-book build --all .`

## Deployment

`.github/workflows/publish.yml` builds the book and deploys it to **GitHub Pages**
on every push to `main`. The base URL is set from the repository name, so internal
asset references use **relative paths** (e.g. `../../_static/...`) to work under the
`/COTHROM_education/` Pages prefix.

## Adding a page

1. Create the `.md` file under `content/`.
2. Add it to `_toc.yml`.
3. Rebuild and check navigation and links.

## Licence

See [`LICENSE`](LICENSE). © The Problem Solving Association C.L.G.
