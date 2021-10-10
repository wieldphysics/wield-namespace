#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: © 2021 Massachusetts Institute of Technology.
# SPDX-FileCopyrightText: © 2021 Lee McCuller <mcculler@mit.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.
""" Setup and build the wavestate.collection package, which acts as the metapackage

Packaging guidance may be found at https://packaging.python.org/tutorials/packaging-projects/
"""
import sys
import os
from setuptools import find_packages, setup

# this is a fix for running within the pypa build package
# it ensures that only the local setup_helper is imported
# it preprends this file's path to the import path
sys.path[0:0] = [os.path.dirname(os.path.abspath(__file__))]
import setup_helper  # noqa

version = '0.0.1'

# this adjusts the setuptools builder to check the internal version against
# the package version as well as the current git tag, to ensure consistency.
# watch for warnings during the build. This mechanism does not prevent
# building packages
cmdclass = setup_helper.version_checker(version, 'wavestate.collection')

# Settings are primarily in setup.cfg
setup(
    version          = version,
    packages         = find_packages(exclude = ['docs']),
    install_requires = [],
    extras_require   = {},
    tests_require    = ['pytest'],
    test_suite       = 'pytest',
    cmdclass         = cmdclass,
    zip_safe         = True,
)

