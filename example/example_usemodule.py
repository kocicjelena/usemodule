#!/usr/bin/env python

import os
import sys
import usemodule


'''Usage: call User as one instance'''


def main():
    api = usemodule.User()
	print (api('firstuser'))


if __name__ == "__main__":
    main()
