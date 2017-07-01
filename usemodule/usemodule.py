#!/usr/bin/env python

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
    from urllib import __version__ as urllib_version

class UseApi(object):


    
    def __init__(self, base_url=None, debugHTTP=False):
		
		if base_url is None:
            self.base_url = 'localhost
        else:
            self.base_url = base_url

       
        if debugHTTP:
            import logging
            import http.client

            http.client.HTTPConnection.debuglevel = 1

            logging.basicConfig()  # you need to initialize logging, otherwise you will not see anything from requests
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("requests.packages.urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
		
	@property
	def content(self):
		if not self._content:
			print("the content...")
			self._content = urlopen(self.url).read()        
		return self._content 
    
    
