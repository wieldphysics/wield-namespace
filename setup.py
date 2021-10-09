#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from setuptools import find_packages, setup
import setup_helper

version = '0.0.1'

cmdclass = setup_helper.version_checker(version, 'wavestate.collection')

setup(
    version          = version,
    packages         = find_packages(exclude = ['docs']),
    install_requires =[],
    extras_require   ={},
    tests_require=['pytest'],
    test_suite   = 'pytest',
    cmdclass         = cmdclass,
    zip_safe         = True,
)

