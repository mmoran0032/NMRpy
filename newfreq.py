#!/usr/bin/env python
# NMRFREQ - NMR Frequency Calculator for the NSL


versionNum = "0.9.99"
versionDate = "2015-XX-XX"

import data.config as config
import data.wapstra as wapstra
reload(config)
reload(wapstra)

from math import sqrt
import os
import subprocess as sp
import sys


#####
# Creates class to handle all actions
#   does not include actually taking user input, just storage and
#   manipulation of variables
#####
class NMRcalc(object):
  def __init__(self):
    """
    Initializes flag for what actually will be calculated and container
    for the ISOTOPE that we care about. Variables holding actual values are
    Not initialized, since we don't know which ones and how many we need.
    """
    self.FLAGsingleCharge = False
    self.FLAGsingleEnergy = False
    self.FLAGfrequency = False
    self.FLAGcanCalculate = False
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
      print isoFinal
    else:
      sys.stderr.write("Given isotope not in accepted format\n")

    if isoFinal in wapstra.table:
      self.isotope[0] = isoFinal
      self.isotope[1] = wapstra.table[isoFinal][0]
      self.isotope[2] = wapstra.table[isoFinal][1]
    else:
      sys.stderr.write("Isotope {0} not found in table\n".format(isoFinal))


  def saveCharge(self, chargeStart, chargeEnd = 0):
    if self.chechCharge(chargeStart):
      self.charge[0] = chargeStart
    if chargeEnd != 0 and self.checkCharge(chargeEnd):
      self.charge[1] = chargeEnd
      if self.charge[0] > self.charge[1]:
        # exchange two saved values for the charge states
        self.charge[0], self.charge[1] = self.charge[1], self.charge[0]
    else:
      self.charge[1] = self.charge[0]


  def checkCharge(self, charge):
    flag = True
    if int(charge) != charge:
      flag = False
      sys.stderr.write("Charge state must be an integer")
    else:
      if charge < 1 or charge > self.isotope[1]:
        flag = False
        sys.stderr.write("Charge state outside physical bounds (1-{0})\n"\
          .format(self.isotope[1]))
    return flag


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
  testCases = ["HE4", "he4", "4he", "290Na", "22-Ne"]
  for iso in testCases:
    print iso,
    n.saveIsotope(iso)
