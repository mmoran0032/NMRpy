# NMRcalc - data storage and calculator for nmrfreq


from math import sqrt


class NMRcalc(object):
  def __init__(self, isotope, config, charge=None, energy=None, freq=None):
    self.isotope = isotope
    self.config = config
    self.charge = charge
    self.energy = energy
    self.frequency = freq


  def processValues(self):
    if self.valuesAreValid():
      self.getResult()
    else:
      self.getIsotope()


  def valuesAreValid(self):
    return self.chargeStateValid() and self.energyAndFreqValid()


  def chargeStateValid(self):
    charge = self.charge
    return charge >= 1 and charge <= self.isotope.getZ()


  def energyAndFreqValid(self):
    energy = self.energy
    freq = self.frequency
    if freq is None and energy is not None:
      return energy > 0
    elif freq is not None and energy is None:
      return freq > 0


  def getResult(self):
    self.performCalculation()
    self.showNMRcalculation()


  def performCalculation(self):
    if self.energy is None:
      self.calculateEnergy()
    elif self.frequency is None:
      self.calculateFrequency()


  def calculateEnergy(self):
    K = self.config.magnetK
    freq = self.frequency
    charge = self.charge
    factor = ((freq * charge) / (K * self.isotope.getMass()))**2
    self.energy = (self.isotope.getMass() * self.config.amuToMeV *
                  (sqrt(1 + factor) - 1))


  def calculateFrequency(self):
    K = self.config.magnetK
    energy = self.energy
    charge = self.charge
    factor = energy / (self.isotope.getMass() * self.config.amuToMeV)
    self.frequency = (K * (self.isotope.getMass() / charge) *
                     sqrt(factor**2 + 2.0 * factor))


  def showNMRcalculation(self):
    print("{0}, Charge State: +{1}\n".format(self.isotope, self.charge))
    print("\tNMR FREQUENCY: {0:9.6f} MHz".format(self.frequency))
    print("\tBEAM ENERGY:   {0:9.6f} MeV\n".format(self.energy))


  def getIsotope(self):
    print(self.isotope)
