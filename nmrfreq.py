#!/usr/bin/env python

versionnum = "1.0.0"
versiondate = "2014-08-04"

#####
# Set Accelerator Environment
# - modules reloaded to ensure that they are recompiled if they've been changed
#####
import data.NMRconfig as NMRconfig
reload(NMRconfig)

import importlib
config = importlib.import_module("data.{0}config".format(NMRconfig.ACCELERATOR))
reload(config)

#####
# Global variables for required values - rough, but workable
#   plan on changing everything to class structure eventually
#####
Q1 = 0          # Starting charge state, used if only one charge state wanted
Q2 = 0          # Ending charge state, zero if only one charge state wanted
E1 = 0          # Starting energy, used if only one energy wanted
E2 = 0          # Ending energy, zero if only one energy wanted
ESTEP = 0       # Energy step, used only if an energy range wanted
FREQ = 0        # NMR Frequency, used if converting energy to frequency
ISO = ""        # Isotope name
Z = 0           # Z of isotope, taken from Wapstra mass database
MASS = 0        # Mass of isotope in AMU, taken from Wapstra mass database

import sys

#####
# Get command line arguments and save them
#####
def main():
  """Parses command line options, takes appropriate action"""

  options = {2:onearg, 3:editconfig, 4:editconfig, 6:twosingle,
             7:qrange, 8:erange, 9:tworange}

  if len(sys.argv) in options:
    options[len(sys.argv)]()
  else: # number of arguments doesn't match up with what's expected
    badusage()
  # Have values, need to check that everything is valid and do calculations
  # Anything that doesn't do this (1-arg, etc) needs sys.exit() at end
  checkiso()
  checkcharge()
  if FREQ == 0:
    checkenergy()
  else:
    checkfreq()
  settype()

# Only one argument, just printing stuff
def onearg():
  # Possible: -a || -c || -v || -h
  if sys.argv[1] == "-v" or sys.argv[1] == "--version":
    version()
  elif sys.argv[1] == "-h" or sys.argv[1] == "--help":
    help()
  elif sys.argv[1] == "-c":
    editconfig()
  elif sys.argv[1] == "-a" or sys.argv[1] == "--accelerator":
    environment()
  else:
    badusage()

def editconfig():
  if sys.argv[1] == "-c":
    if len(sys.argv) == 3:
      editfile(sys.argv[2])
    elif len(sys.argv) == 4:
      editfile(sys.argv[2], sys.argv[3])
    else:
      editfile() # restore defaults
  else:
    badusage()

def editfile(accel="FN", outdir="~"):
  # stores content of original NMRconfig file
  print "Updating NMRconfig to reflect changes ({0})".format(accel)
  file = open("NMRconfig.py", "r")
  filedata = []
  for line in file:
    line = line.strip().split()
    filedata.append(line)
  file.close()

  # edits contents of file
  file = open("NMRconfig.py", "w")
  for line in filedata:
    if len(line) == 0:
      line = ""
    elif line[0] == "ACCELERATOR":
      line[2] = "'{0}'".format(accel)
    elif line[0] == "OUTPUT":
      line[2] = "'{0}'".format(outdir)
    else:
      pass
    line = " ".join(line)
    file.write("{0}\n".format(line))
  file.close()

  sys.exit()

# Just want a single frequency/energy
def twosingle():
  # Possible: -sq Q -se E || -sf F
  global ISO, Q1, E1, FREQ

  if sys.argv[2] == "-sq" and (sys.argv[4] == "-se" or sys.argv[4] == "-sf"):
    ISO = sys.argv[1]
    Q1 = int(sys.argv[3])
    if sys.argv[4] == "-se":
      E1 = float(sys.argv[5])
    elif sys.argv[4] == "-sf":
      FREQ = float(sys.argv[5])
  else:
    badusage()

def qrange():
  # Possible: -mq Q1 Q2 -se/-sf E/F
  global ISO, Q1, Q2, E1, FREQ

  if sys.argv[2] == "-mq" and (sys.argv[5] == "-se" or sys.argv[5] == "-sf"):
    ISO = sys.argv[1]
    Q1 = int(sys.argv[3])
    Q2 = int(sys.argv[4])
    if sys.argv[5] == "-se":
      E1 = float(sys.argv[6])
    elif sys.argv[5] == "-sf":
      FREQ = float(sys.argv[6])
  else:
    badusage()

def erange():
  # Possible: -sq Q -me E1 E2 ESTEP
  global ISO, Q1, E1, E2, ESTEP

  if sys.argv[2] == "-sq" and sys.argv[4] == "-me":
    ISO = sys.argv[1]
    Q1 = int(sys.argv[3])
    E1 = float(sys.argv[5])
    E2 = float(sys.argv[6])
    ESTEP = float(sys.argv[7])
  else:
    badusage()

def tworange():
  # Possible: -mq Q1 Q2 -me E1 E2 ESTEP
  global ISO, Q1, Q2, E1, E2, ESTEP

  if sys.argv[2] == "-mq" and sys.argv[5] == "-me":
    ISO = sys.argv[1]
    Q1 = int(sys.argv[3])
    Q2 = int(sys.argv[4])
    E1 = float(sys.argv[6])
    E2 = float(sys.argv[7])
    ESTEP = float(sys.argv[8])
  else:
    badusage()

# Not doing any calculations, use this
def usage():
  import os
  sys.stderr.write("Usage: "+os.path.basename(sys.argv[0]))
  sys.stderr.write(" isotope <charge state flag> <energy/freq. flag>\n")
  sys.stderr.write("  charge state flags: -sq Q\n")
  sys.stderr.write("                      -mq Q1 Q2\n")
  sys.stderr.write("  energy/freq. flags: -se energy (MeV)\n")
  sys.stderr.write("                      -sf freq (MHz)\n")
  sys.stderr.write("                      -me en1 en2 step (MeV)\n")
  sys.stderr.write("  other options: [-a] [-c] [-h] [-v] [-c accelerator]\n")

def badusage():
  usage()
  import os
  sys.stderr.write("\nRun `"+os.path.basename(sys.argv[0])+" --help' for more information.\n")
  sys.exit()

def help():
  usage()
  sys.stderr.write("\n")
  sys.stderr.write(" -a:  displays accelerator environment\n")
  sys.stderr.write(" -c:  edits NMRconfig file\n")
  sys.stderr.write(" -h:  prints help to screen\n")
  sys.stderr.write(" -v:  displays current version\n")
  sys.stderr.write(" -sq: find frequency/energy for a single charge state\n")
  sys.stderr.write(" -mq: find frequencies/energies for a range of charge states\n")
  sys.stderr.write(" -sf: determine energy from given frequency (MHz)\n")
  sys.stderr.write(" -se: determine frequency for a single energy (MeV)\n")
  sys.stderr.write(" -me: determine frequencies for multiple energies (MeV)\n")
  sys.exit()

def version():
  print "nmrfreq.py {0} ({1})".format(versionnum, versiondate)
  print "NMR Frequency utility for Notre Dame accelerators"
  sys.exit()

def environment():
  if NMRconfig.ACCELERATOR == "FN":
    print "10 MV FN Tandem Accelerator (FNconfig.py)"
  elif NMRconfig.ACCELERATOR == "SA":
    print "5 MV StANA Vertical Accelerator (SAconfig.py)"
  else:
    print "Custom Accelerator ({0}config.py)".format(NMRconfig.ACCELERATOR)
  sys.exit()

#####
# Checking values of inputs to make sure that we are set for calculations
#####
def checkiso():
  import data.wapstra as wapstra

  global ISO, Z, MASS

  ISO = ISO.upper()
  if ISO[0].isdigit():
    for i in xrange(1,len(ISO)+1,1):
      if not ISO[:i].isdigit():
        num = ISO[:i-1]
        sym = ISO[i-1:]
        ISO = "{0}{1}".format(sym, num) # New version of string formatting
        break
      # symbol now contains type required by masstable
      # use wapstra.py dictionary (wapstra) to determine values
  if ISO in wapstra.table:
    Z = wapstra.table[ISO][0]
    MASS = wapstra.table[ISO][1]
  else:
    print "ISOTOPE not found"
    sys.exit()

def checkcharge():
  # charge states need to be integers and both less than Z of nucleus
  # first, decide if Q2 present (meaning we need a range)
  global Q1, Q2

  if Q2 != 0: # range
    if _checkchargesize(Q1) and _checkchargesize(Q2):
      # valid values for each charge size, need to see which is bigger
      if Q1 > Q2:
        Q1, Q2 = Q2, Q1 # exchanges values to make Q2 > Q1
      else:
        pass
  else: # only Q1
    if _checkchargesize(Q1):
      # valid charge state
      pass

def _checkchargesize(qvalue):
  if int(qvalue) != qvalue:
    # Probably redundant, since we force integer values when grabbing from cl
    print "INVALID Q-VALUE: must be integer"
    sys.exit()
  else:
    if qvalue > Z or qvalue < 1:
      print "INVALID Q-VALUE: must be <= Z of nucleus and non-zero"
      sys.exit()
    else:
      return True

def checkenergy():
  global E1, E2, ESTEP

  if E2 != 0: # range
    if _checkenergyvalue(E1) and _checkenergyvalue(E2):
      if E1 > E2:
        E1, E2 = E2, E1
      else:
        pass
    if ESTEP > abs(E1 - E2):
      ESTEP = abs(E1 - E2)
  else:
    if _checkenergyvalue(E1):
      pass

def _checkenergyvalue(energy):
  if energy <= 0:
    print "INVALID ENERGY: must be positive"
    sys.exit()
  else:
    return True

def checkfreq():
  if FREQ <= 0:
    print "INVALID NMR FREQUENCY: must be positive"
    sys.exit()
  else:
    pass

#####
# All values set, ready to calculate
#####
def settype():
  if ESTEP != 0: # tabular output to file
    if Q2 != 0:
      # call tabular for each q
      for i in xrange(Q2-Q1+1):
        simpletable(Q1 + i)
    else:
      simpletable(Q1)
  else: # only one E value, or one F value
    if Q2 != 0:
      # for each Q value, print result to terminal
      screentable()
    else:
      simpleout()

def simpleout():
  print "Isoptope: {0} (Z = {1}, MASS = {2} amu), Charge State: +{3}\n"\
    .format(ISO, Z, MASS, Q1)
  if E1 != 0:
    freq = getfrequency(E1, Q1)
    #freqerr = getfrequencyerror(freq)
    energy = E1
    enerr = 0.
  elif FREQ != 0:
    energy = getenergy(FREQ, Q1)
    #enerr = getenergyerror(FREQ, Q1, energy)
    freq = FREQ
    freqerr = 0.
  print "    NMR FREQUENCY: {0:9.6f} MHz".format(freq)
  print "    BEAM ENERGY:   {0:9.6f} MeV".format(energy)
  print

def simpletable(charge):
  import subprocess as sp
  import os

  proc = sp.Popen(["date '+%Y-%m-%d %H:%M:%S'"], stdout=sp.PIPE, shell=True)
  date, err = proc.communicate()

  location = os.path.expanduser(NMRconfig.OUTPUT)
  filename = "{0}+{1}.nmr".format(ISO, charge)
  fileloc = os.path.join(location, filename)

  #os.system("touch {0}".format(filename))
  fout = open(fileloc, "w")

  header = """
  {0} Analyzing Magnet Frequencies in MHz\t\t\t{5}

  {1}, Mass = {3:12.9f}, Charge State = +{2}\t\tK = {4}
  """.format(NMRconfig.ACCELERATOR, ISO, charge, MASS, config.K, date)
  #print header
  #print "  ENERGY    FREQ     "*5
  #print "{0}".format("-"*105)

  fout.write("{0}\n".format(header))
  fout.write("{0}{0}{0}{0}{0}\n".format("  ENERGY    FREQ     "))
  fout.write("{0}\n".format("-"*105))

  # want to print columns going down...
  entrylength = int((E2 - E1)/ESTEP) / 5
  for i in xrange(entrylength + 1):
    et1 = E1 + ESTEP*i
    et2 = E1 + ESTEP*(i + entrylength + 1)
    et3 = E1 + ESTEP*(i + 2*(entrylength + 1))
    et4 = E1 + ESTEP*(i + 3*(entrylength + 1))
    et5 = E1 + ESTEP*(i + 4*(entrylength + 1))
    line0 = "{0:8.3f}  {1:8.5f}   {2:8.3f}  {3:8.5f}   {4:8.3f}"\
      .format(et1, getfrequency(et1,charge), et2, getfrequency(et2,charge), et3)
    line1 = "  {0:8.5f}   {1:8.3f}  {2:8.5f}   {3:8.3f}  {4:8.5f}"\
      .format(getfrequency(et3,charge), et4, getfrequency(et4,charge),\
      et5, getfrequency(et5, charge))
    line = "{0}{1}\n".format(line0, line1)
    fout.write(line)

    if (i+1) % 4 == 0:
      fout.write("\n")

    #print line
  fout.write("\n")
  fout.close()
  #print

  print "\n\tFile {0} created\n".format(fileloc)

def screentable():
  if E1 != 0:
    header = """
    {0} Analyzing Magnet Frequencies in MHz

    {1}, Mass = {3:12.9f}, Energy = {2} MeV\t\t\tK = {4}
    """.format(NMRconfig.ACCELERATOR, ISO, E1, MASS, config.K)
  elif FREQ != 0:
    header = """
    {0} Analyzing Magnet Beam Energies in MeV

    {1}, Mass = {3:12.9f}, Frequency = {2:10.7f} MHz\tK = {4}
    """.format(NMRconfig.ACCELERATOR, ISO, FREQ, MASS, config.K)
  print header
  print "{0}".format("-"*80)

  # will be adjusting in loops
  qstart = Q1

  if E1 != 0:
    print "\tQ-Value\t\t\tFrequency\n{0}\n".format("-"*80)
    while qstart <= Q2:
      print "\t{0}\t\t\t{1}\n".format(qstart, getfrequency(E1, qstart))
      qstart += 1
  elif FREQ != 0:
    print "\tQ-Value\t\t\tEnergy\n{0}".format("-"*80)
    while qstart <= Q2:
      print "\t{0}\t\t\t{1}\n".format(qstart, getenergy(FREQ, qstart))
      qstart += 1

#####
# BASIC CALCULATIONS - Using calibration factor K from appropriate config file
#####
def getfrequency(energy, charge):
  from math import sqrt

  factor = energy / (MASS * config.ATOMEV)
  frequency = config.K * (MASS / charge) * sqrt(factor**2 + 2.0 * factor)

  return frequency

def getenergy(frequency, charge):
  from math import sqrt

  factor = ((frequency * charge)/(config.K * MASS))**2
  energy = MASS * config.ATOMEV * (sqrt(1 + factor) - 1)

  return energy

if __name__ == "__main__":
  main()
