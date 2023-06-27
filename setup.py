from setuptools import find_packages, setup
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='py-pdf-search',
    packages=find_packages(include=["langchain[all]","pypdf","openai", "tiktoken"]),
     long_description=long_description,
     long_description_content_type="text/markdown",
    version='0.1.0',
    description='A Python library for searching PDFs',
    author='Jacob Somer',
    license='MIT',
)