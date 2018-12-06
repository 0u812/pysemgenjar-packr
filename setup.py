#! /usr/bin/env python

from setuptools import setup

setup(name='pysemgenjar-packr',
      version='0.1.3',
      description='Jar file and embedded openjdk for pysemgen',
      author='J. Kyle Medley',
      packages=['semgenjar'],
      include_package_data=True,
      package_data={'semgenjar': [
          'semgenapi',
          'SemSimAPI.jar',
          'config.json',
          'jre/*',
          'jre/**/*',
      ]},
      install_requires=[
        #'tellurium>=2.1.0',
        ],
      )
