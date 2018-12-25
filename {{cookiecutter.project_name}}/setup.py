from setuptools import setup, find_packages

__version__ = '0.1-dev'

setup(
    name='{{cookiecutter.app_name}}',
    version=__version__,
    packages=find_packages(exclude='tests'),
    entry_points={'console_scripts': ['{{cookiecutter.app_name}} = {{cookiecutter.app_name}}.manage:cli']})
