#!/usr/bin/env python
# nmrfreq - NMR frequency calculator


import sys

import nmrfreq
from nmrfreq.driver import Driver
from nmrfreq.masstable import table


def main():
    version = "{} ({})".format(nmrfreq.__version__, nmrfreq.__date__)
    D = Driver(table, version)
    D.drive()


if __name__ == "__main__":
    main()
