"""Setup file."""

# external imports
from setuptools import setup

# long description
with open("README.md", 'r') as f:
    long_description = f.read()

# requirements
requirements = ['pocha']

setup(
    name='hitos-iv',
    version='0.2',
    description='A JSON reader module',
    long_description=long_description,
    license="GPLv3",
    author='Luis Liñán',
    author_email='luislivilla@gmail.com',
    url="https://github.com/lulivi/hitos-iv",
    install_requires=requirements, )
