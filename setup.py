from setuptools import setup

with open('README.md') as file:
    long_desc = file.read()

setup(
    name = 'threetotheonehalfpy',
    version = '1.0.1',
    author = 'funtrix_doesstuff',
    description = 'A Python package for rapid and secure calculation of three to the one half in an industrial environment',
    url = 'https://github.com/funtrix-ds1/threetotheonehalfpy',
    long_description = long_desc,
    long_description_content_type = 'text/markdown'
    )