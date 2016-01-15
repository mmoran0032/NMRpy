#!/usr/bin/env python
# nmrfreq - NMR frequency calculator


from . import __version__, __date__
from .driver import Driver
from .masstable import table


def main():
    version = "{} ({})".format(__version__, __date__)
    D = Driver(table, version)
    D.drive()


if __name__ == "__main__":
    main()
