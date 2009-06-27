#!/usr/bin/env python

from setuptools import *
setup(
	name='importwatcher',
	version='0.1.0',
	author_email='tim3d.junk+importwatcher@gmail.com',
	author='Tim Cuthbertson',
	url='http://github.com/gfxmonk/importwatcher',
	description="import watcher for python modules",
	long_description="import watcher for python modules",
	packages = find_packages(exclude=['test']),
	classifiers=[
		"License :: OSI Approved :: BSD License",
		"Programming Language :: Python",
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Libraries :: Python Modules",
	],
	keywords='import module modules monitor watcher difference reset',
	license='BSD',
	zip_safe=True,
	install_requires=[
		'setuptools',
	],
)
