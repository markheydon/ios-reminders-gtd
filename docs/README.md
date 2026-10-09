# Contributing to the guide (repository layout)

## Where to edit

| You want to… | Open |
| --- | --- |
| Change guide prose, setup steps, or examples | [`guide/`](../guide/) (`guide/why.md`, `guide/setup.md`, …) |
| Change the home page intro and reading list | [`guide/_index.md`](../guide/_index.md) |
| Update diagrams | [`guide/images/`](../guide/images/) (SVG) |
| Change PDF/EPUB cover or export metadata | [`book/`](../book/) |
| Change site theme, footer, or Hugo config | [`website/`](../website/) |

**README.md** numbered list matches **book/chapters.txt** (book export order). **guide/_index.md** uses Quick Start plus Read the Full Guide and must link each chapter once. CI checks both with `python3 scripts/check-guide.py`.

## Preview and checks

From the repository root:

```bash
python3 scripts/check-guide.py
./scripts/invoke-hugo-site.sh serve    # or preview / build (Docker or Podman)
./scripts/build-book.sh                # needs pandoc, rsvg-convert, xelatex
```

On Windows, use `./scripts/Invoke-HugoSite.ps1` instead of the shell script.

Native Hugo (without Docker): install **Hugo extended**, **Go**, and **Dart Sass** (versions in [`.github/workflows/hugo-build.yml`](../.github/workflows/hugo-build.yml)), then:

```bash
cd website
hugo mod get
hugo server --baseURL http://localhost:1313/ios-reminders-gtd/
```

## Published site

The live guide is built with [Hugo Book](https://github.com/alex-shpak/hugo-book) (Go modules in [`website/go.mod`](../website/go.mod), not git submodules). Chapter files are read from `guide/` via `contentDir` in [`website/hugo.yaml`](../website/hugo.yaml).

- **Production URL:** [markheydon.me.uk/ios-reminders-gtd](https://markheydon.me.uk/ios-reminders-gtd/)
- **Deploy:** merge to `main` runs [`.github/workflows/hugo-deploy.yml`](../.github/workflows/hugo-deploy.yml)
- **GitHub Pages:** Settings → Pages → source **GitHub Actions** (not “Deploy from branch `/docs`”)

Footer text lives in [`website/layouts/partials/docs/inject/footer.html`](../website/layouts/partials/docs/inject/footer.html).

## House style

See [AGENTS.md](../AGENTS.md) and [CONTRIBUTING.md](../CONTRIBUTING.md).
