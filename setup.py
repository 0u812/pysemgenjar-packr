#! /usr/bin/env python

from setuptools import setup

setup(name='pysemgenjar-packr',
      version='0.1.2',
      description='Jar file and embedded openjdk for pysemgen',
      author='J. Kyle Medley',
      packages=['semgenjar'],
      include_package_data=True,
      package_data={'semgenjar': [
          'semgenapi',
          'SemSimAPI.jar',
          'jre/*',
          'jre/**/*',
      ]},
      install_requires=[
        #'tellurium>=2.1.0',
        ],
      )
