import math

class Greed(object):
    def __init__(self):
        self.grid = self.grid()
        self.points = {}
        self.number_point = 1

    def grid(self):
        self.length = 180
        self.width = 160

    def calculate_degree(self):
        pi = math.pi
        degrees_horizontal = []
        degrees_vertical = []

        for count in range(1, 101):
            degree = 0.5 * pi * (count  / 100)
            if math.cos(degree) > 0.25 * pi:
                degrees_horizontal.append(math.cos(degree))
            else:
                degrees_vertical.append(math.sin(degree))

        return degrees_vertical, degrees_horizontal

    def calculate_point(self):
        # greedy algoritme
        while self.number_point < 20:
            sectors = {}
            degrees_vertical, degrees_horizontal = self.calculate_degree()
            max = []
            distances = []
            max_distance = 0
            max_degree = 0
            # calculate the first point with the greatest point
            if self.points == {}:
                self.points["point" + str(self.number_point)] =({"y": self.length/2, "x": self.width/2})

            else:

                # makes different sector
                if self.number_point == 1:
                    count = 0
                    for count in range(1, 5):

                        # sector1
                        sector_x = self.points["point" + str(self.number_point)]["x"]
                        sector_y = self.points["point" + str(self.number_point)]["y"]

                        if count == 2:
                            sector_x = self.width - sector_x

                        elif count == 3:
                            sector_y = self.length - sector_y

                        elif count == 4:
                            sector_x = self.width - sector_x
                            sector_y = self.length - sector_y

                        for degree in degrees_horizontal:
                            distances.append({"degree": degree, "distance": (sector_x/degree)})

                        for degree in degrees_vertical:
                            distances.append({"degree": degree, "distance": (sector_y/degree)})


                for key, values in sectors:
                    max_value = None
                    point = self.points["point" + str(self.number_point)]

                    if distances == []:
                        print("No Data")
                    else:
                        if float(distance["distance"]) > max_distance:
                            print(max_distance)
                            max_distance = distance["distance"]

                print(max_distance)

                break






if __name__ == "__main__":
    Greed().calculate_point()
