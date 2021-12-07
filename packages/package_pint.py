"""
Pint is a Python package to define,
 operate and manipulate physical quantities:
 the product of a numerical value and a unit
  of measurement.
 It allows arithmetic operations between them
 and conversions from and to different units.
"""

import pint

ureg = pint.UnitRegistry(system='mks')
print(3 * ureg.meter - 25 * ureg.cm)

f = 3, 5
unit = 'pounds'


def convert_to_system(f, unit, system='mks'):
    urged = pint.UnitRegistry(system=system)
    measurement = f * urged[unit]
    return measurement


def as_mks():
    measurement = convert_to_system(f, unit, system='mks')
    return measurement.to_base_units()


def as_imperial():
    measurement = convert_to_system(f, unit, system='imperial')
    return measurement.to_base_units()


print(convert_to_system(f, unit).to_base_units())
print(as_mks().to_base_units())
print(as_imperial())
