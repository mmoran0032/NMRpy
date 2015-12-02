

import sys

import nmrfreq
from nmrfreq.driver import Driver
import nmrfreq.config as config
from nmrfreq.masstable import table

__version__ = "1.1.4"  # 2015-12-02


def main():
    D = Driver(config, table, __version__)
    D.drive()


if __name__ == "__main__":
    main()
