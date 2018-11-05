from car import Car
from truck import Truck
import numpy as np


class RushHour(object):
    def __init__(self, size):
        self.size = size
        self.field = []


    def load_field(self):
        for i in range(self.size):
            self.field.append([''] * self.size)

        return self.field


    def load_vehicles(self, size, x, y, id, orientation):
        vehicles = []
        # size = int(size)
        print(type(size))
        print(f"x = {x}")
        print(f"y={y}")
        print(id)
        print(orientation)


        # horizontal
        if orientation.upper() == 'H':
            print(f"orient: {orientation}")
            for i in range(size):
                y_car = self.size - y - 1
                x_car = x - 1
                self.field[y_car][x_car + i] = id

        # vertical
        if orientation.upper() == 'V':
            for i in range(size):
                y_car = self.size - y - 1
                print(y_car + i)
                x_car = x - 1
                self.field[y_car + i][x] = id

        return self.field


    def fill_field(self, vehicles):

            return True



if __name__ == "__main__":
    rush = RushHour(6)
    rush.load_field()
    rush.load_vehicles(2, 2, 0, 2, 'H')
    rush.load_vehicles(2, 0, 5, 3, 'V')
    print(rush.field)
