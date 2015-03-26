# NMRcalc - data storage and calculator for nmrfreq


import data.config as config
import data.wapstra as wapstra
reload(config)
reload(wapstra)

from Isotope import Isotope

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
    Stores information required for calculation, including the ISOTOPE that
    we care about. Variables holding actual values are initialized to None
    since we don't know what we need to hold.

    NEW: we're going to restrict to only worrying about a single charge
    state at a time. Before, it forced tabular and was exceedingly sparse,
    or we had two full tabular files for energy ranges. No need to worry
    about that, and is more straightforward for the user.
    """
    self.chargeState = None
    self.energy = None
    self.frequency = None
    self.isotope = None


  def saveIsotope(self, isoName):
    self.isoName = Isotope(isoName)


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
      self.FLAGfrequency = True
    else:
      sys.stderr.write("Frequency ({0}) must be positive\n".format(freq))


if __name__ == "__main__":
  n = NMRcalc()
  testCases = ["HE4", "he4", "4he", "290Na", "22-Ne", "18O-10"]
  for iso in testCases:
    n.saveIsotope(iso)
