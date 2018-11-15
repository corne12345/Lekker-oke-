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

    x = coordinates_1.coordinates()
    print(x)

if __name__ == "__main__":

    money = calc_money()
