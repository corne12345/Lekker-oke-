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
                        # print(house, minimum_distance, sep='\t')
            temp = min(selected[0][i] - 0, 160 - selected[0][i], selected[1][i] - 0, 180 - selected[1][i])
            if temp < minimum_distance:
                minimum_distance = temp
                # print("BOUNDS", minimum_distance, sep='\t')
        distances.append(minimum_distance)

    # print(distances)
    return(coordinates, distances)

def calc_validity(distances):
    """
    This function checks if the distances provided as a list as argument fulfill
    the constraints in terms of free space. It returns a boolean
    """
    for i in range(len(distances)):
        if i < 3:
            if distances[i] < 6:
                return False
                break
        elif i < 8:
            if distances[i] < 3:
                return False
                break
        else:
            if distances[i] < 2:
                return False
                break
    return True

def calc_score(distances):
    """
    This function takes the distances of all the houses to its closest neighbour
    as input and returns the worth of the neigborhood
    """
    worth = 0
    for i in range(len(distances)):
        if i < 3:
            factor = ((distances[i] - 6) * 6)/100 + 1
            price = 610000 * factor
            worth += price
        elif i < 8:
            factor = ((distances[i] - 3) * 4)/100 + 1
            price = 399000 * factor
            worth += price
        else:
            factor = ((distances[i] - 2) * 3)/100 + 1
            price = 285000 * factor
            worth += price

    return worth

if __name__ == "__main__":

    instances = 0
    max_worth = 0
    max_distances = []
    max_coordinates = []

    while(instances < 1000):
        money = []
        check = False
        while(check == False):
            outcome = calc_money()
            coordinates = outcome[0]
            distances = outcome[1]
            check = calc_validity(distances)
            print(check)

        instances += 1
        worth = calc_score(distances)
        if worth > max_worth:
            max_worth = worth
            max_coordinates = coordinates
            max_distances = distances

    # print(coordinates)
    # print(distances)
    # print(worth)

    print(max_worth)
    print(max_coordinates)
    print(max_distances)
