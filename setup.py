#!/usr/bin/python

from setuptools import setup

setup(name='RedisConfigParser',
      version='0.0.1',
      description='A simple way to use redis as backend for python ConfigParser',
      author='Juliano Martinez',
      author_email='juliano@martinez.io',
      url='https://github.com/ncode/RedisConfigParser',
      install_requires=['redis','simplejson'],
      packages=['RedisConfigParser'],
     )
