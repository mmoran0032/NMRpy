#!/usr/bin/env python
# nmrfreq - NMR frequency calculator


import nmrfreq
from . import driver
from .masstable import table


def main():
    version = "{} ({})".format(nmrfreq.__version__, nmrfreq.__date__)
    D = driver.Driver(table, version)
    D.drive()


if __name__ == "__main__":
    main()
