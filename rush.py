from car import Car
from truck import Truck
# import numpy as np
import matplotlib.pyplot as plt

class RushHour(object):
    def __init__(self, size):
        self.size = size
        self.field = []


    def load_field(self):
        for i in range(self.size):
            self.field.append([0] * self.size)

        return self.field


    def load_vehicles(self, size, x, y, id, orientation):
        vehicles = []

        # horizontal
        if orientation.upper() == 'H':
            print(f"orient: {orientation}")
            for i in range(size):
                y_car = self.size - y
                x_car = x - 1 + i
                self.field[y_car][x_car] = id

        # vertical
        if orientation.upper() == 'V':
            for i in range(1, size + 1):
                y_car = self.size - y - 1 - i
                print(y_car)
                x_car = x - 1
                print(x_car)
                self.field[y_car][x_car] = id

        return self.field


    def fill_field(self, vehicles):

            return True



if __name__ == "__main__":
    rush = RushHour(6)
    rush.load_field()
    rush.load_vehicles(3, 1, 1, 1, 'H')
    plt.imshow(rush.field)
    plt.axis("off")
    plt.show()
    print(rush.field)
