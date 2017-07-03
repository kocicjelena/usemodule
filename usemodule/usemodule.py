#!/usr/bin/env python

from __future__ import division
from __future__ import print_function

import json
import sys
import gzip
import time
import base64
import re
import requests
from requests_oauthlib import OAuth1
import io
import warnings
from uuid import uuid4
import os

try:
    # python 3
    from urllib.parse import urlparse, urlunparse, urlencode
    from urllib.request import urlopen
    from urllib.request import __version__ as urllib_version
except ImportError:
    from urlparse import urlparse, urlunparse
    from urllib2 import urlopen
    from urllib import urlencode


class InitOnAccess:
    def __init__(self, method, *args, **kwargs):
        self.method = method
        self.method_name = method.__name__
        self.args = args
        self.kwargs = kwargs
        self._hosted = None

    def __get__(self, obj, cls):
        if not self._hosted:
            print('hosted')
            self._hosted = self.method(*self.args, **self.kwargs)
        else:
            print('cached!')
        return self._hosted




class UseModule():
	super().__init__(self, base_url=None, *args, **kwargs)
	if base_url is None:
		self.base_url = 'localhost'
	else:
		self.base_url = base_url

    def content(self):
		if not self._content:
			print("the content...")
			self._content = urlopen(self.base_url).read()        
		return self._content    
		
class MethodClass:
    def reset(self):
        self.base_url = ''


class UseModuleUser(object):
    def __init__(self, function):
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj or cls)
        setattr(cls, self.fget.__name__, value)
        return value

class MyModuleModule:

    @UseModuleUser
    def modulise(self):
        print("modulise!")
        return val
    
