
.. _chapter1:

Writing content
===============

.. note::

    This template is *self-documenting*: each chapter both explains and
    demonstrates a part of the authoring system. Read the rendered page to see
    what is possible, then open the matching ``.rst`` source file to see exactly
    how it was produced. Replace this instructional content with your own.

This chapter covers the everyday building blocks of a document: headings, text,
lists, links, cross-references, highlighted notes, and code. Chapter 2 covers
figures, tables and diagrams; Chapter 4 covers API reference documentation.

Headings and structure
----------------------

Headings define the structure of a chapter. A heading is a line of text with a
row of punctuation underneath it, at least as long as the text. The *character*
used sets the level:

* ``=`` for the chapter title (top level),
* ``-`` for a section (like this one),
* ``"`` for a subsection.

Subsection example
""""""""""""""""""

This is a subsection. Chapters are numbered automatically, so you never type
"1.2.3" yourself — Sphinx computes it from the heading levels and the order of
files.

Text styling
------------

Within a paragraph you can mark text as *italic* (one asterisk), **bold** (two
asterisks), or ``inline code`` / literal text (two backticks). Use inline code
for field names, values, and anything a reader should type verbatim, such as
``transactionId`` or ``application/json``.

Lists
-----

Use a bulleted list for items with no particular order:

* First point.
* Second point, which can wrap onto several lines and still belong to the same
  item as long as the following lines are indented to match.
* Third point.

Use a numbered list when order or count matters. Start every item with ``#.``
and the numbers are filled in for you:

#. Collect the input.
#. Validate it.
#. Produce the result.

A *definition list* pairs a term with its explanation — useful for glossaries or
parameter descriptions:

Term
    The explanation of the term, indented underneath it.

Another term
    Its explanation.

Links and cross-references
--------------------------

Link to an external site with the text and URL together, followed by an
underscore, like `the TIDA site <https://www.itu.int/>`_.

To point at another part of *this* document, give a target a label and refer to
it by name. This paragraph can, for example, send the reader to
:ref:`chapter2` — the link text and page number update automatically if the
target moves. Labels are defined with ``.. _name:`` immediately above a heading
(see the top of any chapter source file).

Highlighting: notes, warnings, tips
-----------------------------------

*Admonitions* draw the eye to something important. Several types are available,
each with its own colour and icon:

.. note::

    A note adds supporting information the reader should be aware of.

.. tip::

    A tip offers helpful, optional advice.

.. warning::

    A warning flags something that can cause errors or data loss.

.. important::

    An "important" box stresses a point that must not be missed.

Code and data samples
---------------------

Show code or data in a highlighted block. Name the language after
``.. code-block::`` to get syntax colouring — here, ``json``:

.. code-block:: json

    {
        "key": "value",
        "anotherKey": 23
    }

Requirement keywords
--------------------

Specifications rely on precise requirement language. The key words "MUST",
"MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT",
"RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as
described in `RFC 2119 <http://www.ietf.org/rfc/rfc2119.txt>`_.

Keep this section in your specification and use those words deliberately —
readers and implementers rely on their exact meaning.
