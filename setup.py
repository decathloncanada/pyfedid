#!/usr/bin/env python

from setuptools import setup, find_packages


setup(name='pyfedid',
      version='1.0.0',
      plateformes='UNIX',
      description='Package for Decathlon FEDID',
      packages=find_packages(),
      packages_dir={'': 'pyfedid'},
      author='Sylvain Lemoine',
      author_email='sylvain.lemoine@decathlon.com',
      url='https://github.com/decathloncanada/pyfedid',
      download_url='https://github.com/decathloncanada/pyfedid',
      license='GPL Version 3',
      zip_safe=False,
      long_description=open('README.md').read())
