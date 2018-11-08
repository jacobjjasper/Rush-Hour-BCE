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

        # create empty matrix with numpy function zeros
        self.field = np.zeros((size, size), dtype=int)


    def load_vehicles(self, car_size, x, y, id, orientation):
        vehicles = []

        # weg als car.py wordt gebruikt
        if y < 0:
            return print("Error: y negative")
        elif x < 0:
            return print("Error: x negative")

        # horizontal
        if orientation.upper() == 'H':

            # if vehicle is of size 2, fill 2 spots
            for i in range(car_size):

                # vehicle cannot go off the board
                # weg als car.py wordt gebruikt
                if x + car_size - 1 > self.size:
                    return print("Error too big")

                # input y = 1: y-coordinate = 0 (left bottom)
                y_car = self.size - y

                # input x = 1: x-coordinate = 0
                x_car = x - 1 + i

                # vehicle id on filled spot
                self.field[y_car][x_car] = id

        # vertical
        if orientation.upper() == 'V':
            for i in range(car_size):

                # vehicle cannot go off the board
                # weg als car.py wordt gebruikt
                if y + car_size - 1 > self.size:
                    return print("Error too big")

                # input y = 1: y-coordinate = 0 (left bottom)
                y_car = self.size - y - i

                # input x = 1: x-coordinate = 0
                x_car = x - 1

                # vehicle id on filled spot
                self.field[y_car][x_car] = id


        return self.field


    def fill_field(self, vehicles):

            return True

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
        cmap = ListedColormap(['w', 'k', 'r', 'b', 'g', 'c', 'm', 'y'])

        plt.matshow(rush.field, cmap=cmap)
        col_labels = range(self.size, 0, -1)
        row_labels = range(1, self.size + 1)
        plt.xticks(range(1, self.size + 1), row_labels)
        plt.gca().xaxis.tick_bottom()
        plt.yticks(range(1, self.size + 1), col_labels)
        plt.show()

        return True


if __name__ == "__main__":
    rush = RushHour(6)

    # my car (id = 2)
    rush.load_vehicles(2, 4, 4, 2, 'h')

    # other cars and trucks
    rush.load_vehicles(3, 3, 4, 3, 'v')
    rush.load_vehicles(3, 4, 1, 4, 'v')
    rush.load_vehicles(3, 6, 4, 5, 'v')
    rush.load_vehicles(2, 1, 1, 6, 'v')
    rush.load_vehicles(2, 2, 2, 7, 'h')
    rush.load_vehicles(2, 5, 1, 3, 'h')
    rush.load_vehicles(2, 5, 3, 3, 'h')
    rush.load_vehicles(2, 4, 6, 3, 'h')


    rush.show_field()
    print(rush.field)
