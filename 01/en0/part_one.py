from sys import argv
from math import floor
from typing import Callable


def compute_module_fuel(mass: int) -> int:
    """ Compute the amount of fuel required for the given mass"""
    fuel = max(floor(mass / 3) - 2, 0)
    #print(fuel)
    return fuel


class FuelCalculator:

    def __init__(self, source: str):
        self._source = source
        self._compute_module_fuel = compute_module_fuel

    def set_fuel_calculation(self, fuel_calculation: Callable[[int], int]):
        self._compute_module_fuel = fuel_calculation

    def compute_total_fuel(self):

        def _list_module_mass():
            with open(self._source, 'r') as fd:
                for line in fd:
                    yield int(line.rstrip('\n'))

        def _list_fuel_for_module():
            for mass in _list_module_mass():
                yield self._compute_module_fuel(mass)

        return sum(_list_fuel_for_module())


def main(resource_path):
    fc = FuelCalculator(resource_path)
    fc.set_fuel_calculation(compute_module_fuel)
    print(fc.compute_total_fuel())


if __name__ == "__main__":
    main(argv[-1])
