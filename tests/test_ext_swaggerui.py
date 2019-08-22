"""
    test_ext_swaggerui
    ~~~~~~~~~~~~~~~~~~
    Test sphinx.ext.swaggerui extension.
    :copyright: Copyright 2019 by the Sphinx team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""
import os

import pytest
import re

@pytest.mark.sphinx('html', testroot='ext-swaggerui')
def test_swaggerui_html(app, status, warning):
    app.builder.build_all()

    swaggerui_dom = r'<div id="swagger-ui"></div>'
    spec = r'url: ".*?_static/swaggerui/petstore.yaml"'
    css = r'<link rel="stylesheet" href=".*?_static/swaggerui/swagger-ui.css" type="text/css" />'
    url = r'<script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"></script>'
    script = r'<script src="https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js"></script>'

    for path in ['index.html', 'sw/index.html']:
        content = (app.outdir / path).text()

        for pattern in [swaggerui_dom, css, spec, url, script]:
            assert re.search(pattern, content, re.S)


@pytest.mark.sphinx('html', testroot='ext-swaggerui')
def test_swaggerui_custom_html(app, status, warning):
    app.builder.build_all()

    swaggerui_dom = r'<div id="swagger-ui"></div>'
    spec = r'url: "\.\./_static/swaggerui/api-spec.yaml"'
    css = r'<link rel="stylesheet" href="\.\./_static/swaggerui/sw-ui.css" type="text/css" />'
    url = r'<script src="https://unpkg.com/swagger-ui-dist@3.23.5/swagger-ui-bundle.js"></script>'
    script = r'<script src="https://unpkg.com/swagger-ui-dist@3.23.5/swagger-ui-standalone-preset.js"></script>'

    path = (app.outdir / 'sw/custom.html')
    content = path.text()

    for pattern in [swaggerui_dom, css, spec, url, script]:
        assert re.search(pattern, content, re.S)

    dir_path = (app.outdir / 'sw')
    assert os.path.isfile(dir_path / '../_static/swaggerui/api-spec.yaml')
    assert os.path.isfile(dir_path / '../_static/swaggerui/sw-ui.css')
