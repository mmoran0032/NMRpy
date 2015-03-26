# NMRcalc - data storage and calculator for nmrfreq


from math import sqrt


class NMRcalc(object):
  """
  Verifies and stores all user data and performs calculation when all
  required components are in place. Does not handle actually getting user
  input, which is in a separate driver class.
  """
  def __init__(self, isotope=None, config=None):
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
    self.isotope = isotope
    self.config = config


  def saveChargeState(self, charge):
    """
    Verifies that the charge state is an integer and within the range 1 - Z,
    then saves the value. Requires the isotope to already be saved.
    """
    if int(charge) == charge:
      if charge > 1 and charge < self.isotope.getZ():
        self.chargeState = charge


  def saveEnergy(self, energy):
    if energy > 0:
      self.energy = energy


  def saveFrequency(self, freq):
    if freq > 0:
      self.frequency = freq


if __name__ == "__main__":
  n = NMRcalc()
