"""Setup file."""

# external imports
from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
   name='hitos-iv',
   version='0.2',
   description='A JSON reader module',
   license="GPLv3",
   long_description=long_description,
   author='Luis Liñán',
   author_email='luislivilla@gmail.com',
   url="https://github.com/lulivi/hitos-iv",
   install_requires=['unittest', 'json'],
)
