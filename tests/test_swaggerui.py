"""
    tests.test_openapi
    ------------------

    Tests certain stuff of ``sphinxcontrib.swaggerui`` Sphinx extension.

    :copyright: (c) 2019, Albert Bagdasaryan.
    :license: BSD, see LICENSE for details.
"""


def test_functional(tmpdir, run_sphinx):


    spec = '_static/swaggerui/petstore.yaml'

    run_sphinx(spec, options={
        'url': 'https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js',
        'css': '_static/swaggerui/swagger-ui.css',
        'script': 'https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js'
    })

    rendered_html = tmpdir.join('out', 'index.html').read_text('utf-8')

    assert '<div id="swagger-ui"></div>' in rendered_html

