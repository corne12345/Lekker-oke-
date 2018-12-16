""""
This program calculates the state space of the Amstelhaege case for a set amount of houses.
"""

AMOUNT_HOUSES = 60
SMALL_HOUSES = int(0.6 * AMOUNT_HOUSES)
MEDIUM_HOUSES = int(0.25 * AMOUNT_HOUSES)
LARGE_HOUSES = int(0.15 * AMOUNT_HOUSES)

area_small = 64
options = 1

# Calculates the amount of options for each house
for i in range(SMALL_HOUSES):
    options_temp = (24864 - area_small * i)
    options *= options_temp

area_medium = 75
for i in range(MEDIUM_HOUSES):
    opp = 144 * 166.5 - SMALL_HOUSES * area_small
    options_temp = opp - i * area_medium
    options *= options_temp

area_large = 115.5
for i in range(LARGE_HOUSES):
    opp = 137 * 157.5 - SMALL_HOUSES * area_small - MEDIUM_HOUSES * area_medium
    options_temp = opp - i * area_large
    options *= options_temp

print(options)
