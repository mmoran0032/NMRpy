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
    self.charge = list(set(self.charge))
    self.charge.sort()
    self.determineEnergyValues()

  def determineEnergyValues(self):
    if self.energy is not None:
      if len(self.energy) == 3:
        self.createEnergyRange()
      else:
        self.energy = [self.energy[0]]

  def createEnergyRange(self):
    self.energy.sort()
    step, start, stop = self.energy
    eList = [start]
    while eList[-1] < stop:
      newEnergy = float("{0:.3f}".format(eList[-1] + step))
      eList.append(newEnergy)
    self.energy = eList

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
    if self.energy is None:
      self.createEnergyList()
    elif self.freq is None:
      self.createFreqList()

  def createEnergyList(self):
    energies = []
    freqs = []
    for charge in self.charge:
      eList = [self.calculateEnergy(f, charge) for f in self.freq]
      energies.append(eList)
      fList = [f for f in self.freq]
      freqs.append(fList)
    self.energy = energies
    self.freq = freqs

  def calculateEnergy(self, freq, charge):
    K = self.config.magnetK
    factor = ((freq * charge) / (K * self.isotope.getMass()))**2
    return (self.isotope.getMass() * self.config.amuToMeV *
            (sqrt(1 + factor) - 1))

  def createFreqList(self):
    energies = []
    freqs = []
    for charge in self.charge:
      eList = [e for e in self.energy]
      energies.append(eList)
      fList = [self.calculateFrequency(e, charge) for e in self.energy]
      freqs.append(fList)
    self.energy = energies
    self.freq = freqs

  def calculateFrequency(self, energy, charge):
    K = self.config.magnetK
    factor = energy / (self.isotope.getMass() * self.config.amuToMeV)
    return (K * (self.isotope.getMass() / charge) *
            sqrt(factor**2 + 2.0 * factor))

  def showCalculation(self):
    display = Display(self.isotope, self.charge, self.energy, self.freq)
    if len(self.charge) == 1:
      display.showSingleCalculation()
    else:
      display.showMultipleCalculations()

  def getIsotope(self):
    print(self.isotope)
