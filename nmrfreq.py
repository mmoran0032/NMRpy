#!/usr/bin/env python
# nmrfreq - NMR frequency calculator


# Version numbering follows Semantic Versioning (http://semver.org/)
versionNum = "1.0.0"
versionDate = "2015-03-31"

from include.Driver import Driver
import share.config as config
from share.masstable import table

import sys


def main():
  D = Driver(config,
                    table,
                    "{0} ({1})".format(versionNum, versionDate))
  D.drive(" ".join(sys.argv[1:]))


if __name__ == "__main__":
  main()
