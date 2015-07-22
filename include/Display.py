# Display - shows results of NMR calculations


class Display(object):
  def __init__(self, isotope, charges, energies, freqs):
    self.isotope = isotope
    self.charges = charges
    self.energies = energies
    self.freqs = freqs

  def showSingleCalculation(self):
    self.showSingle(self.charges[0], self.energies[0][0], self.freqs[0][0])

  def showSingle(self, charge, energy, freq):
    print("""{0}, Charge State: +{1}\n
        NMR FREQUENCY: {2:9.6f} MHz
        BEAM ENERGY:   {3:9.6f} MeV\n"""
          .format(self.isotope, charge, freq, energy))

  def showMultipleCharge():
    pass

  def showMultipleEnergy():
    pass
