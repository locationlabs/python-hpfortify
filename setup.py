#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '0.1'

__build__ = ''

setup(name='hpfortify',
      version=__version__ + __build__,
      description='Python HPfority api client',
      author='Location Labs',
      author_email='info@locationlabs.com',
      url='http://www.locationlabs.com',
      packages=find_packages(exclude=['*.tests']),
      setup_requires=[
          'nose>=1.0'
      ],
      install_requires=[
          'click==5.1',
          'enum34>=1.0.4',
      ],
      tests_require=[
          'mock==1.0.1',
          'coverage',
      ],
      test_suite='hpfortify.tests',
      entry_points={
          'console_scripts': [
              'start-static-scan = hpfortify.cmd.client:start_static_scan',
          ],
      },
      )
