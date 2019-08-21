"""
    sphinxcontrib.swaggerui
    ~~~~~~~~~~~~~~~~~~~~~~~

    Provides the swaggerui directive for reST files to build an interactive Swagger-UI based HTML page with
    your specification document in the OpenAPI format.

    :copyright: Copyright 2019 by Albert Bagdasaryan <albert.bagd@gmail.com>
    :license: BSD, see LICENSE for details.
"""

import pbr.version
from sphinxcontrib.swaggerui import swaggerui

if False:
    # For type annotations
    from typing import Any, Dict  # noqa
    from sphinx.application import Sphinx  # noqa

__version__ = pbr.version.VersionInfo(
    'swaggerui').version_string()


def setup(app):
    # type: (Sphinx) -> Dict[unicode, Any]
    app.add_directive('swaggerui', swaggerui.SwaggeruiDirective)
    return {'version': __version__, 'parallel_read_safe': True}
