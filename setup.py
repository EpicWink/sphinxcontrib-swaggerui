#!/usr/bin/env python

import setuptools


setuptools.setup(
    name="sphinxcontrib-swaggerui",
    version="0.0.1",
    description="Provides the swaggerui directive for reST files to build an interactive HTML page with your OpenAPI specification document.",
    long_description="README.md",
    author="Albert Bagdasaryan",
    author_email="albert.bagd@gmail.com",
    url="http://www.sphinx-doc.org/",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Framework :: Sphinx :: Extension",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Documentation",
        "Topic :: Utilities"
    ],
    setup_requires=['pbr'],
)
