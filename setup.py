#!/usr/bin/env python
from distutils.core import setup


with open('README.rst') as f:
    readme = f.read()


setup(
    name='SimpleUpload',
    version='0.0.2',
    description='Upload file via HTTP.',
    long_description=readme,
    packages=['simple_upload'],
    url='https://github.com/codeif/SimpleUpload',
    license='MIT',
    author='codeif',
    author_email='me@codeif.com',
    install_requires=['Flask']
)
