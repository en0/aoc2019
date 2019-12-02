import math
'''

Fuel required to launch a given module is based on its mass.
Specifically, to find the fuel required for a module,

take its mass,
divide by three,
round down,
and subtract 2.

Part II

Any mass that would require negative fuel should instead be treated as if it requires zero fuel
for each module mass, calculate its fuel and add it to the total

Then, treat the fuel amount you just calculated as the input mass and repeat the process, 
continuing until a fuel requirement is zero or negative

'''
total_fuel = 0
required_fuel_per_module = []
fuel_parts_total = 0


def calculate_fuel(mass: int):
    required_fuel = math.floor(mass / 3) - 2
    return required_fuel


def calculate_fuel_parts(fuel_amount: int):
    fuel_for_parts = calculate_fuel(fuel_amount)
    global fuel_parts_total
    # print(fuel_amount)
    if fuel_for_parts > 0:
        fuel_parts_total = fuel_parts_total + fuel_for_parts
        return calculate_fuel_parts(fuel_for_parts)
    else:
        return


with open('sample_resource.txt', 'r') as input_file:
    for module in input_file:
        fuel = calculate_fuel(int(module))
        required_fuel_per_module.append(fuel)
        total_fuel = total_fuel + fuel
        calculate_fuel_parts(fuel)
# print(total_fuel, required_fuel_per_module)

# print(f"fuel parts {fuel_parts_total} + total fuel {total_fuel} = {fuel_parts_total + total_fuel}")




