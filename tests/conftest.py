"""
    pytest config for sphinxcontrib/swaggerui/tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2019 by Albert Bagdasaryan <albert.bagd@gmail.com>
    :license: BSD, see LICENSE for details.
"""


from sphinx.application import Sphinx
from sphinx.testing.path import path
import textwrap
import pytest

pytest_plugins = 'sphinx.testing.fixtures'

@pytest.fixture(scope='session')
def rootdir():
    return path(__file__).parent.abspath() / 'roots'

def _format_option_raw(key, val):
    if isinstance(val, bool) and val:
        return ':%s:' % key
    return ':%s: %s' % (key, val)


@pytest.fixture(scope='function')
def run_sphinx(tmpdir):
    src = tmpdir.ensure('src', dir=True)
    out = tmpdir.ensure('out', dir=True)

    def run(spec, options={}):
        options_raw = '\n'.join([
            '   %s' % _format_option_raw(key, val)
            for key, val in options.items()])

        src.join('conf.py').write_text(
            textwrap.dedent('''
                import os

                project = 'sphinxcontrib-swaggerui'
                copyright = '2019, Albert Bagdasaryan'

                extensions = ['sphinxcontrib.swaggerui']
                source_suffix = '.rst'
                master_doc = 'index'
            '''),
            encoding='utf-8')

        src.join('index.rst').write_text(
            '.. swaggerui:: %s\n%s' % (spec, options_raw),
            encoding='utf-8')

        Sphinx(
            srcdir=src.strpath,
            confdir=src.strpath,
            outdir=out.strpath,
            doctreedir=out.join('.doctrees').strpath,
            buildername='html'
        ).build()

    yield run

