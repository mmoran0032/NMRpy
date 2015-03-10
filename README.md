Analyzing Magnet NMR Utility
============================

Calculates the NMR frequency for a given isotope with a given charge state at a given energy. Designed for use at the Notre Dame Nuclear Structure Laboratory. Uses the [Atomic Mass Tables](http://ie.lbl.gov/toimass.html) by Audi, Wapstra, and Thibault (Nuc. Phys. A 729 (2003) 337-676). Supports both frequency-from-energy and energy-from-frequency calculations, with the former also allowing for tabular output.

When calculating, at the very least a single isotope, charge state, and energy/frequency is required. These are set using the respective options can can be organized is the following ways:
```
  ISO -sq QSTATE -se ENERGY
  ISO -sq QSTATE -sf FREQUENCY
  ISO -sq QSTATE -me ENERGY1 ENERGY2 ENERGYSTEP
  ISO -mq QSTATE1 QSTATE2 -se ENERGY
  ISO -mq QSTATE1 QSTATE2 -sf FREQUENCY
  ISO -mq QSTATE1 QSTATE2 -me ENERGY1 ENERGY2 ENERGYSTEP
```

Options
-------
* `-a, --accelerator` Prints which accelerator environment is currently selected.

* `-c` Changes the environment variables defined in NMRconfig.py. This option can be used in two different ways: restoring the options to their default (FN) with `nmrfreq -c` or setting a new defined (XXconfig.py exits) accelerator with `nmrfreq -c ACCELERATOR`

* `-h, --help` Prints the help screen.

* `-v, --version` Prints version number and date of last update.

* `-sq QSTATE` Defines a single charge state calculation.

  Sets the parser to only calculate for a single charge state. The routine can determine if it is a legitimate charge state, with the program exiting if the test is failed

* `-mq Q1 Q2`     Defines a multiple charge state calculation.

  Forces calculation for multiple charge states. The program will calculate frequencies for all charge states between Q1 and Q2, inclusive. No preference is given for defining the range as low-to-high or high-to-low, although output will always be in the low-to-high format.

* `-sf FREQ`      Defines a single frequency calculation.

  Using the supplied charge state(s), the program will determine the energy of the particle for the given frequency.

* `-se ENERGY`    Defines a single energy calculation.

  From the supplied information, the program calculates the NMR frequency at a single energy and displays it on the screen.

* `-me E1 E2 DE`  Defines a multiple energy calculation with a given energy step.

  Creates a tabular output of the NMR frequencies over the given energy range. The energies are displayed from lowest to highest, along with a header describing the isotope, charge states, and other important values. Energies may be input in either order.

  The default output in this mode is to a file: ISOTOPE+Q.nmr. This may be viewed in the terminal, with a screen width of at least 105 characters required to preserve formatting. Each charge state desired then has a separate file.

  For some energy ranges, the energy values will overshoot the final given energy in the tabular output. This effect is due to retaining the rectangular shape of the table. Since this is, at most, an additional four energies, this "feature" is retained without worry.

###Example

Alpha-particles with lab energy 7.5 MeV
```
nmrfreq.py he4 -sq 2 -se 7.5
```
Output
```
Isoptope: HE4 (Z = 2, MASS = 4.00260325415 amu), Charge State: +2

    NMR FREQUENCY: 16.495194 MHz
    BEAM ENERGY:    7.500000 MeV
```

Creating an `XXconfig.py` file
------------------------------

The program uses a relatively simple method of determining what accelerator it is calculating for, based on the configuration file. Only three numbers are required: ATOMEV (a known constant), K (magnetic calibration factor), and KERR (the uncertainty of the calibration, if available).

  The XXconfig.py file should look like the following (parsed from FNconfig.py):
```# Updated 2013-04-29 - Mike Moran (mmoran9@nd.edu)
      # Conversion from Mass to Mev - REQUIRED
      ATOMEV = 931.481
      # Calibration factor obtained by deBoer et al., 2013-04
      K = 129.88
      KERR = 0.05```

Additional comments, citations for the calibration factor, etc. are offset from the two variables by preceeding each line with the pound (#) character. Since the file is still a python file, additional blocks of code can be included for more advanced calculations but, since only ATOMEV and K are currently used by the program, defining new variables is unnecessary.

---------------

Utility Programs:

  `convertAWT.py`   Takes the 2003 Audi, Wapstra, and Thibault atomic mass tables (in text form, default location `2003AWTMass.dat`) and converts it into the actual dictionary used by the program. Since future mass table data files may have slightly different formatting, please take care when deciding to upgrade to the newest table.


Required files: masstable.py(c), FNconfig.py(c), SAconfig.py(c), NMRconfig.py(c)

Utilities: `convertAWT.py` (converts `2003AWTMass.dat` to `masstable.py`)
