

import os
from setuptools import setup
import sys

import nmrfreq


def getReadme(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name="nmrfreq",
    version=nmrfreq.__version__,
    license="MIT",
    description="NMR frequency determiner for the NSL",
    long_description=getReadme("README.md"),
    author="Mike Moran",
    author_email="mmoran9@nd.edu",
    install_requires=(["argparse"] if sys.version_info < (2, 7) else []),
    packages=["nmrfreq"],
    entry_points={"console_scripts": ["nmrfreq = nmrfreq.__main__:main"]}
)
