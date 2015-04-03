# NMRcalc - data storage and calculator for nmrfreq


from math import sqrt


class NMRcalc(object):
  def __init__(self, isotope=None, config=None):
    self.chargeState = None
    self.energy = None
    self.frequency = None
    self.isotope = isotope
    self.config = config


  def saveChargeState(self, charge):
    if int(charge) == charge:
      if charge >= 1 and charge <= self.isotope.getZ():
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


  def performCalculation(self):
    charge = self.chargeState
    if self.energy is None:
      energy = self.calculateEnergy(self.frequency, charge)
      frequency = self.frequency
    elif self.frequency is None:
      energy = self.energy
      frequency = self.calculateFrequency(self.energy, charge)
    print("{0}, Charge State: +{1}\n".format(self.isotope, charge))
    print("\tNMR FREQUENCY: {0:9.6f} MHz".format(frequency))
    print("\tBEAM ENERGY:   {0:9.6f} MeV\n".format(energy))


  def showResult(self):
    if self.energy is None and self.frequency is None:
      print(self.isotope)
    else:
      self.performCalculation()


if __name__ == "__main__":
  n = NMRcalc()
