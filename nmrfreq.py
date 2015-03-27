#!/usr/bin/env python
# nmrfreq - NMR frequency calculator


# Version numbering follows Semantic Versioning (http://semver.org/)
versionNum = "0.9.99"
versionDate = "2015-XX-XX"

import include.Driver as Driver
import include.Isotope as Isotope
import include.NMRcalc as NMRcalc
import share.config as config
from share.masstable import table

import sys


def main():
  D = Driver.Driver(config,
                    table,
                    "{0} ({1})".format(versionNum, versionDate))
  D.parseArguments(" ".join(sys.argv[1:]))
  D.createIsotope()
  print(D.isotope)


if __name__ == "__main__":
  main()
