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
    if int(charge) != charge:
      sys.stderr.write("Charge state must be an integer")
    else:
      if charge < 1 or charge > self.isotope[1]:
        sys.stderr.write("Charge state outside physical bounds (1-{0})\n"\
          .format(self.isotope[1]))
      else:
        self.chargeState = charge


  def saveEnergy(self, energyStart, energyEnd = 0, energyStep = 0):
    if self.checkEnergy(energyStart):
      self.energy[0] = energyStart
    if energyEnd != 0 and self.checkEnergy(energyEnd):
      self.energy[1] = energyStart
      if energyStep > 0:
        self.energy[2] = energyStep
      else:
        sys.stderr.write("Energy step not valid\n")
        sys.stderr.write("Setting energy step to default (1 MeV)\n")
        self.energy[2] = 1.
    else:
      self.energy[1] = self.energy[0]


  def checkEnergy(self, energy):
    flag = True
    if energy < 0:
      sys.stderr.write("Must have a positive energy\n")
      flag = False
    return flag


  def saveFrequency(self, frequency):
    if self.checkFrequency(frequency):
      self.freq = frequency


  def checkFrequency(self, frequency):
    flag = True
    if frequency <= 0:
      sys.stderr.write("Must have a positive frequency\n")
      flag = False
    return flag


if __name__ == "__main__":
  n = NMRcalc()
  testCases = ["HE4", "he4", "4he", "290Na", "22-Ne", "18O-10"]
  for iso in testCases:
    n.saveIsotope(iso)
