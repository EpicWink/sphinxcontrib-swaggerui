"""
    tests.test_openapi
    ------------------

    Tests certain stuff of ``sphinxcontrib.swaggerui`` Sphinx extension.

    :copyright: (c) 2019, Albert Bagdasaryan.
    :license: BSD, see LICENSE for details.
"""

import pytest

from sphinxcontrib.swaggerui import swaggerui

@pytest.mark.sphinx
class TestSwaggerUI(object):

    def test_basic(self):
        pass
