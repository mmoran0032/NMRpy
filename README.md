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
the isotope tag (`-i, --iso`).

Options
-------

* `-e ENERGY, --energy ENERGY` Selects an energy to determine an NMR frequency
for. Cannot be combined with selecting a frequency.

* `-f FREQ, --frequency FREQ` Selects a frequency to use when determining the
beam energy. Cannot be combined with selecting an energy.

* `-h, --help` Prints the help screen.

* `-i, --iso` Selects an isotope. Defaults to Hydrogen-1 (H1) if none selected
and at least one other option present.

* `-q CHARGE, --charge CHARGE` Defines the desired charge state for the
calculation. If none is given the default is +1.

* `-v, --version` Prints version number and date of last update.

###Example

Alpha-particles with lab energy 7.5 MeV
```
nmrfreq.py -i he4 -q 2 -e 7.5
```
Output
```
Isoptope: HE4 (Z = 2, MASS = 4.00260325415 amu), Charge State: +2

    NMR FREQUENCY: 16.495194 MHz
    BEAM ENERGY:    7.500000 MeV
```
