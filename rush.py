from car import Car
from truck import Truck
# import numpy as np
import matplotlib.pyplot as plt

class RushHour(object):
    def __init__(self, size):
        self.size = size
        self.field = []


    def load_field(self):

        # repeat size times for field height of size
        for i in range(self.size):

            # set field with to size
            self.field.append([0] * self.size)

        return self.field


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



if __name__ == "__main__":
    rush = RushHour(6)
    rush.load_field()
    rush.load_vehicles(3, 1, 100, 1, 'v')
    plt.imshow(rush.field)
    plt.axis("off")
    plt.show()

    for i in rush.field:
        print(i)
