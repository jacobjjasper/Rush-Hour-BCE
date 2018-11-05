from car import Car
from truck import Truck
import numpy as np
import matplotlib.pyplot as plt

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
        plt.matshow(rush.field)
        row_labels = ['6', '5', '4', '3', '2', '1']
        col_labels = ['1', '2', '3', '4', '5', '6']
        plt.xticks(range(6), col_labels)
        plt.gca().xaxis.tick_bottom()
        plt.yticks(range(6), row_labels)
        plt.show()

        return True


if __name__ == "__main__":
    rush = RushHour(6)
    rush.load_vehicles(2, 1, 1, 1, 'h')
    rush.load_vehicles(3, 1, 2, 2, 'v')
    rush.show_field()
    print(rush.field)
