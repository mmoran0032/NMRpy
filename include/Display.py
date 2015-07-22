# Display - shows results of NMR calculations


class Display(object):
  def __init__(self, isotope, charges, energies, freqs):
    self.isotope = isotope
    self.charges = charges
    self.energies = energies
    self.freqs = freqs

  def showSingleCalculation(self):
    charge = self.charges[0]
    energy = self.energies[0][0]
    freq = self.freqs[0][0]
    self.showSingleEnergy(charge, energy, freq)

  def showSingleEnergy(self, charge, energy, freq):
    print("""{0}, Charge State: +{1}\n
        NMR FREQUENCY: {2:9.6f} MHz
        BEAM ENERGY:   {3:9.6f} MeV\n"""
          .format(self.isotope, charge, freq, energy))

  def showMultipleCalculations(self):
    if len(self.charges) == 1:
      self.showMultipleEnergy()
    else:
      self.showMultipleCharge()

  def showMultipleCharge(self):
    for i in range(len(self.charges)):
      self.showSingleEnergy(self.charges[i], self.energies[i][0],
                            self.freqs[i][0])

  def showMultipleEnergy():
    pass
