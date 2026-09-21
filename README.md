# Remote Attestation Challenges for AI Agents

*What to attest · How to attest · When to attest?*

An FG-TIDA Working Group 1 specification examining the challenges of **remote
attestation (RA) for AI agents** — surveying the landscape, stating the problem
for agentic AI, identifying core challenges and gaps, and mapping existing
standards (IETF, TCG) to the needs of AI-agent attestation.

**Read it online:**
📄 **[Web page](https://fg-tida.github.io/wg1-ra-aai/)** ·
📥 **[PDF](https://fg-tida.github.io/wg1-ra-aai/specification.pdf)**

> **Status:** Draft (v0.1) — work in progress. Sections currently contain author
> notes marked *[Author: …]* to be filled in.

## Structure

The document source lives under `src/doc/`. Each chapter is a file in
`src/doc/chapters/`:

| File | Chapter |
| --- | --- |
| `01_landscape.rst` | RA Landscape: Industry Analysis |
| `02_problem-statement.rst` | Problem Statement |
| `03_core-challenges.rst` | RA Core Challenges |
| `04_three-questions.rst` | Three Fundamental Questions (what / how / when) |
| `05_building-blocks.rst` | Standards' Existing Building Blocks (IETF, TCG) |
| `06_future-directions.rst` | Future Directions |
| `07_references.rst` | References |

The title page, abstract, authors and foreword are in `src/doc/index.rst`.

## How to contribute

You do not need to build anything locally to contribute — you can edit the
`.rst` files directly on GitHub and open a pull request. The site and PDF are
rebuilt automatically when changes are merged.

1. **Fork** this repository (button at the top right of the GitHub page).
2. Edit the relevant chapter in `src/doc/chapters/` (or `src/doc/index.rst` for
   the title/abstract/authors). The text is
   [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html);
   the existing content shows the patterns for headings, lists, tables, figures,
   and cross-references.
3. Commit your changes to your fork.
4. Open a **pull request** back to this repository.

When the pull request is merged into `main`, the published web page and PDF
update automatically (via GitHub Actions).

## Building locally (optional)

To preview your changes on your own machine before opening a pull request.

**1. Clone your fork** (replace `<your-username>` with your GitHub username):

```shell
git clone https://github.com/<your-username>/wg1-ra-aai.git
cd wg1-ra-aai
```

**2. Install Python 3.10+** (from <https://www.python.org/downloads/>), then
install the build dependencies. A virtual environment is recommended so the
packages stay isolated:

```shell
python -m venv .venv
# activate it:
#   Windows (PowerShell):  .venv\Scripts\Activate.ps1
#   macOS / Linux:         source .venv/bin/activate
pip install -r requirements.txt
```

**3. Diagrams — you can skip this.** Most editing (all the text, tables and
lists) does **not** need it. You only need this step if your changes include
diagrams *and* you want to see them drawn on your own machine. Either way, the
diagrams are always drawn correctly on the published website — this is only
about the local preview.

If you do want diagrams locally: install [Java](https://adoptium.net/), download
the file `plantuml.jar` from <https://plantuml.com/download>, save it into the
project folder (next to `requirements.txt`), and run this once in your terminal
before building:

```powershell
$env:PLANTUML = "java -jar $PWD/plantuml.jar"
```

(If you skip this, everything still builds — diagrams just appear as a "broken
image" placeholder in your local preview.)

**4. Preview the document.** Two ways:

*Simplest — build once and open the result:*

```shell
sphinx-build -b html src/doc target/html
```

Then open the file `target/html/index.html` in your web browser.

*Recommended — automatic live preview.* The project already includes a small
helper script called `preview.ps1` (nothing to install — it is part of the
files you cloned). On Windows, run it from the project folder:

```powershell
./preview.ps1
```

It opens the document in your browser and **refreshes it automatically every
time you save a file**, so you can see your edits as you type. Press `Ctrl+C` in
the terminal to stop it.

**5. When you are happy, commit your changes, push them to your fork, and open a
pull request** (see *How to contribute* above).

Full build details and customisation notes are in [HOWTO.md](HOWTO.md).

## About

Produced by **FG-TIDA** (Focus Group on Trust and Identity for humans and
agentic AI) using the [CUTEspecs](https://github.com/debora-com/CUTEspecs)
specification template.
