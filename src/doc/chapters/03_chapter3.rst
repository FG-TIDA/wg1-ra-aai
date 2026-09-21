
.. _chapter3:

============================
Organising a large document
============================

As a specification grows, you will want to split it across several source files.
Sphinx offers two mechanisms, and they produce **different results in the
navigation sidebar** — so it matters which you choose.

toctree
-------

A ``toctree`` links to other files as *separate pages*, each with its own entry
in the navigation sidebar. This is how the chapters of this document are joined
together (see ``index.rst``).

You write it like this, listing each sub-page (without the ``.rst`` extension):

.. code-block:: rst

    .. toctree::

        _part1
        _part2

Each listed file becomes its own page. In the sidebar, the parent gets an
**expand arrow** and the sub-pages appear nested beneath it. The reader clicks
through to a separate page for each part.

include
-------

An ``include`` pastes another file's content directly into the current page, as
if you had typed it there. The result is a **single continuous page** with no
extra sidebar entries and no expand arrow.

You write it like this, giving the path to each fragment:

.. code-block:: rst

    .. include:: _part1.rst

    .. include:: _part2.rst

Use it to break one long chapter into smaller source files — for example, so
several authors can edit different parts without touching the same file — while
the reader still sees one seamless chapter.

Two rules keep includes working:

- **Name included fragments with a leading underscore** (for example
  ``_part1.rst``) so the build skips them as standalone pages.
- **Demote the headings inside a fragment by one level.** The chapter title uses
  ``=`` underlines; a heading inside an included fragment must use ``-`` so it
  becomes a *section* of the chapter rather than a new chapter of its own.

Which to use
------------

.. important::

    Because the two approaches look different in the sidebar, mixing them makes
    the navigation inconsistent. **Pick one and use it throughout your
    document.** This template recommends the ``include`` approach: it keeps each
    chapter on a single page with a clean, uniform sidebar, and lets you still
    split the source into manageable files. Chapters 4, 5 and 6 of this template
    are all built with ``include``.

.. tip::

    A change to an *included* file does not always trigger a rebuild of the page
    that includes it. If an edit does not appear, rebuild fully — the project
    ``HOWTO`` explains how, and the live-preview helper is already configured to
    do this for you.
