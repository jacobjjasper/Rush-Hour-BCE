from car import Car
from truck import Truck
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class RushHour(object):
    """
    Rush Hour class for loading and playing Rush Hour
    """
    def __init__(self, game):
        self.fill_field(game)


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
                self.field[y_car][x_car] = vehicle

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
                self.field[y_car][x_car] = vehicle

    def fill_field(self, field):
        """
        Creates list of all vehicles from file and calls load_vehicle()
        """

        # create empty array of all vehicles
        self.vehicles = {}

        # open text file with rush hour field
        with open(field) as file:
            reader = file.readlines()

            # get field size
            self.size = int(reader[0][0])
            reader.pop(0)

            # build field with list comprehension
            self.field = [[0 for i in range(self.size)] for n in range(self.size)]

            # boolean for more than 9 vehicles in field
            under_10_vehicles = True

            # get every line in file
            for line in reader:

                # strip from \n
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
                self.vehicles[id] = new

        # call load_vehicle function for every vehicle in list
        for vehicle in self.vehicles.values():
            self.load_vehicle(vehicle)

        return self.field

    def show_field(self):
        """
        All matplotlib details for showing the Rush Hour board
        """
        # copy field to new variable
        print_field = self.field

        # change objects into their integers for printing
        for index, y in enumerate(print_field):
            for i, x in enumerate(y):
                if not isinstance(x, int):
                    print_field[index][i] = x.id

        # add ones around field
        print_field = np.pad(print_field, ((1,1),(1,1)), 'constant', constant_values=1)

        # add exit
        exit_row = self.size - (self.size // 2 + 1) + 1
        print_field[exit_row][-1] = 0

        # create colormap: 0 = white, 1 = black, 2(myCar) = red
        cmap = ListedColormap(['w', 'k', 'r', 'b', 'g', 'c', 'm', 'y', 'orange', 'grey', 'purple'])

        plt.matshow(print_field, cmap=cmap)
        col_labels = range(self.size, 0, -1)
        row_labels = range(1, self.size + 1)
        plt.xticks(range(1, self.size + 1), row_labels)
        plt.gca().xaxis.tick_bottom()
        plt.yticks(range(1, self.size + 1), col_labels)
        plt.show()



    def won(self):
        """
        Game is won
        """
        if self.vehicles[2].x == self.size - 1:
            print("You've won the game!")
            return True
        else:
            return False

    def move(self, id, move):
        """
        Move vehicle
        """
        vehicle = self.vehicles[id]

        # if move is to the right or up
        if move > 0:

            # if vehicle is placed horizontally
            if vehicle.orientation == 'H':

                # check for every block
                for i in range(move):

                    # if places in matrix are not 0
                    if self.field[self.size - vehicle.y][vehicle.x + vehicle.size - 1 + i] != 0:
                        print("can't move")
                        return

                # move vehicle
                vehicle.x += move

            elif vehicle.orientation == 'V':
                for i in range(move):
                    if self.field[self.size - (vehicle.y + vehicle.size + i)][vehicle.x - 1] != 0:
                        print("can't move")
                        return

                # move vehicle
                vehicle.y += move

        # if move is to the left or down
        if move < 0:

            # if vehicle is placed horizontally
            if vehicle.orientation == 'H':

                # check for every block
                for i in range(0, move, -1):

                    # if places in matrix are not 0
                    if self.field[self.size - vehicle.y][vehicle.x + i - 1] != 0:
                        print("can't move")
                        return

                # move vehicle
                vehicle.x += move

            elif vehicle.orientation == 'V':
                for i in range(0, move, -1):
                    if self.field[self.size - (vehicle.y + i - 1)][vehicle.x - 1] != 0:
                        print("can't move")
                        return

                # move vehicle
                vehicle.y += move


        # empty field
        for index, y in enumerate(self.field):
            for i, x in enumerate(y):
                    self.field[index][i] = 0

        # fill field with moved vehicle
        for vehicle in self.vehicles.values():
            self.load_vehicle(vehicle)

        self.show_field()

    def play(self):

        return True


        # while not self.won():
        #
        #     # promt user
        #     command = input("> ").upper()
        #
        #     self.move(int(command[0]), int(command.split(' ')[1]))



if __name__ == "__main__":
    rush = RushHour("../data/game1.txt")
    rush.show_field()
    rush.play()
