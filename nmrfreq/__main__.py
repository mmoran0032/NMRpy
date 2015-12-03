#!/usr/bin/env python
# nmrfreq - NMR frequency calculator


import sys

import nmrfreq
from nmrfreq.driver import Driver
from nmrfreq.masstable import table


def main():
    D = Driver(table, nmrfreq.__version__)
    D.drive()


if __name__ == "__main__":
    main()
