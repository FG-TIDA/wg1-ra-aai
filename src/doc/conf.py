
import datetime

source_suffix = {'.rst': 'restructuredtext'}
master_doc = 'index'
exclude_patterns = []
pygments_style = 'colorful'
project = '<acronym>'
release = '<version>'
html_title = "<acronym>"
author = '<author>'

numfig = True

# Pin the LaTeX/PDF output to a stable filename (specification.tex ->
# specification.pdf) regardless of the project name, so the publish workflow
# always knows what to copy.
latex_documents = [
    (master_doc, 'specification.tex', project, author, 'manual'),
]

# --- Cover metadata: single source of truth for index.rst (via substitutions)
# and the LaTeX cover (via \newcommand interpolation below). Edit here.
cover_title    = '<acronym>'
cover_series   = '<series or category>'
cover_subject  = '<subject line>'
cover_subtitle = '<subtitle of this document>'

extensions = ['sphinxcontrib.httpdomain','sphinxcontrib.plantuml','sphinxcontrib.openapi', 'sphinx_copybutton']
# PlantUML command. On CI (GitHub Actions / Read the Docs) the `plantuml` package
# is installed via apt and provides a `plantuml` command on PATH, so the default
# works there. For a local build, set the PLANTUML environment variable to point at
# a local jar, e.g. (PowerShell):
#   $env:PLANTUML = "java -jar C:/dev/TIDA-spec-template/plantuml.jar"
import os as _os
plantuml = _os.environ.get("PLANTUML", "plantuml")
plantuml_output_format = 'svg'
templates_path = ['_templates']
html_js_files = [
    "osia-sidebar.js",
]

exclude_patterns = ['_*.rst', '*/_*.rst']

rst_prolog = '''

.. meta::
  :http-equiv=X-UA-Compatible: IE=9    

.. |tick|   unicode:: U+2714 .. HEAVY CHECK MARK
.. |project| replace:: OSIA
.. |release| replace:: '''+release+'''
.. |cover-title|    replace:: '''+cover_title+'''
.. |cover-series|   replace:: '''+cover_series+'''
.. |cover-subject|  replace:: '''+cover_subject+'''
.. |cover-subtitle| replace:: '''+cover_subtitle+'''

.. role:: todo

.. raw:: html

    <style>
        .todo {background-color: #f3f375;font-style: italic;}

        /* override table width restrictions */
        .wy-table-responsive table td, .wy-table-responsive table th {
            /* !important prevents the common CSS stylesheets from
            overriding this as on RTD they are loaded after this stylesheet */
            white-space: normal !important;
        }

        .wy-table-responsive {
            overflow: visible !important;
        }
        
        tr th.head {background-color: #00A0DD; color: white}

        li p {
            margin-top: 3px;
        }

        dl.py.function {
            margin-top: 20px;
        }

        dl dd p {
            margin: 0px;
        }

        figcaption p {
            text-align: center !important;
        }

    </style>

'''

#
# HTML Output Configuration
#
html_static_path = ['_static', 'images']
html_css_files = [
    #'custom.css',
    'osia-furo.css',
]
html_theme = "furo"
html_theme_options = {
    "sidebar_hide_name": False,
}
html_logo = "images/TIDA_logo.png"
html_show_sourcelink = False
copyright = '<year>, <author>'
html_context = {'project':project, 'version':release, 'copyright': copyright}
html_last_updated_fmt = '%b %d, %Y'
html_extra_path = ['yaml']

#
# Latex/PDF Output Configuration
#

# use small font for source code
# XXX investigate if it is possible to customize \sphinxVerbatim environment 
from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter
 
class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"
 
PygmentsBridge.latex_formatter = CustomLatexFormatter

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
 'papersize': 'a4paper',

# The font size ('10pt', '11pt' or '12pt').
 'pointsize': '10pt',

# Keep the figure where there are defined (no floating)
'figure_align':'H',

 # no raw string can contain '\u' (this is interpreted as unicode char)
 'preamble': u'''
\\usepackage{bbding,pifont} %% two dingbat fonts
\\usepackage{attachfile}

\\attachfilesetup{color=0 0.5 0.5}

\\DeclareUnicodeCharacter{2714}{\\Checkmark}
\\newcommand{\\DUroletodo}[1]{\\colorbox{yellow}{#1} }
\\usepackage{color}
\\usepackage{colortbl}
\\definecolor{tableheader}{rgb}{0,0.627,0.867}

\\usepackage{makeidx}
\\usepackage[columns=1]{idxlayout}

\\usepackage{draftwatermark}
\\SetWatermarkScale{0.5}

\\usepackage{tikz}
\\usetikzlibrary{positioning,calc}
\\definecolor{ituBg}{HTML}{2A2D31}
\\definecolor{ituRed}{HTML}{B91E1E}
\\definecolor{ituAccent}{HTML}{29ABE2}

''' + r'''

\renewcommand*{\sphinxstyletheadfamily}{\cellcolor{tableheader}\sffamily\color{white}}

%% HEADER-FOOTER (disabled). Previously defined \companylogo / \companylogobig
%% macros using logo.pdf / logo2.pdf; removed along with those unused images.

%% Front-matter toggle: \osiafrontmatter suppresses chapter / section
%% numbering (used between the cover and the first numbered chapter).
%% \osiamainmatter restores numbering and resets the chapter counter so
%% the chapter immediately after it becomes Chapter 1.
%% Neutralise sphinxmanual.cls's TOC page-numbering swaps so they don't fight
%% our \osiafrontmatter / \osiamainmatter macros. Also override \@title /
%% \release here (after Sphinx writes them from project / release in conf.py)
%% so the running header reads "Rec. ITU-T, Release <acronym>" in the PDF only,
%% without touching the HTML.
\AtBeginDocument{%
  \renewcommand{\sphinxtableofcontents}{%
    \begingroup
      \parskip = 0mm
      \tableofcontents
    \endgroup
    \if@openright\cleardoublepage\else\clearpage\fi
  }%
  \title{Rec. ITU-T}%
  \release{<acronym>}%
}

%% Hide the next \chapter heading. Used to suppress the "Overview" chapter
%% title on its opening page while keeping the chapter in the TOC.
%% The whole block runs under \makeatletter/\makeatother so that \@-tokens
%% are stored correctly inside the macro bodies (the \makeatletter inside
%% \newcommand{}{...} doesn't help — by then the body has already been
%% tokenized).
\makeatletter
\AtBeginDocument{%
  \let\osiaorigmakechapterhead\@makechapterhead
}
\newcommand{\osiahidenextchapterhead}{%
  \renewcommand{\@makechapterhead}[1]{%
    \global\let\@makechapterhead\osiaorigmakechapterhead
  }%
}
\makeatother

%% Skip the next \chapter{...} call entirely: no TOC entry, no heading, no
%% counter bump. Only emits a \cleardoublepage to start a fresh page, then
%% restores \chapter for subsequent calls. Used so the "Overview" chapter
%% has no row in the PDF TOC while its content still renders normally.
\newcommand{\osiaskipnextchapter}{%
  \let\osiaorigchapter\chapter
  \def\chapter##1{%
    \cleardoublepage%
    \let\chapter\osiaorigchapter%
  }%
}

%% Centered unnumbered section / subsection titles that still appear in the
%% TOC. Used for the front-matter overview chapter (X-Series, Foreword,
%% Note, Intellectual Property Rights). These hijack the NEXT \section /
%% \subsection call so the rst heading can stay at the proper document
%% level (HTML keeps its section structure with body content nested
%% correctly), while the PDF gets the custom centered rendering.
\newcommand{\osiacenternextsection}{%
  \let\osiaorigsection\section
  \def\section##1{%
    \par\addvspace{1.5em}%
    \begin{center}{\normalfont\Large\bfseries ##1\par}\end{center}%
    \par\addvspace{0.5em}%
    \addcontentsline{toc}{section}{##1}%
    \let\section\osiaorigsection%
  }%
}
\newcommand{\osiacenternextsubsection}{%
  \let\osiaorigsubsection\subsection
  \def\subsection##1{%
    \par\addvspace{2.5em}%
    \begin{center}{\normalfont\large\bfseries ##1\par}\end{center}%
    \par\addvspace{1em}%
    \addcontentsline{toc}{subsection}{##1}%
    \let\subsection\osiaorigsubsection%
  }%
}

\newcommand{\osiafrontmatter}{%
  \setcounter{secnumdepth}{-1}%
  \pagestyle{plain}%            % page footer: page number only (no chapter name)
  \pagenumbering{roman}%        % i, ii, iii ... for cover + overview + TOC
}
\newcommand{\osiamainmatter}{%
  \setcounter{secnumdepth}{2}%
  \setcounter{chapter}{0}%
  \pagestyle{normal}%           % restore Sphinx's default header/footer
  \pagenumbering{arabic}%       % restart at 1, arabic, for Chapter 1 onward
}

%% Cover metadata — kept in sync with the same strings used in index.rst.
%% Source of truth lives in conf.py (cover_title, cover_series, cover_subject,
%% cover_subtitle). Edit there, not here.
\newcommand{\coverTitle}{'''+cover_title+r'''}
\newcommand{\coverSeries}{'''+cover_series.replace('–', '--')+r'''}
\newcommand{\coverSubject}{'''+cover_subject.replace('–', '--')+r'''}
\newcommand{\coverSubtitle}{'''+cover_subtitle+r'''}

%% TITLE — ITU-style cover page (white background, fits the rest of the document)
\newcommand{\osiamaketitle}{%
  \begin{titlepage}
    \thispagestyle{empty}
    \begin{tikzpicture}[remember picture, overlay]
      %% Top-left banner: ITUPublications / Recommendations
      \node[anchor=north west, inner sep=0pt]
        at ([xshift=1.5cm, yshift=-1.3cm]current page.north west)
        {\sffamily\Large\textcolor{ituAccent}{\textbf{ITU}}\textbf{Publications}};
      \node[anchor=north west, inner sep=0pt]
        at ([xshift=1.5cm, yshift=-1.9cm]current page.north west)
        {\sffamily\normalsize Recommendations};

      %% Top-right banner: International Telecommunication Union / Standardization Sector
      \node[anchor=north east, inner sep=0pt]
        at ([xshift=-1.5cm, yshift=-1.3cm]current page.north east)
        {\sffamily\normalsize\textbf{International Telecommunication Union}};
      \node[anchor=north east, inner sep=0pt]
        at ([xshift=-1.5cm, yshift=-1.9cm]current page.north east)
        {\sffamily\small Standardization Sector};

      %% Red horizontal bar
      \fill[ituRed] ([yshift=-2.6cm]current page.north west)
        rectangle ([yshift=-2.95cm]current page.north east);
      %% Red downward triangle
      \fill[ituRed]
        ([xshift=2cm, yshift=-2.95cm]current page.north west) --
        ([xshift=2.7cm, yshift=-2.95cm]current page.north west) --
        ([xshift=2.35cm, yshift=-3.4cm]current page.north west) -- cycle;

      %% Title block — text pulled from conf.py cover_* constants.
      %% \hyphenpenalty=10000\exhyphenpenalty=10000 + \sloppy disables word
      %% hyphenation so labels never split (e.g. "systems" → "sys-tems").
      %% Wider text_width (18cm) gives the larger sizes room to fit on one line.
      \node[anchor=north west, inner sep=0pt, text width=18cm]
        at ([xshift=1.5cm, yshift=-4.8cm]current page.north west)
        {\sffamily\hyphenpenalty=10000\exhyphenpenalty=10000\sloppy%
         {\huge Recommendation}\\[0.4cm]
         {\Huge\bfseries \coverTitle}\\[1.2cm]
         {\Large \coverSeries}\\[0.5cm]
         {\Large \coverSubject}};

      %% Thin separator
      \draw[black, line width=0.4pt]
        ([xshift=1.5cm, yshift=-12.5cm]current page.north west) --
        ([xshift=-1.5cm, yshift=-12.5cm]current page.north east);

      %% Subtitle
      \node[anchor=north west, inner sep=0pt, text width=18cm]
        at ([xshift=1.5cm, yshift=-13cm]current page.north west)
        {\sffamily\hyphenpenalty=10000\exhyphenpenalty=10000\sloppy\LARGE\bfseries \coverSubtitle};

      %% TIDA logo bottom-right
      \node[anchor=south east, inner sep=0pt]
        at ([xshift=-1.5cm, yshift=1.5cm]current page.south east)
        {\includegraphics[width=2.5cm]{tida-logo.png}};
    \end{tikzpicture}
  \end{titlepage}
  \cleardoublepage
  \setcounter{footnote}{0}
  \relax\let\maketitle\relax
}

''',

  'maketitle': r'\osiamaketitle\osiafrontmatter',
  # TOC suppressed at its default slot; emitted manually at the end of
  # 00 - overview.rst so the overview chapter physically precedes the TOC.
  'tableofcontents': '',
  'atendofbody':u'''
  \\listoftables
  \\listoffigures
 ''',

'classoptions' : ',english,openany,oneside'
}

# DRAFT watermark always disabled (PDF should not be marked as DRAFT even when
# `release` still contains "DRAFT"). To re-enable, switch back to the
# `if 'DRAFT' in release` conditional that was here previously.
# if 'DRAFT' in release:
#     latex_elements['preamble'] += '\\SetWatermarkText{}'
latex_elements['preamble'] += '\\SetWatermarkText{}'

# Copy images
import os,shutil,fnmatch
def setup(app):
    try:
        os.makedirs(app.outdir)
    except:
        pass
    for root, dirs, files in os.walk(os.path.join(app.srcdir,'images')):
        for pattern in ('*.pdf', '*.png'):
            for f in fnmatch.filter(files, pattern):
                shutil.copy(os.path.join(root, f), app.outdir)


if 'itu' in tags:
    rst_prolog += '''
.. |osia| replace:: ITU-T <acronym>
.. |specification| replace:: recommendation
.. |chapter| replace:: clause
    '''
else:
    rst_prolog += '''
.. |osia| replace:: OSIA
.. |specification| replace:: specification
.. |chapter| replace:: chapter
    '''
