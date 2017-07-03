#!/usr/bin/env python

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
from .usemodule import *                    
