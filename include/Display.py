# Display - shows results of NMR calculations


from share.config import magnetK

blank = "                "
values = "{0:7.3f}{1:9.6f}"
header = "ENERGY FREQUENCY"


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
    print("""{0}, Charge State: +{1:2d}   K = {4:6.2f}\n
        NMR FREQUENCY: {2:9.6f} MHz
        BEAM ENERGY:   {3:9.6f} MeV\n"""
          .format(self.isotope, charge, freq, energy, magnetK))

  def showMultipleCalculations(self):
    if len(self.charges) == 1:
      self.showMultipleEnergy(self.charges[0])
    else:
      self.showMultipleCharge()

  def showMultipleCharge(self):
    for i in range(len(self.charges)):
      if len(self.energies[0]) == 1:
        self.showSingleEnergy(self.charges[i], self.energies[i][0],
                              self.freqs[i][0])
      else:
        self.showMultipleEnergy(i)

  def showMultipleEnergy(self, index):
    charge = self.charges[index]
    energies = self.energies[index]
    freqs = self.freqs[index]
    print("table of energies")
    print(charge, energies, freqs)
