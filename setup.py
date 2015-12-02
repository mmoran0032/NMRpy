

from setuptools import setup
import sys


INSTALL_REQUIRES = (["argparse"] if sys.version_info < (2, 7) else [])

def version():
    with open("nmrfreq.py", "rU") as f:
        text = [line.strip() for line in f]
    for line in text:
        if line.startswith("__version__"):
             return line.split()[2]


setup(
    name="nmrfreq",
    version=version(),
    description="NMR frequency determiner for the NSL",
    author="Mike Moran",
    author_email="mmoran9@nd.edu",
    license="MIT",
    install_requires=INSTALL_REQUIRES,
    packages=["nmrfreq"],
    entry_points={"console_scripts": ["nmrfreq=nmrfreq.main"]}
)
