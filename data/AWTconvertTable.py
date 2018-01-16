#!/usr/bin/env python
# convertAWT.py - Mass Table Conversion Utility


import os

massFile = 'AWTMass-2003.dat'
newFile = os.path.join('..', 'nmrfreq', 'masstable.py')


def main():
    with open(massFile, 'r') as file:
        massDict = extractMasses(file)
    writeToFile(newFile, massDict, massFile)


def extractMasses(file):
    massdict = {}

    for line in file:
        line = adjustLine(line)
        if line is not None:
            isotope, Z, mass = getValuesFrom(line)
            mass = convertMass(mass)
            massdict[isotope] = (Z, mass)
    return massdict


def adjustLine(line):
    line = line.strip()
    if line[0] != '#' and line[-1] != '#':
        line = line[9:].strip()
        line = line.split()
        return line


def getValuesFrom(splitline):
    isotope = '{0}{1}'.format(splitline[2], splitline[1])
    isotope = isotope.upper()
    Z = int(splitline[0])
    mass = '{0}{1}'.format(splitline[-3], splitline[-2])
    return isotope, Z, mass


def convertMass(mass):
    mass = float(mass) / 1000000.0
    return mass


def writeToFile(filename, massdict, massFile):
    with open(filename, 'w') as f:
        f.write('# Mass table for use in nmrfreq from {0}\n'.format(massFile))
        f.write('table = {\n')
        f.write(createIsotopesString(massdict))
        f.write('}\n')


def createIsotopesString(massdict):
    string = ''
    for key in sorted(massdict.iterkeys()):
        string = '{2}    "{0}": {1},\n'.format(key, massdict[key], string)
    return string


if __name__ == '__main__':
    main()
