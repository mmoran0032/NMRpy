

import os
from setuptools import setup
import sys


def getReadme(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


VERSION = "1.1.4"  # 2015-12-02
INSTALL_REQUIRES = (["argparse"] if sys.version_info < (2, 7) else [])


setup(
    name="nmrfreq",
    version=VERSION,
    license="MIT",
    description="NMR frequency determiner for the NSL",
    long_description=getReadme("README.md"),
    author="Mike Moran",
    author_email="mmoran9@nd.edu",
    install_requires=INSTALL_REQUIRES,
    packages=["nmrfreq"],
    entry_points={"console_scripts": ["nmrfreq = nmrfreq.__main__:main"]}
)
