#! /usr/bin/env python

from setuptools import setup

# https://stackoverflow.com/questions/27664504/how-to-add-package-data-recursively-in-python-setup-py
# compensating for python's worthless packaging system
import os

def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths

openjdk_files = package_files(os.path.join('semgenjar','jre'))
print('openjdk_files')
print(openjdk_files)

setup(name='pysemgenjar-packr',
      version='0.1.4',
      description='Jar file and embedded openjdk for pysemgen',
      author='J. Kyle Medley',
      packages=['semgenjar'],
      include_package_data=True,
      package_data={'semgenjar': [
          'semgenapi',
          'SemSimAPI.jar',
          'config.json',
          ]+openjdk_files},
      install_requires=[
        #'tellurium>=2.1.0',
        ],
      )
