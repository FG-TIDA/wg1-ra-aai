.. This page is a reusable pattern for documenting one API interface. To add
   another interface: copy this file, change the heading and the label above it,
   and repoint every "../../yaml/example.yaml" at your own OpenAPI file. Then
   list the new page in this folder's index.rst. The directives below do the rest:
     openapi:version  -> prints the version from the file's info.version
     openapi:toc      -> a floating box listing the operations
     openapi           -> the full generated reference (endpoints, schemas, examples)

Example Interface
-----------------

This is version :openapi:version:`../../yaml/example.yaml` of this interface.

.. only:: html

    Get the OpenAPI file: `example.yaml <../../example.yaml>`_

.. raw:: latex

    Get the OpenAPI file: \textattachfile[]{../html/example.yaml}{example.yaml}

.. sidebar:: Operations

    .. openapi:toc:: ../../yaml/example.yaml
        :nb_columns: 1

Services
""""""""
.. openapi:: ../../yaml/example.yaml
    :examples:
    :group:
    :group_examples:
