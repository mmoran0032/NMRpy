#!/usr/bin/env python
# nmrfreq - NMR frequency calculator


import sys

from include.driver import Driver
import share.config as config
from share.masstable import table

# Version numbering follows Semantic Versioning (http://semver.org/)
versionNum = "1.1.3"
versionDate = "2015-11-12"


def main():
    D = Driver(config, table, "{0} ({1})".format(versionNum, versionDate))
    if len(sys.argv) == 1:
        sys.argv.append("-h")
    D.drive(sys.argv[1:])


if __name__ == "__main__":
    main()
