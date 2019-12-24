import math


def calculate_fuel(mass):
    """
    Calculate fuel for the module only.
    """
    return int(math.floor(mass / 3) - 2)


def calculate_total_fuel(mass, total_fuel=None):
    """
    Calculate fuel for the module and the fuel for the fuel.
    """
    fuel = calculate_fuel(mass)

    if fuel <= 0:
        return 0

    return fuel + calculate_total_fuel(mass=fuel, total_fuel=fuel)


with open('input.txt', 'r') as f:
    part_a_total = 0
    part_b_total = 0

    for line in f:
        mass = int(line)
        part_a_total += calculate_fuel(mass=mass)
        part_b_total += calculate_total_fuel(mass=mass)

    print('Total fuel for part A: {}'.format(part_a_total))
    print('Total fuel for part B: {}'.format(part_b_total))
