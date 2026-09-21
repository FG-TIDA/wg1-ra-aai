# Live preview of the documentation.
# Serves the docs at http://127.0.0.1:8000, auto-rebuilds on save, and
# live-reloads the browser. Diagrams render locally via the bundled PlantUML jar.
#
# Usage (from the repo root):
#   .\preview.ps1
#
# Stop with Ctrl+C.

$ErrorActionPreference = "Stop"
$root = $PSScriptRoot

# Point Sphinx at the local PlantUML jar so .. uml:: diagrams render.
# (On CI the `plantuml` apt package is used instead; see conf.py.)
$jar = Join-Path $root "plantuml.jar"
if (Test-Path $jar) {
    $env:PLANTUML = "java -jar $jar"
} else {
    Write-Warning "plantuml.jar not found at $jar - UML diagrams will not render locally."
    Write-Warning "Download it from https://plantuml.com/download and place it in the repo root."
}

# -a forces Sphinx to rewrite ALL output on every rebuild. This is required
# because Sphinx does not track ".. include::" dependencies: without -a, editing
# an included file (e.g. functional/_notification.rst) may not refresh the parent
# page that includes it, so changes silently fail to appear.
& (Join-Path $root ".venv\Scripts\sphinx-autobuild.exe") `
    "src\doc" "target\html" `
    -a `
    --open-browser `
    --ignore "*.tmp"
