

from .config import magnetK

# Output optimized for 80-character-width terminal
header = '\n{0}, Charge State: +{1:<2d}   K = {2:<6.2f}\n'
titles = '  ENERGY  FREQUENCY ' * 4
border = '-' * 80
values = '{0:8.3f}{1:11.6f} '
blank = '                    '


class Display:

    def __init__(self, isotope, charges, energies, freqs, fields):
        self.isotope = isotope
        self.charges = charges
        self.energies = energies
        self.freqs = freqs
        self.fields = fields

    def showSingleCalculation(self):
        charge = self.charges[0]
        energy = self.energies[0][0]
        freq = self.freqs[0][0]
        field = self.fields[0][0]
        self.showSingleEnergy(charge, energy, freq, field)

    def showSingleEnergy(self, charge, energy, freq, field):
        topLine = header.format(self.isotope, charge, magnetK)
        print('{0}\n    NMR FREQUENCY:   {1:10.6f} MHz'.format(topLine, freq))
        print('    BEAM ENERGY:     {0:10.6f} MeV'.format(energy))
        print('    FIELD STRENGHT:  {0:10.6f} G\n'.format(field))

    def showMultipleCalculations(self):
        if len(self.charges) == 1:
            self.showMultipleEnergy(0)
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
        print(self.createTableHeader(charge))
        print(self.createTableBody(energies, freqs))

    def createTableHeader(self, charge):
        return '{0}\n{1}\n{2}'.format(
            header.format(self.isotope, charge, magnetK),
            titles,
            border)

    def createTableBody(self, energy, freq):
        rows = self.determineNumberOfRows(energy)
        table = ''
        for i in range(rows):
            row = ''
            for j in range(4):
                index = i + j * rows
                subRange = self.createSegment(energy, freq, index)
                row = '{0}{1}'.format(row, subRange)
            table = '{0}{1}\n'.format(table, row)
        return table

    def determineNumberOfRows(self, values):
        if len(values) % 4 != 0:
            return len(values) // 4 + 1
        else:
            return len(values) // 4

    def createSegment(self, energy, freq, index):
        try:
            return values.format(energy[index], freq[index])
        except:
            return blank
