import sys

# get the path to the coordinates
sys.path.append(sys.path[0].replace('\\score_functions', '\\coordinates'))

from coordinate import *

def calc_money():
    """
    This function takes the length of the newly created detachement around the houses
    and calculates the money each house yields.
    """

    # Create sample coordinates
    coordinates_1 = Coordinates_large(0, 0)
    coordinates_2 = Coordinates_large(20,3)

    # Extends to full set of coordinates
    one = coordinates_1.coordinates()
    two = coordinates_2.coordinates()

    # Create local variable that can't be a result value
    minimum_distance = 9999.999

    # loop over all coordinates
    for i in range(4):
        for j in range(4):
            temp = ((one[0][i] - two[0][j])**2 + (one[1][i] - two[1][j])**2)**0.5
            # print(temp)
            if temp < minimum_distance:
                minimum_distance = temp
    print(minimum_distance)





if __name__ == "__main__":
    money = calc_money()
