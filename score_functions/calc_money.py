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

    # Create sample coordinates by using random
    coordinates = Coordinates(20, 180, 160).coordinates
    # print(coordinates)
    comparisons = []
    distances = []

    # Create 4-point coordinates for each house by making 3 large, 5 medium
    # and 12 small houses
    for i in range(20):
        y = coordinates[i]['y']
        x = coordinates[i]['x']
        if i < 3:
            temp = Coordinates_large(x, y)
        elif i < 8:
            temp = Coordinates_medium(x,y)
        else:
            temp = Coordinates_little(x,y)
        temp = temp.coordinates()
        comparisons.append(temp)

    # print(comparisons)
    # Create local variable that can't be a result value
    for s in range(len(comparisons)):
        selected = comparisons[s]
        # loop over all coordinates of selected house
        for i in range(4):
            minimum_distance = 9999.999
            # Loop over the list of houses to  select one
            for house in range(len(comparisons)):
                if comparisons[house] == selected:
                    break
                # Loop over all coordinates of the other houses
                for j in range(4):
                    temp = ((selected[0][i] - comparisons[house][0][j])**2 + (selected[1][i] - comparisons[house][1][j])**2)**0.5
                    # print(temp)
                    if temp < minimum_distance:
                        minimum_distance = temp
                        print(house, minimum_distance, sep='\t')
            temp = min(selected[0][i] - 0, 160 - selected[0][i], selected[1][i] - 0, 180 - selected[1][i])
            if temp < minimum_distance:
                minimum_distance = temp
                print("BOUNDS", minimum_distance, sep='\t')
        distances.append(minimum_distance)

    print(distances)
    return(distances)

if __name__ == "__main__":
    money = calc_money()
