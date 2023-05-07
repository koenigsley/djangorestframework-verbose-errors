#!/usr/bin/env python3
from setuptools import setup

from rest_framework_verbose_errors import __version__

setup(
    name='djangorestframework-verbose-errors',
    version=__version__,
    license='MIT',
    description='A simple package for DRF errors formatting',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mikhail Yeremeyev',
    author_email='koenigsley@gmail.com',
    url='https://github.com/koenigsley/djangorestframework-verbose-errors',
    packages=['rest_framework_verbose_errors'],
)
