#!/usr/bin/env python

from __future__ import division
from __future__ import print_function

import json
import sys
import os

class User(object):
    def __call__(self, username):
        self.username=username
        
class UserVer(User):
    def __call__(self, username):
        super(UserVer, self).__call__(username)  
        
class UseModuleUser(object):
    def __call__(self, function):
        self.fget = function

    def __get__(self, obj, cls):
        value = self.fget(obj or cls)
        setattr(cls, self.fget.__name__, value)
        return value

class MyModuleModule:

    @UseModuleUser
    def modulise(self):
        print("modulise!")
        return value
    
