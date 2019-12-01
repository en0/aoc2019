from sys import argv
from math import floor
from part_one import FuelCalculator, compute_module_fuel


def compute_module_fuel_with_fuel(mass: int) -> int:
    if mass <= 0:
        return 0
    mass = compute_module_fuel(mass)
    return mass + compute_module_fuel_with_fuel(mass)


def main(resource_path):
    fc = FuelCalculator(resource_path)
    fc.set_fuel_calculation(compute_module_fuel_with_fuel)
    print(fc.compute_total_fuel())


if __name__ == "__main__":
    main(argv[-1])
