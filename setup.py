#!/usr/bin/env python
from setuptools import setup, find_packages


def load_long_description():
    with open("README.md", "r") as fh:
        long_description = fh.read()
    return long_description


setup(
    name='pesel',
    version='0.3.0',
    description='Polish PESEL',
    long_description=load_long_description(),
    long_description_content_type='text/markdown',
    author='Jakub Spórna <jakub.sporna@gmail.com>',
    author_email='jakub@sporna.dev',
    url='https://github.com/jsporna/pypesel',
    keywords=['pesel'],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    packages=find_packages(exclude=['tests*']),
    install_requires=[],
    entry_points={
        'console_scripts': ['pesel=pesel.main:cli']
    }
)
