# Driver - command line interface for nmrfreq


import argparse
from Isotope import Isotope
from NMRcalc import NMRcalc
import sys

desc = """NMRFREQ - analyzing magnet frequency utility for the NSL"""


class Driver(object):
  def __init__(self, config=None, masstable=None, version=""):
    self.isotope = None
    self.config = config
    self.calc = None
    self.masstable = masstable
    self.version = version
    self.parser = argparse.ArgumentParser(description=desc)
    self.defineUsage()


  def defineUsage(self):
    p = self.parser
    p.add_argument("-v", "--version", action="version",
                   version="nmrfreq {0}".format(self.version))
    p.add_argument("-i", "--iso", type=str, metavar="ISOTOPE", default="H1",
                   help="desired isotope name")
    p.add_argument("-q", "--charge", type=int, default=1,
                   help="selected charge state")
    g = p.add_mutually_exclusive_group()
    g.add_argument("-e", "--energy", type=float, nargs="*",
                   help="desired beam energy")
    g.add_argument("-f", "--frequency", type=float, metavar="FREQ",
                   help="desired NMR frequency")


  def createIsotope(self):
    self.isotope = Isotope(self.iso, self.masstable)


  def createMassTable(self, table):
    self.masstable = table


  def createCalculator(self, isotope, config):
    self.calc = NMRCalc(isotope, config)


  def parseArguments(self, argstring):
    arglist = argstring.split()
    if len(arglist) == 0:
      self.parser.print_help()
      sys.exit()
    else:
      # namespace stores output of parsing as variables within class Driver
      self.parser.parse_args(arglist, namespace=Driver)
      self.passArgumentsToCalc()


  def passArgumentsToCalc(self):
    self.calc = NMRcalc(self.isotope, self.config)
    self.calc.saveCharge(self.charge)
    self.calc.saveEnergy(self.energy)
    self.calc.saveFrequency(self.frequency)


  def drive(self, arguments):
    self.parseArguments(arguments)
    self.createIsotope()
    self.passArgumentsToCalc()
    self.calc.showResult()


if __name__ == "__main__":
  n = Driver()
  n.parseArguments("-i He4 -q 2 -e 8.7")
  n.createMassTable({"HE4": (2, 4)})
  n.createIsotope()
  print(n.isotope)
