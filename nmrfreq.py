#!/usr/bin/env python
# nmrfreq - NMR frequency calculator


import share.config as config
from include.Driver import Driver
from share.masstable import table

import sys

# Version numbering follows Semantic Versioning (http://semver.org/)
versionNum = "1.1.1"
versionDate = "2015-07-29"


def main():
  D = Driver(config, table, "{0} ({1})".format(versionNum, versionDate))
  if len(sys.argv) == 1:
    sys.argv.append("-h")
  D.drive(sys.argv[1:])


if __name__ == "__main__":
  main()
