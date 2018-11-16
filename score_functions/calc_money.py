import sys

# get the path to the coordinates
sys.path.append(sys.path[0].replace('\\score_functions', '\\coordinates'))

from coordinate import *

def calc_money():
    """
    This function takes the length of the newly created detachement around the houses
    and calculates the money each house yields.
    """
    coordinates_1 = Coordinates_large(0, 0)
    coordinates_2 = Coordinates_large(20,0)

    one = coordinates_1.coordinates()
    two = coordinates_2.coordinates()
    # print(one, two, sep='\n')

    for i in range(4):
        print(coordinates_1[0[i]] - coordinates_2[0[i]])


if __name__ == "__main__":
    money = calc_money()
