# Driver - command line interface for nmrfreq


import argparse

from .isotope import Isotope
from .calc import NMRcalc

desc = """NMRFREQ - analyzing magnet frequency utility for the NSL"""


class Driver:

    def __init__(self, masstable, version=""):
        self.masstable = masstable
        self.version = version
        self.parser = argparse.ArgumentParser(description=desc)
        self.defineUsage()

    def defineUsage(self):
        p = self.parser
        p.add_argument("-v", "--version", action="version",
                       version="nmrfreq {0}".format(self.version))
        p.add_argument("-i", "--isotope", type=str, nargs=1,
                       help="desired isotope name")
        p.add_argument("-q", "--charge", type=int, nargs="*",
                       help="selected charge state")
        g = p.add_mutually_exclusive_group()
        g.add_argument("-e", "--energy", type=float, nargs="*",
                       help="desired beam energy")
        g.add_argument("-f", "--freq", type=float, nargs=1,
                       help="desired NMR frequency")

    def drive(self):
        self.parser.parse_args(namespace=Driver)
        try:
            self.createIsotope()
            self.performCalculation()
        except KeyError:
            print("No matching isotope for {} found".format(self.isotope))
        except IndexError:
            print("Isotope {} not a valid input".format(self.isotope))
        except TypeError:
            self.parser.print_help()

    def createIsotope(self):
        if (self.isotope is None and
                (self.energy is not None or self.freq is not None)):
            self.isotope = ["H1"]
        self.isotope = self.isotope[0]
        self.isotope = Isotope(self.isotope, self.masstable)

    def performCalculation(self):
        self.calc = NMRcalc(self.isotope, self.charge,
                                 self.energy, self.freq)
        self.calc.processValues()
