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


  def calculateEnergy(self, freq, charge):
    K = self.config.magnetK
    factor = ((freq * charge) / (K * self.isotope.getMass()))**2
    energy = (self.isotope.getMass() * self.config.amuToMeV *
             (sqrt(1 + factor) - 1))
    return energy


  def calculateFrequency(self, energy, charge):
    K = self.config.magnetK
    factor = energy / (self.isotope.getMass() * self.config.amuToMeV)
    freq = (K * (self.isotope.getMass() / charge) *
           sqrt(factor**2 + 2.0 * factor))
    return freq


  def showResult(self, charge, energy, frequency):
    if energy is None:
      energy = self.calculateEnergy(frequency, charge)
    elif frequency is None:
      frequency = self.calculateFrequency(energy, charge)
    print("{0}, Charge State: +{1}\n".format(self.isotope, charge))
    print("\tNMR FREQUENCY: {0:9.6f} MHz".format(frequency))
    print("\tBEAM ENERGY:   {0:9.6f} MeV\n".format(energy)))

if __name__ == "__main__":
  n = NMRcalc()
