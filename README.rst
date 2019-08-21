sphinxcontrib-swaggerui
#######################

.. image:: https://travis-ci.org/sphinx-contrib/sphinxcontrib-swaggerui.svg?branch=master
   :target: https://travis-ci.org/sphinx-contrib/sphinxcontrib-swaggerui

Provides the ``swaggerui`` directive for reST files to build an interactive driven
by `Swagger-UI <https://swagger.io/tools/swagger-ui/>`_ panel presenting
your `OpenAPI <https://swagger.io/resources/open-api>`_ specification document.

Overview
========

This Sphinx extension is necessary for those who publish an interactive document presenting their API specification
compliant with OpenAPI and want to use the well-known Swagger-UI tool for this purpose.
The ``swaggerui`` directive enables you to embed such interactive panel in an arbitrary place of an reST file.

Sphinx Directive swaggerui
==========================

Installation
------------

.. code-block:: text

   $ pip install sphinxcontrib-swaggerui

Configuration
-------------

In your Sphinx project configuration file ``config.py``, add the installed extension::

    extensions = [...,
        'sphinxcontrib.swaggerui',
        ...]

The directive also implies that you use the static content in the **_static/** folder and this is configured as::

    html_static_path = ['_static']


Directive in reST Files
-----------------------

Use the following sample configuration when testing the directive for the first time::

    .. swaggerui:: ../_static/swagger/petstore.yaml                                 # *) Required
       :url: https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js               # *) Required
       :css: ../_static/swagger/swagger-ui.css                                      # *) Required
       :script: https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js # Optional

An attribute (for example, ``../_static/swagger/petstore.yaml``) refers to your local YAML or JSON file in
the OpenAPI format. The path must be relative to the document containing the directive.

The directive uses the following options:

*  ``url`` refers to a CDN-based (Content Delivery Network) Swagger-UI package.
*  ``css`` refers to a local Swagger-UI CSS file. The path must be relative to the document containing the directive.
*  ``script`` refers to an additional script (the one in the above example is recommended).

.. note:: This package contains ``petstore.yaml`` and ``swagger-ui.css`` files (mentioned in the above example)
   copied to the ``_static/swaggerui/`` folder during the first use of the directive by Sphinx.
   So don't care about copying these files when you specify the relative path to that folder;
   the sample files will appear automatically in it whether you use them or not.


Links
=====

- Source: `Bitbucket <https://bitbucket.org/albert_bagdasaryan/sphinxcontrib-swaggerui/>`_
- Bugs and issues: `Issues <https://github.com/sphinx-contrib/sphinxcontrib-swaggerui/issues>`_
