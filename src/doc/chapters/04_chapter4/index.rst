
.. _chapter4:

Documenting an API
==================

This chapter demonstrates the template's most powerful feature: generating a
complete REST API reference automatically from an OpenAPI specification. You
write the API once, as a standard OpenAPI (Swagger) file, and the endpoints,
parameters, request and response schemas, and examples are rendered for you.

This is why the template is built on Sphinx rather than plain Markdown — no
Markdown toolchain offers this.

How it works
------------

#. Put your OpenAPI 3.0 file in the ``yaml/`` folder (see ``yaml/example.yaml``
   for a minimal, complete example you can copy).
#. Create one page per interface that points at the file (see
   ``chapter4/interface1.rst``). Copy it for each additional API.
#. List those pages in the ``toctree`` below so each gets its own page in the
   navigation sidebar.

The example interface on the next page is generated entirely from
``yaml/example.yaml`` — edit that file and the documentation follows.

.. include:: _interface1.rst
