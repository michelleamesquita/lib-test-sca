#!/usr/bin/env python

from setuptools import setup
import pathlib

import pkg_resources

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name='lib-test-sca',
    version='1.0',
    description='Project example for building Python project with JFrog products',
    author='michelleamesquita',
    author_email='jfrog@jfrog.com',
    url='michelleamesquita/lib-test-sca',
    install_requires=install_requires
    #install_requires=['PyYAML>3.11', 'nltk'],
)
