
.. raw:: latex

    \pagestyle{plain}
    \thispagestyle{plain}
    %% Suppress all TOC entries for the overview chapter (sections, subsections,
    %% Copyright addcontentsline) — restored just before \sphinxtableofcontents
    %% so chapters from Introduction onward appear in the TOC normally.
    \let\osiaorigaddcontentsline\addcontentsline
    \renewcommand{\addcontentsline}[3]{}

.. _chapter-overview:

.. only:: html

    .. admonition:: This is a document template
        :class: tip

        Replace the ``<placeholders>`` and the *lorem ipsum* text throughout with
        your own content. This landing page is the document's front matter:

        * **Abstract**, **History**, **Authors**, **Keywords** and **Foreword**
          are standard front-matter sections — keep them and fill them in.
        * **Chapters 1–4** demonstrate the authoring system (text, figures,
          tables, diagrams, and API references). Read them, then replace their
          content with your specification.

        This notice appears on the web version only; it is excluded from the
        published PDF. See the project ``HOWTO`` for how to build and publish.

Title of this document
========================

.. only:: html

    **<subtitle of this document>**

.. raw:: latex

    \begin{center}\textbf{<subtitle of this document>}\end{center}

Abstract
--------

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.

History
-------

.. list-table::
    :header-rows: 1
    :widths: 10 26 18 14 32

    * - Version
      - Document
      - Approval
      - Focus Group
      - Working Group
    * - <version>
      - <title>
      - <date>
      - TIDA
      - <acronym>

To access this Document as a PDF, open the published documentation site in your web
browser and click the PDF download link, or navigate directly to
https://debora-com.github.io/CUTEspecs/specification.pdf.

Authors
-------

.. list-table::
    :header-rows: 1
    :widths: 30 40 30

    * - Name
      - Affiliation
      - Contact
    * - <Jane Doe>
      - <Organization / Company>
      - <jane.doe@example.com>
    * - <John Smith>
      - <Organization / Company>
      - <john.smith@example.com>

Keywords
--------

Lorem, ipsum, dolor, consectetur, adipiscing.

.. raw:: latex

    \newpage
    \osiacenternextsection

Foreword
--------

Agentic AI systems now act as autonomous entities capable of reasoning, planning, and
executing tasks across services, infrastructures, and organizational boundaries. This
fundamentally changes the nature of identity in digital systems: identity is no longer
limited to human users and static machine instances but must also encompass autonomous,
dynamic, and goal-oriented agents. And identity alone is insufficient — the core question
extends beyond "what an entity is" to "whether, and under what conditions, that entity
should be trusted to act".

The Focus Group on Trust and Identity for humans and agentic AI (FG-TIDA) addresses trust
management and interoperable digital identity infrastructure for humans and for agentic AI,
supporting the development of secure, trustworthy digital ecosystems in which humans and
agentic AI can safely interact and collaborate.

FG-TIDA was established under Recommendation ITU-T A.7 (Focus groups: Establishment and
working procedures), with ITU-T Study Group 17 as its parent group. Further details are
available in the group's terms of reference.

For more news and updates about the TIDA Community, including its supporter organizations,
please refer to the community's published resources.

.. raw:: latex

    \osiacenternextsection

Note
----

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
deserunt mollit anim id est laborum. Sed ut perspiciatis unde omnis iste natus error sit
voluptatem accusantium doloremque laudantium.

.. Intellectual Property Rights — section commented out. To restore it, remove the
   leading ".." and the indentation below, and re-add a ".. raw:: latex" block with
   "\osiacenternextsection" before the heading (to centre it on the PDF).

   Intellectual Property Rights
   ----------------------------

   ITU draws attention to the possibility that the practice or implementation of this
   Recommendation may involve the use of a claimed Intellectual Property Right. ITU takes no
   position concerning the evidence, validity or applicability of claimed Intellectual Property
   Rights, whether asserted by ITU members or others outside of the Recommendation development
   process.

   As of the date of approval of this Recommendation, ITU had not received notice of intellectual
   property, protected by patents/software copyrights, which may be required to implement this
   Recommendation. However, implementers are cautioned that this may not represent the latest
   information and are therefore strongly urged to consult the appropriate ITU-T databases
   available via the ITU-T website at http://www.itu.int/ITU-T/ipr/.
   Implementers should also be aware that the organization that originated the technically
   equivalent document listed in the Bibliography may have received notices of intellectual
   property required for the implementation of this Recommendation.

.. raw:: latex

    %% Copyright notice commented out. To restore, uncomment the lines below.
    %% \vspace{4em}
    %% \begin{center}\textcopyright{} ITU 2024\end{center}
    %%
    %% \medskip
    %% All rights reserved. No part of this publication may be reproduced, by any means whatsoever, without the
    %% prior written permission of ITU.

    %% Restore \addcontentsline so the TOC below (and Chapter 1 onward) populate.
    \let\addcontentsline\osiaorigaddcontentsline
    \sphinxtableofcontents
    \osiamainmatter

.. toctree::
    :maxdepth: 3
    :numbered:
    :hidden:

    chapters/01_chapter1
    chapters/02_chapter2
    chapters/03_chapter3
    chapters/04_chapter4/index
    chapters/05_annex/index
    chapters/06_appendix/index
    chapters/07_references
