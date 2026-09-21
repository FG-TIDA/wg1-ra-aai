# TIDA Specification Template

**See the template live:**
📄 **[Web page](https://fg-tida.github.io/spec-template/)** ·
📥 **[PDF](https://fg-tida.github.io/spec-template/specification.pdf)**

The pages you see there are produced by this repository — they double as the
template's documentation, explaining and demonstrating how to write a spec.

> **Starting a new specification?** Follow
> **[WG-ONBOARDING.md](WG-ONBOARDING.md)**. Once your repo is created, replace
> the text of this README with a short description of *your* specification
> (what it is, its status, and a link to its published site).

---

A specification for the FG-TIDA working groups, authored with the shared TIDA
template: one source that builds a modern web page and a print-ready PDF, with
support for diagrams and auto-generated API references.

## Quick start

1. Click **Use this template → Create a new repository** (owner `FG-TIDA`, name
   `wg<N>-<short-name>`).
2. In the new repo: **Settings → Pages → Source: GitHub Actions**.
3. Edit the content under `src/doc/` — replace the `<placeholders>` and the
   example text. Full instructions are in **[WG-ONBOARDING.md](WG-ONBOARDING.md)**.
4. Push to `main`. The site and PDF publish automatically to
   `https://fg-tida.github.io/<repo-name>/`.

## In this repository

- `src/doc/index.rst` — the document front matter (title, abstract, authors…).
- `src/doc/chapters/` — the chapters; they explain and demonstrate how to write
  content, then you replace them with your own.
- `HOWTO.md` — how to build and preview locally, and how to customise.
- `WG-ONBOARDING.md` — the full step-by-step guide for authors.

Built on the open-source [CUTEspecs](https://github.com/debora-com/CUTEspecs)
template.
