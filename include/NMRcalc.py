# NMRcalc - data storage and calculator for nmrfreq


from math import sqrt


class NMRcalc(object):
  def __init__(self, isotope, config, charge=None, energy=None, freq=None):
    self.isotope = isotope
    self.config = config
    self.charge = charge
    self.energy = energy
    self.freq = freq

  def processValues(self):
    if self.valuesAreValid():
      self.getResult()
    else:
      self.getIsotope()

  def valuesAreValid(self):
    return self.chargeStateValid() and self.energyAndFreqValid()

  def chargeStateValid(self):
    for charge in self.charge:
      return charge >= 1 and charge <= self.isotope.getZ()

  def energyAndFreqValid(self):
    if self.freq is None and self.energy is not None:
      for energy in self.energy:
        return energy > 0
    elif self.freq is not None and self.energy is None:
      return self.freq > 0

  def getResult(self):
    self.performCalculation()
    self.showCalculation()

  def performCalculation(self):
    charge = self.charge[0]
    if self.energy is None:
      self.energy = [self.calculateEnergy(freq, charge) for freq in self.freq]
    elif self.freq is None:
      self.freq = [self.calculateFrequency(energy, charge) for energy in self.energy]

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
    if len(self.charge) == 1 and len(self.energy) == 1:
      self.showSingleCalculation()
    else:
      self.showTable()

  def showSingleCalculation(self):
    print("{0}, Charge State: +{1}\n".format(self.isotope, self.charge[0]))
    print("\tNMR FREQUENCY: {0:9.6f} MHz".format(self.freq[0]))
    print("\tBEAM ENERGY:   {0:9.6f} MeV\n".format(self.energy[0]))

  def showTable(self):
    pass

  def getIsotope(self):
    print(self.isotope)
