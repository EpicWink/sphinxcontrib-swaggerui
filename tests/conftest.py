"""
    pytest config for sphinxcontrib/swaggerui/tests
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: Copyright 2019 by Albert Bagdasaryan <albert.bagd@gmail.com>
    :license: BSD, see LICENSE for details.
"""

pytest_plugins = 'sphinx.testing.fixtures'

### Copied from sphinx/tests/conftest.py:

import os
import shutil

import docutils
import pytest

import sphinx
from sphinx.testing.path import path
from sphinx.testing import comparer

@pytest.fixture(scope='session')
def rootdir():
    return path(__file__).parent.abspath() / 'roots'
