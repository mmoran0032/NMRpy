#!/usr/bin/env python
#convertAWT.py - Mass Table Conversion Utility


massFile = "AWTMass-2003.dat"
newFile = "masstable.py"


def openFileFrom(filename):
  file = open(filename, "r")
  return file


def extractMasses(file):
  massdict = {}

  for line in file:
    line = adjustLine(line)
    if line is not None:
      print line
      isotope, Z, mass = getValuesFrom(line)
      mass = convertMass(mass)
      massdict[isotope] = (Z, mass)
  file.close()
  return massdict


def adjustLine(line):
  line = line.strip()
  if line[0] != "#" and line[-1] != "#":
    line = line[9:].strip()
    line = line.split()
    return line


def getValuesFrom(splitline):
  isotope = "{0}{1}".format(splitline[2], splitline[1])
  isotope = isotope.upper()
  Z = int(splitline[0])
  mass = "{0}{1}".format(splitline[-3], splitline[-2])
  return isotope, Z, mass


def convertMass(mass):
  mass = float(mass)/1000000.0
  return mass


def writeToFile(filename, massdict, massFile):
  file = open(filename, "w")
  file.write("# Mass table for use in nmrfreq from {0}\n".format(massFile))
  file.write("table = {\n")
  for key in sorted(massdict.iterkeys()):
    string = "\t'%s': %s,\n" % (key, massdict[key])
    file.write(string)
  file.write("}\n")
  file.close()


def main():
  file = openFileFrom(massFile)
  massDict = extractMasses(file)
  writeToFile(newFile, massDict, massFile)


if __name__ == "__main__":
  main()
