# Driver - command line interface for nmrfreq


import argparse
from Isotope import Isotope

desc = """NMRFREQ - analyzing magnet frequency utility for the NSL"""

class Driver(object):
  def __init__(self, isotope=None, config=None, calc=None):
    self.isotope = isotope
    self.config = config
    self.calc = calc
    self.parser = argparse.ArgumentParser(description=desc)
    self.defineUsage()


  def defineUsage(self):
    p = self.parser
    p.add_argument("-v", "--version", action="version",
                   version="nmrfreq 0.99.999.9999 (date)")
    p.add_argument("-i", "--iso", type=str, metavar="ISO", default="H1",
                   help="desired isotope name")
    p.add_argument("-q", "--charge", type=int, default=1,
                   help="selected charge state")
    g = p.add_mutually_exclusive_group()
    g.add_argument("-e", "--energy", type=float, nargs="*",
                   help="desired beam energy")
    g.add_argument("-f", "--frequency", type=float, metavar="FREQ",
                   help="desired NMR frequency")


if __name__ == "__main__":
  n = Driver()
  n.parser.print_help()
  # namespace stores output of parsing as variables within class Driver
  n.parser.parse_args("-i He4 -q 2 -e 8.7".split(), namespace=Driver)
  print(Driver.iso)
