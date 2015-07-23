Analyzing Magnet NMR Utility
============================

Calculates the NMR frequency for a given isotope with a given charge state at a
given energy. Designed for use at the Notre Dame Nuclear Structure Laboratory.
Uses the [Atomic Mass Tables](http://ie.lbl.gov/toimass.html) by Audi, Wapstra,
and Thibault (Nuc. Phys. A 729 (2003) 337-676). Supports both frequency-from-
energy and energy-from-frequency calculations.

When calculating, the user inputs a combination of isotope, charge state, beam
energy, and frequency for the desired output. Depending on the options selected,
the program either performs the desired calculation or informs the uer that the
specific combinations are not usable.

The program defaults to selecting Hydrogen-1 and charge state +1 to ease
calculations for using proton beams. If no options are present, the help
information is printed.

The program also includes a basic isotope lookup (for mass and Z) by only using
the isotope tag. All isotopes included are stable or near stability and
frequently encountered at the Nuclear Science Lab at Notre Dame.

Options
-------

* `-h, --help` Prints the help screen.

* `-v, --version` Prints version number and date of last update.

* `-i, --iso` Selects an isotope. Defaults to Hydrogen-1 (H1) if none selected
  and at least one other option present.

* `-q CHARGE, --charge CHARGE` Defines the desired charge state for the
  calculation. If none is given the default is +1.

  You can select multiple charge states to calculate with by listing them after
  the `-q` option, and each calculation will be displayed one after the other.
  The output will automatically be from smallest to largest charge state.

* `-e ENERGY, --energy ENERGY` Selects an energy to determine an NMR frequency
  for. Cannot be combined with selecting a frequency.

  Either a single energy or a range of energies may be selected. When using a
  range, you supply three values: the starting energy, the ending energy, and
  the size of the energy step you'd like to take.

  *Note: the energy step must be smaller than your starting value. If you are
  not getting the results you expect for a range calculation, this may be the
  case.*

* `-f FREQ, --frequency FREQ` Selects a frequency to use when determining the
  beam energy. Cannot be combined with selecting an energy.

Examples
--------

Alpha-particles with lab energy 7.5 MeV
```
$ ./nmrfreq.py -i he4 -q 2 -e 7.5

Isotope: HE4 (Z = 2, mass = 4.00260325 amu), Charge State: +2    K = 129.88

         NMR FREQUENCY: 16.495194 MHz
         BEAM ENERGY:    7.500000 MeV
```

Sulfer-33 over a range of energies
```
$ ./nmrfreq.py -i s33 -q 7 -e 50 60 0.5

Isotope: S33 (Z = 16, mass = 32.97145876 amu), Charge State: +7    K = 129.88

  ENERGY  FREQUENCY   ENERGY  FREQUENCY   ENERGY  FREQUENCY   ENERGY  FREQUENCY 
--------------------------------------------------------------------------------
  50.000   30.556810  53.000   31.460929  56.000   32.339866  59.000   33.195622
  50.500   30.709339  53.500   31.609110  56.500   32.484052  59.500   33.336120
  51.000   30.861116  54.000   31.756602  57.000   32.627603  60.000   33.476031
  51.500   31.012153  54.500   31.903414  57.500   32.770527                    
  52.000   31.162461  55.000   32.049556  58.000   32.912833                    
  52.500   31.312049  55.500   32.195037  58.500   33.054529

```
