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
    self.showCalculation()

  def performCalculation(self):
    if self.energy is None:
      self.energy = self.calculateEnergy(self.frequency, self.charge)
    elif self.frequency is None:
      self.frequency = self.calculateFrequency(self.energy, self.charge)

  def calculateEnergy(self, freq, charge):
    K = self.config.magnetK
    factor = ((freq * charge) / (K * self.isotope.getMass()))**2
    return (self.isotope.getMass() * self.config.amuToMeV *
            (sqrt(1 + factor) - 1))

  def calculateFrequency(self, energy, charge):
    K = self.config.magnetK
    factor = energy / (self.isotope.getMass() * self.config.amuToMeV)
    return (K * (self.isotope.getMass() / charge) *
            sqrt(factor**2 + 2.0 * factor))

  def showCalculation(self):
    if type(self.charge) is not list:
      self.showSingleCalculation()
    else:
      self.showTable()

  def showSingleCalculation(self):
    print("{0}, Charge State: +{1}\n".format(self.isotope, self.charge))
    print("\tNMR FREQUENCY: {0:9.6f} MHz".format(self.frequency))
    print("\tBEAM ENERGY:   {0:9.6f} MeV\n".format(self.energy))

  def showTable(self):
    pass

  def getIsotope(self):
    print(self.isotope)
