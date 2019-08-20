"""
    sphinxcontrib.swaggerui
    ~~~~~~~~~~~~~~~~~~~~~~~

    Sphinx extension to embed the Swagger-UI generated OpenAPI specification document
    to the Restructured Text format.

    :copyright: (c) 2019 by Albert Bagdasaryan.
    :license: BSD, see LICENSE for details.

    Sample use:

    .. swaggerui:: ../_static/swagger/petstore.yaml                                 # *) Required
       :url: https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js               # *) Required
       :css: ../_static/swagger/swagger-ui.css                                      # *) Required
       :script: https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js # Optional
"""

import filecmp
import os
import shutil
import requests

from docutils import nodes
from docutils.parsers.rst import directives
from sphinx.errors import ExtensionError
from sphinx.util import relative_uri
from sphinx.util.docutils import SphinxDirective

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
SWAGGER_CACHE_DIR = '_static/swaggerui'  # relative to the doc root

# Default argument and options:
SPEC_PATH = SWAGGER_CACHE_DIR + "/petstore.yaml"
SWAGGER_URL = "https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"
OPT_SCRIPT = "https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js"
CSS_PATH = SWAGGER_CACHE_DIR + "/swagger-ui.css"

def copyfile(directive, source, dest):
    """Copy the source file if its copy does not exist on the the destination path
    or it's timestamp differs."""
    if not os.path.exists(source):
        raise ExtensionError('The source file "%s" specified in "%s", line "%s" does not exist.'
                             % (source, directive.env.doc2path(directive.name), directive.lineno))
    if not os.path.exists(dest) or not filecmp.cmp(source, dest):
        if not os.path.exists(SWAGGER_CACHE_DIR):
            os.makedirs(SWAGGER_CACHE_DIR)
        shutil.copyfile(source, dest)

def validate_url(directive, url):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError('The URL "%s" in the "%s" directive on line "%s" is not a valid URL.'
                         % (url, directive.name, directive.lineno))
    return url


class SwaggeruiDirective(SphinxDirective):
    required_arguments = 1          # Path to the Spec YAML file - first line, after ::
    optional_arguments = 0          # No more arguments allowed in the line after ::
    option_spec = {                 # Options marked with :option: <value> on the lines after the first line
        'url': directives.uri,      # URL of the Swagger-UI JavaScript file in a CDN
        'css': directives.path,     # (Required) Path to the CSS file
        'script': directives.unchanged
    }
    has_content = False

    def run(self, block_text=None):
        # Sphinx objects:
        env = self.env
        app = env.app
        builder = app.builder
        docname = env.docname
        node_list = []

        page_url = builder.get_target_uri(docname)      # The HTML page path relative to the HTML Doc root

        # Spec path processing - copy the Spec file to _static/{SWAGGER_CACHE_DIR}/:
        spec_relpath, spec_abspath = env.relfn2path(directives.path(self.arguments[0]))
        spec_path = SWAGGER_CACHE_DIR + "/%s" % os.path.basename(spec_relpath)
        copyfile(self, spec_relpath, spec_path)
        spec_path = relative_uri(page_url, spec_path)

        # CSS path processing - copy the CSS file to _static/{SWAGGER_CACHE_DIR}/:
        css_relpath, css_abspath = env.relfn2path(directives.path(self.options["css"]))
        css_path = SWAGGER_CACHE_DIR + "/%s" % os.path.basename(css_relpath)
        copyfile(self, css_relpath, css_path)
        css_path = relative_uri(page_url, css_path)

        # Swagger URL processing:
        swagger_url = validate_url(self, self.options["url"])

        # Optional script:
        opt_script = OPT_SCRIPT     # Default script if none is specified in the directive
        if "script" in self.options:
            opt_script = validate_url(self, self.options["script"])

        # Get the Window.Onload() function from the file and substitute the placeholders:
        with open(MODULE_DIR + "/content.txt") as f:
            text = f.read()
        text = text.replace('url: url', 'url: "%s"' % spec_path)\
            .replace('href=css-path', 'href="%s"' % css_path)\
            .replace('src=swagger-url', 'src="%s"' % swagger_url)\
            .replace('src=opt-script', 'src="%s"' % opt_script)

        raw_node = nodes.raw(text=text, format='html')
        (raw_node.source, raw_node.line) = self.state_machine.get_source_and_line(self.lineno)
        node_list.append(raw_node)
        return node_list
