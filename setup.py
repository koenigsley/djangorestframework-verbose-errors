#!/usr/bin/env python3
import os

from setuptools import setup

from rest_framework_verbose_errors import __version__

with open('README.md') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    install_requires = f.read().strip().split(os.linesep)

setup(
    name='djangorestframework-verbose-errors',
    version=__version__,
    license='MIT',
    description='A simple package for DRF errors formatting',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Mikhail Yeremeyev',
    author_email='koenigsley@gmail.com',
    url='https://github.com/koenigsley/djangorestframework-verbose-errors',
    packages=['rest_framework_verbose_errors'],
    python_requires='>=3.6',
    install_requires=install_requires,
)
