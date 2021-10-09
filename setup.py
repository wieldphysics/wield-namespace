#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
# Copyright: 2021 Massachusetts Institute of Technology.
# Copyright: 2021 Lee McCuller <mcculler@mit.edu>
# NOTICE: Contributors should add their name to copyright and document their contributions in NOTICE
""" Setup and build the wavestate.collection package, which acts as the metapackage
"""
from setuptools import find_packages, setup
import setup_helper

# Packaging guidance may be found at https://packaging.python.org/tutorials/packaging-projects/

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

