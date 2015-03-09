nmrfreq.py - NSL Analyzing Magnet NMR Frequency Calculator
==========================================================

Version 0.9.17 - 2014-02-25 - Mike Moran (mmoran9@nd.edu)
---------------------------------------------------------

Calculates the NMR frequency for a given isotope with a given charge state at a given energy for the Notre Dame Nuclear Structure Laboratory. Uses the Atomic Mass Tables by Audi, Wapstra, and Thibault (Nuc. Phys. A 729 (2003) 337-676).

The input method takes the options directly from the command line and incorporates added functionality:
* can set a user-defined energy step when calculating multiple values, instead of forcing 0.025 MeV steps, and avoids printing extraneous values, and
* can calculate the energy for a given NMR frequency and charge state These options make for a cleaner end result and improve upon the base program.


Calling the routine has changed. The available potential calls are listed below and accessible through "nmrfreq.py -h" which includes short explanations of the command line tags. In addition, to maintain the same calling procedure, running the program without any options will default to the legacy interface.

Informative Options
-------------------

  -a            Prints which accelerator environment is used. Also available with --accelerator

  -h            Prints the help screen, with options and descriptions of tags. Also available with --help

  -v            Prints version number and date of last update. Also available with --version

Environment Options
-------------------

  -c            Changes the environment variables defined in NMRconfig.py. This option can be used in two different ways: restoring the options to their default (FN) with `nmrfreq -c` or setting a new defined (XXconfig.py exits) accelerator with `nmrfreq -c ACCELERATOR`

Calculating Options
-------------------

For all of the options below, the input must include a charge state definition and either an energy or a frequency definition, in that order. Anything else will return an error. Possible option sets are displayed using "-h" are are expanded below:

      ISO -sq QSTATE -se ENERGY
      ISO -sq QSTATE -sf FREQUENCY
      ISO -sq QSTATE -me ENERGY1 ENERGY2 ENERGYSTEP
      ISO -mq QSTATE1 QSTATE2 -se ENERGY
      ISO -mq QSTATE1 QSTATE2 -sf FREQUENCY
      ISO -mq QSTATE1 QSTATE2 -me ENERGY1 ENERGY2 ENERGYSTEP

The command line tags ensure that the program interprets the values given correctly and follows the order that the original program used. Each tag is defined below.

  -sq QSTATE    Defines a single charge state calculation.

                Sets the parser to only calculate for a single charge state. The routine can determine if it is a legitimate charge state, with the program exiting if the test is failed

  -mq Q1 Q2     Defines a multiple charge state calculation.

                Forces calculation for multiple charge states. The program will calculate frequencies for all charge states between Q1 and Q2, inclusive. No preference is given for defining the range as low-to-high or high-to-low, although output will always be in the low-to-high format.

  -sf FREQ      Defines a single frequency calculation.

                Using the supplied charge state(s), the program will determine the energy of the particle for the given frequency.

  -se ENERGY    Defines a single energy calculation.

                From the supplied information, the program calculates the NMR frequency at a single energy and displays it on the screen.

  -me E1 E2 DE  Defines a multiple energy calculation with a given energy step.

                Creates a tabular output of the NMR frequencies over the given energy range. The energies are displayed from lowest to highest, along with a header describing the isotope, charge states, and other important values. Energies may be input in either order.

                The default output in this mode is to a file: ISOTOPE+Q.nmr. This may be viewed in the terminal, with a screen width of at least 105 characters required to preserve formatting. Each charge state desired then has a separate file.

                For some energy ranges, the energy values will overshoot the final given energy in the tabular output. This effect is due to retaining the rectangular shape of the table. Since this is, at most, an additional four energies, this "feature" is retained without worry.

Examples:

  Alpha-particles with energies between 7.5 MeV and 11.5 MeV in 50 keV steps

      `nmrfreq.py he4 -sq 2 -me 7.5 11.5 0.05`


Creating a XXconfig.py file
---------------------------

The program uses a relatively simple method of determining what accelerator it is calculating for, based on the configuration file. Only three numbers are required: ATOMEV (a known constant), K (magnetic calibration factor), and KERR (the uncertainty of the calibration, if available).

  The XXconfig.py file should look like the following (parsed from FNconfig.py):

      # Updated 2013-04-29 - Mike Moran (mmoran9@nd.edu)
      # Conversion from Mass to Mev - REQUIRED
      ATOMEV = 931.481
      # Calibration factor obtained by deBoer et al., 2013-04
      K = 129.88
      KERR = 0.05

Additional comments, citations for the calibration factor, etc. are offset from the two variables by preceeding each line with the pound (#) character. Since the file is still a python file, additional blocks of code can be included for more advanced calculations but, since only ATOMEV and K are currently used by the program, defining new variables is unnecessary.

---------------

Utility Programs:

  `convertAWT.py`   Takes the 2003 Audi, Wapstra, and Thibault atomic mass tables (in text form) and converts it into the actual dictionary used by the program. Since future mass table data files may have slightly different formatting, please take care when deciding to upgrade to the newest table.

----------------

Eternal files:  masstable.py(c), FNconfig.py(c), SAconfig.py(c), NMRconfig.py(c)

Utilities:      convertAWT.py (2003AWTMass.dat)

Changelog:
  0.9.17 - Split README from program, removed generateRM.py, updated help information
  0.9.16 - Removed bash script and updated informative calls
  0.9.15 - Split legacy interface from program
  0.9.14 - Added error calculation to simple output
  0.9.13 - Shows Legacy flag when checking accelerator environment, bug fixes
  0.9.12 - Added functionality to edit NMRconfig from within the program
  0.9.11 - Added NMRconfig file to control set options
  0.9.10 - Added '-a' option
  0.9.9  - Final Beta Release
  0.9.4  - Added file output for energy range table (forced)
  0.9.3  - Initial beta release: full functionality aside from reading from and writing to a file
  0.9.2  - Finished tabular output from legacy interface
  0.9.1  - Added command line arguments
  0.9    - Initial file
