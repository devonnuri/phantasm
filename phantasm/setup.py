#!/usr/bin/env python
from setuptools import setup
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, '../README.txt'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='phantasm',
    version='1.1.4',
    description='WebAssembly Disassembler',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='devonnuri',
    author_email='devonnuri@gmail.com',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='webassembly',
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4',
    install_requires=['construct'],
)
