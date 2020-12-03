#!/usr/bin/env python
# coding: utf-8

import os
import sys

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
	name='pyping',
	version='0.0.6',
	description='A pure python ICMP ping implementation using raw sockets',
	long_description=open('README.rst').read() + '\n\n' +
                     open('HISTORY.rst').read(),
	license=open("LICENSE").read(),
	author="toxinu",
	author_email="toxinu@gmail.com",
	url='https://github.com/toxinu/pyping/',
	keywords="ping icmp network latency",
	packages = ['pyping'],
	scripts=["bin/pyping"]
)
