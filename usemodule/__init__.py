#!/usr/bin/env python
#
# vim: sw=2 ts=2 sts=2
#
# Copyright 2017
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A library that provides a Python interface to the use API"""
from __future__ import absolute_import

__author__       = 'kocicjelena'
__email__        = 'kocicjelena@gmail.com'
__copyright__    = 'Copyright (c) 2017'
__license__      = 'Apache License 2.0'
__version__      = '0.1'
__url__          = 'https://github.com/kocicjelena/useapi'
__download_url__ = 'https://pypi.python.org/pypi/useapi'
__description__  = 'A Python wrapper around the use API'


import json                              

try:
    from hashlib import md5                 
except ImportError:
    from md5 import md5                   
from .usemodule import UseApi                        
