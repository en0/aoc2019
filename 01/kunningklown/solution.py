import math
'''

Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module,

take its mass,
divide by three,
round down,
and subtract 2.

'''
total_fuel = 0

with open('sample_resource.txt', 'r') as input_file:
    for module in input_file:
        mass = int(module)
        required_fuel = math.floor(mass / 3) - 2
        total_fuel = total_fuel + required_fuel


print(total_fuel)
