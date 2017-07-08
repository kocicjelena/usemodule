#!/usr/bin/env python

from __future__ import division
from __future__ import print_function

import json
import sys
import os

class User(object):
    
	def __call__(self, username, function):
		
		self.username=username
		self.fget = function
	def __get__(self, username):
		value = self.fget(username)
		setattr(username, self.fget.__name__, value)
		return value		
        
class UserVer(User):
    def __call__(self, username):
        super(UserVer, self).__call__(username)  


    
