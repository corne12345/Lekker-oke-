from copy import deepcopy

class CheckHouse(object):
    def __init__(self, grid):
        self.grid = grid


    def check_coordinates(self, coordinates, house):
        corner_points = []

        house_length = house.length
        house_width = house.width
        for place in coordinates:
            point = {'y' : place['y'], 'x': place['x'] }

            # right under point
            corner_points.append(deepcopy(point))

            # left under point
            point['x']= point['x'] + int(house_width)
            corner_points.append(deepcopy(point))

            # left upper point
            point['y'] = point['y'] + int(house_length)
            corner_points.append(deepcopy(point))

            # right upper point
            point['x'] = point['x'] - int(house_width)
            corner_points.append(deepcopy(point))

            print(corner_points)
            # checks the points in the grid if there is already
            for xy_coordinate in corner_points:
                if xy_coordinate["y"] >= 180 or xy_coordinate["y"] < 0 or \
                xy_coordinate["x"] < 0 or xy_coordinate["x"]  >= 160 or \
                self.grid[xy_coordinate["y"]][xy_coordinate["x"]] in range(1, 5):
                    try:
                        print(self.grid[xy_coordinate["y"]][xy_coordinate["x"]])
                    except:
                        print("out of range")
                    place = coordinates.index(place)
                    return False, place
            corner_points = []
        return True, None
