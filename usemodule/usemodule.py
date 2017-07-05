#!/usr/bin/env python

from __future__ import division
from __future__ import print_function

import json
import sys
import os

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
    
