# coding=utf-8
from setuptools import setup

setup(
    name='mathemlib',
    version='0.0.1',
    packages=['mathemlib'],
    url='https://github.com/peerster/mathemlib.git',
    license='MIT',
    author='Pär Berge',
    author_email='paer.berge@gmail.com',
    description='A python library for https://mathem.se',
    install_requires=['beautifulsoup4', 'requests', 'PyYAML'],
)
