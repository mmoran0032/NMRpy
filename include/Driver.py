# Driver - command line interface for nmrfreq


import argparse
from Isotope import Isotope
from NMRcalc import NMRcalc

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
    p.add_argument("-q", "--charge", type=int, nargs="*", default=[1],
                   help="selected charge state")
    g = p.add_mutually_exclusive_group()
    g.add_argument("-e", "--energy", type=float, nargs="*",
                   help="desired beam energy")
    g.add_argument("-f", "--freq", type=float, nargs=1,
                   help="desired NMR frequency")

  def drive(self, arguments):
    self.parseArguments(arguments)
    self.createIsotope()
    self.performCalculation()

  def parseArguments(self, arguments):
    self.parser.parse_args(arguments, namespace=Driver)

  def createIsotope(self):
    self.isotope = Isotope(self.isotope, self.masstable)

  def performCalculation(self):
    self.calc = NMRcalc(self.isotope, self.config, self.charge,
                        self.energy, self.freq)
    self.calc.processValues()
