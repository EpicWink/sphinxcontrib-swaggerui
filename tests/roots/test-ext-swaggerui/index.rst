.. Testing the SwaggerUI extension for Sphinx documentation master file, created by
   sphinx-quickstart on Wed Aug 21 10:52:39 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Testing the SwaggerUI extension for Sphinx's documentation!
======================================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   sw/index

Swagger-UI Directive
--------------------

.. swaggerui:: _static/swaggerui/petstore.yaml
   :url: https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js
   :css: _static/swaggerui/swagger-ui.css
   :script: https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
