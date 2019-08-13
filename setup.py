#!/usr/bin/env python3
import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 7):
    sys.exit("Unsupported Python version (use 3.7)")

install_requires = [
    "jinja2",
]

setup(
    name="j2scr",
    version="1.0.0",
    license="LGPLv3+",
    packages=find_packages(),
    install_requires=install_requires,
)
