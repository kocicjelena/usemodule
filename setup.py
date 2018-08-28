#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function

#
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import codecs

from setuptools import setup, find_packages
try:
    from pypandoc import convert

    def read_md(f):
        return convert(f, 'rst')

except ImportError:
    convert = None
    print(
        "warning: pypandoc module not found, could not convert Markdown to RST"
    )

    def read_md(f):
        return open(f, 'r').read()

README = os.path.join(os.path.dirname(__file__), 'README.md')

setup(
    name='usemm',
	long_description=read_md(README),
    packages=find_packages(),
	version='1.0',
    description='setup module',
    author='Jelena',
    author_email='kocicjelena@gmail.com',
	url='https://github.com/kocicjelena/usemodule/',
	platforms=['Any'],
    install_requires=['future', 'requests'],
    #setup_requires=['pytest-runner'],
    tests_require=['pytest3'],
    keywords='use api',
    scripts=['example/example_usemodule.py'],
    entry_points={
        'console_scripts': [
            'usemm = example_usemodule:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat',
        'Topic :: Internet',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
