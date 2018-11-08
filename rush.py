from car import Car
from truck import Truck
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class RushHour(object):
    """
    Rush Hour class for loading and playing Rush Hour
    """
    def __init__(self, size):
        self.size = size

        # create matrix of zeros with numpy
        self.field = np.zeros((size, size), dtype=int)


    def load_vehicle(self, vehicle):
        """
        Loads one vehicle in matrix
        """

        # get attributes from vehicle object
        vehicle_size = vehicle.size
        x = vehicle.x
        y = vehicle.y
        id = vehicle.id
        orientation = vehicle.orientation

        # weg als car.py wordt gebruikt
        if y < 0:
            return print("Error: y negative")
        elif x < 0:
            return print("Error: x negative")

        # horizontal
        if orientation.upper() == 'H':

            # if vehicle is of size 2, fill 2 spots
            for i in range(vehicle_size):

                # vehicle cannot go off the board
                # weg als car.py wordt gebruikt
                if x + vehicle_size - 1 > self.size:
                    return print("Error too big")

                # input y = 1: y-coordinate = 0 (left bottom)
                y_car = self.size - y

                # input x = 1: x-coordinate = 0
                x_car = x - 1 + i

                # vehicle id on filled spot
                self.field[y_car][x_car] = id

        # vertical
        if orientation.upper() == 'V':
            for i in range(vehicle_size):

                # vehicle cannot go off the board
                # weg als car.py wordt gebruikt
                if y + vehicle_size - 1 > self.size:
                    return print("Error too big")

                # input y = 1: y-coordinate = 0 (left bottom)
                y_car = self.size - y - i

                # input x = 1: x-coordinate = 0
                x_car = x - 1

                # vehicle id on filled spot
                self.field[y_car][x_car] = id


        return self.field


    def fill_field(self, field):
        """
        Creates list of all vehicles from file and calls load_vehicle()
        """

        # create empty array of all vehicles
        vehicles = []

        # open text file with rush hour field
        with open(field) as file:
            reader = file.readlines()

            # boolean for more than 9 vehicles in field
            under_10_vehicles = True

            # get every line in file, strip from \n
            for line in reader:
                line = line.strip()

                # type car (C) or truck (T)
                type = line[0]

                # if vehicle id is two digits (see .txt file)
                if line == "---":
                    under_10_vehicles = False
                    continue

                # vehicles with id < 10
                if under_10_vehicles:
                    id = int(line[1])
                    x = int(line[2])
                    y = int(line[3])
                    orientation = line[4]

                # vehicles with id >= 10
                else:
                    id = int(line[1] + line[2])
                    x = int(line[3])
                    y = int(line[4])
                    orientation = line[5]

                # make either car or truck, else print error
                if type == "C":
                    new = Car(id, x, y, orientation)
                elif type == "T":
                    new = Truck(id, x, y, orientation)
                else:
                    print(line)

                # append object to list of vehicles
                vehicles.append(new)

        # call load_vehicle function for every vehicle in list
        for vehicle in vehicles:
            rush.load_vehicle(vehicle)


    def show_field(self):
        """
        All matplotlib details for showing the Rush Hour board
        """

        # add ones around field
        rush.field = np.pad(rush.field, ((1,1),(1,1)), 'constant', constant_values=1)

        # add exit
        exit_row = self.size - (self.size // 2 + 1) + 1
        rush.field[exit_row][-1] = 0

        # create colormap: 0 = white, 1 = black, 2(myCar) = red
        cmap = ListedColormap(['w', 'k', 'r', 'b', 'g', 'c', 'm', 'y', 'orange', 'grey', 'purple'])

        plt.matshow(rush.field, cmap=cmap)
        col_labels = range(self.size, 0, -1)
        row_labels = range(1, self.size + 1)
        plt.xticks(range(1, self.size + 1), row_labels)
        plt.gca().xaxis.tick_bottom()
        plt.yticks(range(1, self.size + 1), col_labels)
        plt.show()



if __name__ == "__main__":
    rush = RushHour(6)
    rush.fill_field("game1.txt")
    rush.show_field()
