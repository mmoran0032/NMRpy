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
  50.000   34.922069  52.000   35.614241  54.000   36.293259  56.000   36.959847
  50.500   35.096387  52.500   35.785199  54.500   36.461044  56.500   37.124631
  51.000   35.269847  53.000   35.955347  55.000   36.628064  57.000   37.288689
  51.500   35.442461  53.500   36.124697  55.500   36.794328  57.500   37.452031
  52.000   35.614241  54.000   36.293259  56.000   36.959847  58.000   37.614666
  52.500   35.785199  54.500   36.461044  56.500   37.124631  58.500   37.776604
  53.000   35.955347  55.000   36.628064  57.000   37.288689  59.000   37.937853

```
