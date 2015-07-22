# NMRcalc - data storage and calculator for nmrfreq


from math import sqrt
from Display import Display


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
    return all([q >= 1 and q <= self.isotope.getZ() for q in self.charge])

  def energyAndFreqValid(self):
    if self.freq is None and self.energy is not None:
      return all([e > 0 for e in self.energy])
    elif self.freq is not None and self.energy is None:
      return all([f > 0 for f in self.freq])

  def getResult(self):
    self.performCalculation()
    self.showCalculation()

  def performCalculation(self):
    for charge in self.charge:
      if self.energy is None:
        self.energy = [self.calculateEnergy(f, charge) for f in self.freq]
      elif self.freq is None:
        self.freq = [self.calculateFrequency(e, charge) for e in self.energy]

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
    display = Display(self.isotope, self.charge, self.energy, self.freq)
    if len(self.charge) == 1 and len(self.energy) == 1:
      display.showSingleCalculation()
    else:
      print("show table")

  def getIsotope(self):
    print(self.isotope)
