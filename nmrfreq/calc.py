# NMRcalc - data storage and calculator for nmrfreq


from math import sqrt

from . import config
from . import display



class NMRcalc:

    def __init__(self, isotope, charge=None, energy=None, freq=None):
        self.isotope = isotope
        self.charge = charge
        self.energy = energy
        self.freq = freq
        self.determineEnergyValues()
        self.determineCharges()

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

    def determineCharges(self):
        try:
            self.charge = list(set(self.charge))
        except TypeError:
            pass

    def processValues(self):
        if self.valuesAreValid():
            self.getResult()
        elif self.energyAndFreqValid():
            self.charge = [1]
            self.getResult()
        else:
            if self.eitherValueValid():
                print("Both charge and energy/frequency required, or neither")
            print(self.isotope)

    def valuesAreValid(self):
        return self.chargeStateValid() and self.energyAndFreqValid()

    def eitherValueValid(self):
        return self.chargeStateValid() or self.energyAndFreqValid()

    def chargeStateValid(self):
        if self.charge is not None:
            return all([q >= 1 and q <= self.isotope.Z for q in self.charge])
        else:
            return False

    def energyAndFreqValid(self):
        if self.freq is None and self.energy is not None:
            return all([e > 0 for e in self.energy])
        elif self.freq is not None and self.energy is None:
            return all([f > 0 for f in self.freq])
        else:
            return False

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
        factor = ((freq * charge) / (config.magnetK * self.isotope.mass)) ** 2
        return self.isotope.mass * config.amuToMeV * (sqrt(1 + factor) - 1)

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
        factor = energy / (self.isotope.mass * config.amuToMeV)
        return config.magnetK * (self.isotope.mass / charge) * \
            sqrt(factor ** 2 + 2.0 * factor)

    def showCalculation(self):
        display = display.Display(self.isotope, self.charge,
                                  self.energy, self.freq)
        if len(self.charge) == 1 and len(self.energy[0]) == 1:
            display.showSingleCalculation()
        else:
            display.showMultipleCalculations()
