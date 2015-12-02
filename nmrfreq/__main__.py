#!/usr/bin/env python
# nmrfreq - NMR frequency calculator


import sys

from include.driver import Driver
import share.config as config
from share.masstable import table

# Version numbering follows Semantic Versioning (http://semver.org/)
__version__ = "1.1.3"  # 2015-11-12


def main():
    D = Driver(config, table, __version__)
    D.drive()


if __name__ == "__main__":
    main()
