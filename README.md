Provides the swaggerui directive for reST files to build an interactive driven by Swagger-UI panel presenting
your OpenAPI specification document.

---

## Sphinx Directive swaggerui

When using for the first time, the following sample shows the configura:

.. swaggerui:: ../_static/swagger/petstore.yaml                                 # *) Required
   :url: https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js               # *) Required
   :css: ../_static/swagger/swagger-ui.css                                      # *) Required
   :script: https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js # Optional

An attribute (for example, ../_static/swagger/petstore.yaml) refers to your local YUML or JSON file in
the OpenAPI format.

The directive uses the following options:

*   ``url`` refers to a CDN-based (Content Delivery Network) Swagger-UI package.
*   ``css`` refers to a local Swagger-UI CSS file. This package contains a CSS file copied to the ``_static/swagger``
    folder during the first activation of the extension by Sphinx.
*   ``script`` refers to the additional script (the one in the above example is recommended).
