#!/usr/bin/env python

import os
import sys
import useapi


USAGE = '''Usage: 

'''


def main():
    api = useapi.UseApi()
	print (api.content())


if __name__ == "__main__":
    main()
