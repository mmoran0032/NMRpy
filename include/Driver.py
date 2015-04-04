# Driver - command line interface for nmrfreq


import argparse
from Isotope import Isotope
from NMRcalc import NMRcalc
import sys

desc = """NMRFREQ - analyzing magnet frequency utility for the NSL"""


class Driver(object):
  def __init__(self, config, masstable, version=""):
    self.config = config
    self.masstable = masstable
    self.version = version
    self.parser = argparse.ArgumentParser(description=desc)
    self.defineUsage()


  def defineUsage(self):
    p = self.parser
    p.add_argument("-v", "--version", action="version",
                   version="nmrfreq {0}".format(self.version))
    p.add_argument("-i", "--isotope", type=str, default="H1",
                   help="desired isotope name")
    p.add_argument("-q", "--charge", type=int, default=1,
                   help="selected charge state")
    g = p.add_mutually_exclusive_group()
    g.add_argument("-e", "--energy", type=float,
                   help="desired beam energy")
    g.add_argument("-f", "--frequency", type=float, metavar="FREQ",
                   help="desired NMR frequency")


  def drive(self, arguments):
    self.parseArguments(arguments)
    self.createIsotope()
    self.passArgumentsToCalc()
    self.calc.processValues()


  def parseArguments(self, arguments):
    if len(arguments) == 0:
      self.parser.print_help()
      sys.exit()
    else:
      # namespace stores output of parsing as variables within class Driver
      self.parser.parse_args(arguments, namespace=Driver)


  def createIsotope(self):
    self.isotope = Isotope(self.isotope, self.masstable)


  def createMassTable(self, table):
    self.masstable = table


  def passArgumentsToCalc(self):
    self.calc = NMRcalc(self.isotope, self.config, self.charge,
                        self.energy, self.frequency)
