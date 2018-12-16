from copy import deepcopy

class CheckHouse(object):
    """
    Checks if coordinates of the houses satisfy the conditions.
    """

    def __init__(self, grid):
        self.grid = grid

    def check_coordinates(self, coordinates, house):
        corner_points = []
        house_length = house.length
        house_width = house.width

        # Checks every coordinate.
        for place in coordinates:
            point = {'y' : place['y'], 'x': place['x'] }

            # Appends the right under point.
            corner_points.append(deepcopy(point))

            # Appends the left under point.
            point['x']= point['x'] + int(house_width)
            corner_points.append(deepcopy(point))

            # Appends the left upper point.
            point['y'] = point['y'] + int(house_length)
            corner_points.append(deepcopy(point))

            # Appends the right upper point.
            point['x'] = point['x'] - int(house_width)
            corner_points.append(deepcopy(point))


            # # !!!!!!!!!! Nog checken of dit kan !!!!!!!!!!!!!!!!!!!!
            # # Appends the left under, upper and right upper points.
            # for dim in [('x', house_width), ('y', house_length), ('x', - house_width)]:
            #     point[dim[0]] = point[dim[0]] + int(dim[1])
            #     corner_points.append(deepcopy(point))

            # Checks the points in the grid if there are no houses in its range..
            for xy_coordinate in corner_points:
                if xy_coordinate["y"] >= 180 or xy_coordinate["y"] < 0 or \
                xy_coordinate["x"] < 0 or xy_coordinate["x"]  >= 160 or \
                self.grid[xy_coordinate["y"]][xy_coordinate["x"]] in range(1, 5):
                    try:
                        print(self.grid[xy_coordinate["y"]][xy_coordinate["x"]])
                    except:
                        print("Out of range!")
                    place = coordinates.index(place)

                    return False, place

            corner_points = []

        return True, None
