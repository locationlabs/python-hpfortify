#!/usr/bin/env python

from setuptools import setup, find_packages

__version__ = '0.1'

__build__ = ''

setup(name='pfortify-client',
      version=__version__ + __build__,
      description='Python HPfority api client',
      author='rakesh.kumar',
      author_email='rakeshcusat@gmail.com',
      url='http://www.code4reference.com',
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
          'mockredispy>=2.9.0.11',
          'coverage',
          'nose_parameterized>=0.5.0',
      ],
      test_suite='hpfortify.tests',
      entry_points={
          'console_scripts': [
              'start-static-scan = hpfortify.cmd.client:start_static_scan',
          ],
      },
      )
