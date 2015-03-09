#!/usr/bin/env python

"""convertAWT.py - Mass Table Conversion Utility"""

filename = "2003AWTMass.dat"
newfile = "wapstra.py"

file = open(filename, "r")

massdict = {}

for line in file:
  if line[0] == "#":
    continue
  else:
    line = line.strip().split()
    mass = "%s%s" % (line[-3], line[-2])
    if mass[-1] == "#":
      continue
    else:
      for i in xrange(len(line)):
        if line[i].isalpha():
          if line[i] != "x" and line[i] != "IT" and line[i] != "ep":
            # i-2 -> Z
            # i-1 -> A
            symbol = "%s%s" % (line[i], line[i-1])
            symbol = symbol.upper()
            Z = int(line[i-2])
            mass = float(mass)/1000000.0 # to get into amu
            # print "{0} {1} {2}".format(symbol, Z, energy)
            massdict[symbol] = (Z, mass)

file.close()

file = open(newfile, "w")
file.write("table = {")
for key in sorted(massdict.iterkeys()):
  string = "\t'%s': %s,\n" % (key, massdict[key])
  file.write(string)
file.write("}\n")

file.close()

