"""
    sphinxcontrib.swaggerui
    ~~~~~~~~~~~~~~~~~~~~~~~

    Sphinx extension to embed the Swagger-UI generated OpenAPI specification document
    to the Restructured Text format.

    :copyright: (c) 2019 by Albert Bagdasaryan.
    :license: BSD, see LICENSE for details.

    Sample use:

    .. swaggerui:: ../_static/swaggerui/petstore.yaml                               # Required
       :url: https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js               # Required
       :css: ../_static/swaggerui/swagger-ui.css                                    # Required
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

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))     # Absolute path to the installed package
SWAGGER_CACHE_DIR = '_static/swaggerui'  # Relative to the folder with the static content

# Default argument and options:
DOM_NODE_ID = "swagger-ui"
SPEC_PATH = SWAGGER_CACHE_DIR + "/petstore.yaml"
SWAGGER_URL = "https://unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js"
OPT_SCRIPT = "https://unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js"
CSS_PATH = SWAGGER_CACHE_DIR + "/swagger-ui.css"
OPT_FILTER = ""

def copyfile(directive, source, dest):
    """Copy the source file if its copy does not exist on the the destination path
    or it's timestamp differs."""
    if not os.path.exists(source):
        raise ExtensionError('The source file "%s" specified in "%s", line "%s" does not exist.'
                             % (source, directive.env.doc2path(directive.env.docname), directive.lineno))
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
    required_arguments = 1              # Path to the Spec YAML file - first line, after ::
    optional_arguments = 0              # No more arguments allowed in the line after ::
    option_spec = {                     # Options marked with :option: <value> on the lines after the first line
        'url': directives.uri,          # (Required) URL of the Swagger-UI JavaScript file in a CDN
        'css': directives.path,         # (Required) Path to the CSS file
        'script': directives.unchanged, # Additional script: URL to the script in a CDN
        'filter': directives.unchanged  # Filter to select the content by tags
    }
    has_content = False

    def run(self, block_text=None):
        # Sphinx application objects:
        env = self.env
        app = env.app
        builder = app.builder
        docname = env.docname
        node_list = []
        srcdir = app.srcdir     # Absolute path to the reST documentation source.

        page_url = builder.get_target_uri(docname)      # The HTML page path relative to the HTML Doc root

        # Prepare default YAML and CSS files (if not exist):
        if not os.path.exists(srcdir + '/' + SWAGGER_CACHE_DIR):
            os.makedirs(srcdir + '/' + SWAGGER_CACHE_DIR)
        if (not os.path.isfile(srcdir + '/' + SPEC_PATH)):
            copyfile(self, MODULE_DIR + '/petstore.yaml', srcdir + '/' + SPEC_PATH)
        if (not os.path.isfile(srcdir + '/' + CSS_PATH)):
            copyfile(self, MODULE_DIR + '/swagger-ui.css', srcdir + '/' + CSS_PATH)

        # Spec path processing - copy the Spec file to SWAGGER_CACHE_DIR:
        spec_relpath, spec_abspath = env.relfn2path(directives.path(self.arguments[0]))
        # spec_path = SWAGGER_CACHE_DIR + "/%s" % os.path.basename(spec_relpath)
        copyfile(self, spec_abspath, srcdir + '/' + SWAGGER_CACHE_DIR + '/' + os.path.basename(spec_relpath))
        spec_path = relative_uri(page_url, SWAGGER_CACHE_DIR + '/' + os.path.basename(spec_relpath))

        # CSS path processing - copy the CSS file to _static/{SWAGGER_CACHE_DIR}/:
        css_relpath, css_abspath = env.relfn2path(directives.path(self.options["css"]))
        # css_path = SWAGGER_CACHE_DIR + "/%s" % os.path.basename(css_relpath)
        copyfile(self, css_abspath, srcdir + '/' + SWAGGER_CACHE_DIR + '/' + os.path.basename(css_relpath))
        css_path = relative_uri(page_url, SWAGGER_CACHE_DIR + '/' + os.path.basename(css_relpath))

        # Swagger URL processing:
        swagger_url = validate_url(self, self.options["url"])

        # Optional script:
        opt_script = OPT_SCRIPT     # Default script if none is specified in the directive
        if "script" in self.options:
            opt_script = validate_url(self, self.options["script"])

        # Optional filter:
        opt_filter = OPT_FILTER     # Default script if none is specified in the directive
        if "filter" in self.options:
            opt_filter = self.options["filter"]

        # Get the Window.Onload() function from the file and substitute the placeholders:
        with open(MODULE_DIR + "/content.txt") as f:
            text = f.read()

            text = text.replace('swagger-ui', DOM_NODE_ID + '-' + str(env.new_serialno()))\
                .replace('url: url', 'url: "%s"' % spec_path)\
                .replace('href=css-path', 'href="%s"' % css_path)\
                .replace('src=swagger-url', 'src="%s"' % swagger_url)\
                .replace('src=opt-script', 'src="%s"' % opt_script)\
                .replace('filter: true', 'filter: "%s"' % opt_filter)


        raw_node = nodes.raw(text=text, format='html')
        (raw_node.source, raw_node.line) = self.state_machine.get_source_and_line(self.lineno)
        node_list.append(raw_node)
        return node_list
