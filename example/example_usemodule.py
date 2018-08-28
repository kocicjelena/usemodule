#!/usr/bin/env python

import os
import sys
import usemodule


'''Usage: call User as one instance print(api('firstuser', function1))'''
def main():
	api = usemodule.User()
	print(api("f", function1))

def function1():
	pass

if __name__ == "__main__":
    main()
