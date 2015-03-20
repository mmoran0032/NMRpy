#!/usr/bin/env python
# NMRFREQ - NMR Frequency Calculator for the NSL


versionNum = "0.9.99"
versionDate = "2015-XX-XX"

import data.config as config
import data.wapstra as wapstra
reload(config)
reload(wapstra)

from math import sqrt
import sys


class NMRcalc(object):
  """
  Verifies and stores all user data and performs calculation when all
  required components are in place. Does not handle actually getting user
  input, which is in a separate driver class.
  """
  def __init__(self):
    """
    Initializes flag for what actually will be calculated and container
    for the ISOTOPE that we care about. Variables holding actual values are
    initialized to None since we don't know what we need to hold.

    NEW: we're going to restrict to only worrying about a single charge
    state at a time. Before, it forced tabular and was exceedingly sparse,
    or we had two full tabular files for energy ranges. No need to worry
    about that, and is more straightforward for the user.
    """
    self.FLAGsingleEnergy = False
    self.FLAGfrequency = False
    self.FLAGcanCalculate = False
    self.chargeState = 0
    self.energy = None
    self.frequency = None
    self.isotope = ["", 0, 0] # Name, Z, Mass


  def saveIsotope(self, isoName):
    """
    Takes isotope input (###SYM or ###sym or SYM### or sym###) and converts
    it to SYM### (required for mass table) and saves it. Prints an error if
    the final isotope isn't found in the table.
    """
    from re import findall
    iso = isoName.upper()
    isoList = findall("\d+|\D+", iso)
    if (len(isoList) == 2):
      if isoList[0].isdigit():
        num, sym = isoList
      else:
        sym, num = isoList
      isoFinal = "{0}{1}".format(sym, num)
      if isoFinal[0] == "-":
        isoFinal = isoFinal[1:]
      self.verifyIsotope(isoFinal)
    else:
      sys.stderr.write("Isotope {0} not in accepted format\n".format(iso))


  def verifyIsotope(self, isotope):
    # We know the isotope is in the right format, now grab details
    if isotope in wapstra.table:
      self.isotope[0] = isotope
      self.isotope[1] = wapstra.table[isotope][0]
      self.isotope[2] = wapstra.table[isotope][1]
    else:
      sys.stderr.write("Isotope {0} not found in table\n".format(isotope))


  def saveChargeState(self, charge):
    """
    Verifies that the charge state is an integer and within the range 1 - Z,
    then saves the value. Requires the isotope to already be saved.
    """
    if int(charge) == charge:
      if charge > 1 and charge < self.isotope[1]:
        self.chargeState = charge
      else:
        sys.stderr.write("Charge state outside physical bounds (1-{0})\n"\
          .format(self.isotope[1]))
    else:
      sys.stderr.write("Charge state must be an integer")


  def saveEnergy(self, energy):
    if energy > 0:
      self.energy = energy
    else:
      sys.stderr.write("Energy ({0}) must be positive\n".format(energy))


  def saveFrequency(self, freq):
    if freq > 0:
      self.frequency = freq
    else:
      sys.stderr.write("Frequency ({0}) must be positive\n".format(freq))


if __name__ == "__main__":
  n = NMRcalc()
  testCases = ["HE4", "he4", "4he", "290Na", "22-Ne", "18O-10"]
  for iso in testCases:
    n.saveIsotope(iso)
