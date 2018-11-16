import sys

# get the path to the coordinates
sys.path.append(sys.path[0].replace('\\score_functions', '\\coordinates'))

from coordinate import *
from generator import *

def calc_money():
    """
    This function takes the length of the newly created detachement around the houses
    and calculates the money each house yields.
    """

    # Create sample coordinates
    coordinates = Coordinates(20, 180, 160).create_coordinates(20, 180, 160)
    print(coordinates)

    coordinates_1 = Coordinates_large(47, 87)
    coordinates_2 = Coordinates_large(38,75)
    coordinates_3 = Coordinates_large(20,20)
    # coordinates_4 =

    # Extends to full set of coordinates
    one = coordinates_1.coordinates()
    two = coordinates_2.coordinates()
    three = coordinates_3.coordinates()
    comparisons = [two, three]

    # Create local variable that can't be a result value
    minimum_distance = 9999.999

    # loop over all coordinates of selected house
    for i in range(4):
        # Loop over the list of houses to  select one
        for house in range(len(comparisons)):
            # Loop over all coordinates of the other houses
            for j in range(4):
                temp = ((one[0][i] - comparisons[house][0][j])**2 + (one[1][i] - comparisons[house][1][j])**2)**0.5
                # print(temp)
                if temp < minimum_distance:
                    minimum_distance = temp
        temp = min(one[0][i] - 0, 180 - one[0][i], one[1][i] - 0, 160 - one[1][i])
        if temp < minimum_distance:
            minimum_distance = temp

    print(minimum_distance)





if __name__ == "__main__":
    money = calc_money()
