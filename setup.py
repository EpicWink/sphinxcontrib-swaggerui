#!/usr/bin/env python

import setuptools


setuptools.setup(
    name="sphinxcontrib-swaggerui",
    version="0.0.3",
    description="Provides the swaggerui directive for reST files to build an interactive HTML page with your OpenAPI specification document.",
    long_description="README.md",
    license='BSD',
    author="Albert Bagdasaryan",
    author_email="albert.bagd@gmail.com",
    packages=setuptools.find_packages(),
    include_package_data=True,
    url="https://bitbucket.org/albert_bagdasaryan/sphinxcontrib-swaggerui/",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Framework :: Sphinx :: Extension",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Documentation",
        "Topic :: Utilities"
    ],
    namespace_packages=['sphinxcontrib'],
)
