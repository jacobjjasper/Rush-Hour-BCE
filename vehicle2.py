
class Vehicle:

    #define global attributes vehicles
    def __init__(self, id, x, y, length, orientation):
        self.id = id

        if length == 2 or length == 3:
            self.length = length
        else:
            raise ValueError(f"Invalid length: {length}")

        if x in range(6):
            self.x = x
        else:
            raise ValueError(f"Invalid x: {x}")

        if y in range(6):
            self.y = y
        else:
            raise ValueError(f"Invalid y: {y}")

        if orientation.upper() == 'H':
            self.orientation = orientation
            self.x_end = self.x + (self.length - 1)
        elif orientation.upper() == 'V':
            self.orientation = orientation
            self.y_end = self.y + (self.length - 1)
        else:
            raise ValueError(f"Invalid orientation: {orientation}")

        # if self.x_end > 5:
        #     raise ValueError("Invalid position")
        # elif self.y_end > 5:
        #     raise ValueError("Invalid position")

if __name__ == "__main__":
    myCar = Vehicle(1, 2, 4, 2, "v")
    truck1 = Vehicle(2, 1, 1, 3, "h")
    car1 = Vehicle(3, 1, 5, 2, "v")
    print(myCar.id, myCar.x, myCar.y, myCar.length, myCar.orientation)
    print(truck1)
    print(car1)

    #
    # def load_vehicle():
    #     def load_vehicles(self, car_size, x, y, id, orientation):
    #         vehicles = []
    #
    #         # weg als car.py wordt gebruikt
    #         if y < 0:
    #             return print("Error: y negative")
    #         elif x < 0:
    #             return print("Error: x negative")
    #
    #         # horizontal
    #         if orientation.upper() == 'H':
    #
    #             # if vehicle is of size 2, fill 2 spots
    #             for i in range(car_size):
    #
    #                 # vehicle cannot go off the board
    #                 # weg als car.py wordt gebruikt
    #                 if x + car_size - 1 > self.size:
    #                     return print("Error too big")
    #
    #                 # input y = 1: y-coordinate = 0 (left bottom)
    #                 y_car = self.size - y
    #
    #                 # input x = 1: x-coordinate = 0
    #                 x_car = x - 1 + i
    #
    #                 # vehicle id on filled spot
    #                 self.field[y_car][x_car] = id
    #
    #         # vertical
    #         if orientation.upper() == 'V':
    #             for i in range(car_size):
    #
    #                 # vehicle cannot go off the board
    #                 # weg als car.py wordt gebruikt
    #                 if y + car_size - 1 > self.size:
    #                     return print("Error too big")
    #
    #                 # input y = 1: y-coordinate = 0 (left bottom)
    #                 y_car = self.size - y - i
    #
    #                 # input x = 1: x-coordinate = 0
    #                 x_car = x - 1
    #
    #                 # vehicle id on filled spot
    #                 self.field[y_car][x_car] = id
    #
    #
    #         return self.field
    #
    #
    #
    # def move_vehicle():
    #
    #
    #     self.options = []
    #
    #
    #
