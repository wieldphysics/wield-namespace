#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-License-Identifier: Apache-2.0
# SPDX-FileCopyrightText: © 2021 Massachusetts Institute of Technology.
# SPDX-FileCopyrightText: © 2021 Lee McCuller <mcculler@mit.edu>
# NOTICE: authors should document their contributions in concisely in NOTICE
# with details inline in source files, comments, and docstrings.
"""
"""

version_info = (0, 0, 2, 'dev0')
version = '.'.join(str(v) for v in version_info)
__version__ = version

# this section of code is removed in "release" branch versions
__version__ = __version__ + '.git-???'
try:
    import setuptools_scm
    print("SCM", setuptools_scm.get_version())
    __version__ = setuptools_scm.get_version(fallback_version=__version__)
# FIXME: fallback_version is not available in the buster version
# (3.2.0-1)
except (ModuleNotFoundError, TypeError, LookupError):
    pass
