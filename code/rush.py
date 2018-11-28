from vehicle import Vehicle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import copy
import heapq


class RushHour(object):
    """
    Rush Hour class for loading and playing Rush Hour
    """
    def __init__(self, board):
        self.make_first_field(board)

        # make field archive and add hash of initial field to the set
        self.archive = set()
        self.archive.add(self.create_hash(list(self.vehicles.values())))


    def make_first_field(self, field):
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

            # boolean for id's in field higher then 9
            two_digits = True

            # get every line in file
            for id, line in enumerate(reader, 2):

                # strip from \n
                line = line.strip()

                type = line[0]
                x = int(line[1])
                y = int(line[2])
                orientation = line[3]

                # make either car or truck, else print error
                if type == "C":
                    new = Vehicle(id, x, y, orientation, 2)
                elif type == "T":
                    new = Vehicle(id, x, y, orientation, 3)
                else:
                    print(line)

                # append object to list of vehicles
                self.vehicles[id] = new

        # call fill_field function on list of vehicles
        self.fill_field(list(self.vehicles.values()))

    def fill_field(self, vehicles):
        """
        Fills field with list of vehicles
        """

        # empty current field
        for index, y in enumerate(self.field):
            for i, x in enumerate(y):
                    self.field[index][i] = 0

        # fill current field
        for vehicle in vehicles:
            self.load_vehicle(vehicle)

        return True

    def load_vehicle(self, vehicle):
        """
        Loads one vehicle in matrix
        """

        # get attributes from vehicle object
        vehicle_length = vehicle.length
        x = vehicle.x
        y = vehicle.y
        id = vehicle.id
        orientation = vehicle.orientation

        # weg als car.py wordt gebruikt
        if y < 0:
            return print(f"Error: y negative for car {id}")
        elif x < 0:
            return print(f"Error: x negative for car {id}")

        # horizontal
        if orientation.upper() == 'H':

            # if vehicle is of size 2, fill 2 spots
            for i in range(vehicle_length):

                # vehicle cannot go off the board
                # weg als car.py wordt gebruikt
                if x + vehicle_length - 1 > self.size:
                    return print(f"Error too big for car {id}")

                # input y = 1: y-coordinate = 0 (left bottom)
                y_car = self.size - y

                # input x = 1: x-coordinate = 0
                x_car = x - 1 + i

                # vehicle id on filled spot
                self.field[y_car][x_car] = vehicle

        # vertical
        if orientation.upper() == 'V':
            for i in range(vehicle_length):

                # vehicle cannot go off the board
                # weg als car.py wordt gebruikt
                if y + vehicle_length - 1 > self.size:
                    return print(f"Error too big  for car {id}")

                # input y = 1: y-coordinate = 0 (left bottom)
                y_car = self.size - y - i

                # input x = 1: x-coordinate = 0
                x_car = x - 1

                # vehicle id on filled spot
                self.field[y_car][x_car] = vehicle

    def show_field(self):
        """
        All matplotlib details for showing the Rush Hour board
        """
        # copy field to new variable
        print_field = copy.deepcopy(self.field)


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
        all_colors = ['w', 'k', 'r', 'b', 'g', 'c', 'm', 'y', 'lime',
            'brown', 'purple', 'orange', 'grey', 'pink', 'darkred',
            'greenyellow', 'darkcyan', 'gold', 'darkgoldenrod', 'turquoise',
            'darkblue', 'darkgrey', 'darkkhaki', 'darkmagenta', 'darkturquoise',
            'deeppink', 'maroon', 'plum']
        colors = all_colors[0:len(self.vehicles) + 2]
        cmap = ListedColormap(colors)

        plt.matshow(print_field, cmap=cmap)
        col_labels = range(self.size, 0, -1)
        row_labels = range(1, self.size + 1)
        plt.xticks(range(1, self.size + 1), row_labels)
        plt.gca().xaxis.tick_bottom()
        plt.yticks(range(1, self.size + 1), col_labels)
        plt.show(block=False)
        plt.pause(0.0001)
        plt.close()
        # plt.show()

    def won(self):
        """
        Game is won
        """
        if self.field[self.size - (self.size // 2 + 1)][self.size - 1] == 0:
            return False
        else:
            if self.field[self.size - (self.size // 2 + 1)][self.size - 1].id == 2:
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
                    if self.field[self.size - vehicle.y][vehicle.x + vehicle.length - 1 + i] != 0:
                        print("can't move")
                        return

                # move vehicle
                vehicle.x += move

            elif vehicle.orientation == 'V':
                for i in range(move):
                    if self.field[self.size - (vehicle.y + vehicle.length + i)][vehicle.x - 1] != 0:
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



        # fill field with moved vehicle
        for vehicle in self.vehicles.values():
            self.load_vehicle(vehicle)


    def get_child_fields_1_step(self, vehicles):
        """ Comments """

        child_fields = []

        for vehicle in vehicles:

            x = vehicle.x
            y = vehicle.y

            # if vehicle is horizontal
            if vehicle.orientation == 'H':

                # if vehicle is not on left edge
                if x != 1:

                    # if not blocked by other vehicle
                    if self.field[self.size - y][x - 2] == 0:

                        # get parent field
                        new_vehicles = vehicles.copy()

                        # create new vehicle
                        new_vehicle = Vehicle(vehicle.id, x - 1, y, vehicle.orientation, vehicle.length)

                        # exchange old with new vehicle
                        new_vehicles[vehicle.id - 2] = new_vehicle

                        # add to child_fields
                        child_fields.append(new_vehicles)

                # if vehicle is not on right edge
                if x + vehicle.length - 1 != self.size:

                    # if not blocked by other vehicle
                    if self.field[self.size - y][x + vehicle.length - 1] == 0:
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x + 1, y, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

            # if vehicle is vertical
            if vehicle.orientation == 'V':

                # if vehicle is not on lower edge
                if y != 1:

                    # if not blocked by other vehicle
                    if self.field[self.size - (y - 1)][x - 1] == 0:
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x, y - 1, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

                # if vehicle is not on top edge
                if y + vehicle.length - 1 != self.size:

                    # if not blocked by other vehicle
                    if self.field[self.size - (y + vehicle.length)][x - 1] == 0:
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x, y + 1, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

        return child_fields

    def is_unique(self, field):
        """
        Return true if field is not in archive, calls hash function
        """

        # remember old length of archive (type: set)
        old_length = len(self.archive)

        # add hash value of field to archive
        self.archive.add(self.create_hash(field))

        # if it has been added, the field is unique
        if len(self.archive) > old_length:

            return True
        else:
            return False

    def create_hash(self, vehicles):
        """ Creates a unique respresentation of field """

        field = 0

        for i, vehicle in enumerate(vehicles):
            if vehicle.orientation == 'H':

                # add coordinate to integer field, as if it's made up of
                # single digits -> from the last car id until the red car
                field += vehicle.x * pow(10, i)
            else:
                field += vehicle.y * pow(10, i)

        return field


    def check_block(self, vehicles):
        """
        Checks whether a car is blocking the red car
        """

        # get red car's x
        my_car = vehicles[0]

        # if red car is on x = 4, the game is finished
        # return 0 means priority = 0, i.e. the highest priority
        if my_car.x == 5:
            return 0

        # start at prio = 1 when game is not yet finished
        blocking_vehicles = 1
        for vehicle in vehicles:
            # check for blocking vehicle
            # can only be vertically oriented, x must be greater than the red car's position
            # y must be smaller than or equal to the red car's y position, and y + length must
            # be greater than the red car's y position (car on y = 2 gives 2 + 2 = 4, but does
            # not block the read car). Therefore, y + length must be greater than the red
            # car's y coordinate.
            if vehicle.orientation == 'V' and vehicle.x >= (my_car.x + my_car.length) and vehicle.y <= my_car.y and (vehicle.y + vehicle.length) > my_car.y:
                # print()
                # print(my_car.x, my_car.y)
                # print(vehicle.id, vehicle.orientation, vehicle.x, vehicle.y)
                # print()
                blocking_vehicles += 1

        return blocking_vehicles

    def get_child_fields_whole_step(self, vehicles):
        """ Comments """

        child_fields = []

        for vehicle in vehicles:

            x = vehicle.x
            y = vehicle.y

            # if vehicle is horizontal
            if vehicle.orientation == 'H':

                # if vehicle is not on left edge
                if x != 1:

                    # if not blocked by other vehicle
                    if self.field[self.size - y][x - 2] == 0:

                        # check how many next blocks in field are 0
                        i = 0
                        while self.field[self.size - y][x - 2 - i] == 0:
                            i += 1

                            # break if next is not the edge
                            if x - i == 1:
                                break

                        # get parent field
                        new_vehicles = vehicles.copy()

                        # create new vehicle
                        new_vehicle = Vehicle(vehicle.id, x - i, y, vehicle.orientation, vehicle.length)

                        # exchange old with new vehicle
                        new_vehicles[vehicle.id - 2] = new_vehicle

                        # add to child_fields
                        child_fields.append(new_vehicles)

                # if vehicle is not on right edge
                if x + vehicle.length - 1 != self.size:

                    # if not blocked by other vehicle
                    if self.field[self.size - y][x + vehicle.length - 1] == 0:

                        i = 0
                        while self.field[self.size - y][x + vehicle.length - 1 + i] == 0:
                            i += 1
                            if x + vehicle.length - 1 + i == self.size:
                                break

                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x + i, y, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

            # if vehicle is vertical
            if vehicle.orientation == 'V':

                # if vehicle is not on lower edge
                if y != 1:

                    # if not blocked by other vehicle
                    if self.field[self.size - (y - 1)][x - 1] == 0:

                        i = 0
                        while self.field[self.size - (y - 1 - i)][x - 1] == 0:
                            i += 1
                            if y - i == 1:
                                break

                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x, y - i, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

                # if vehicle is not on top edge
                if y + vehicle.length - 1 != self.size:

                    # if not blocked by other vehicle
                    if self.field[self.size - (y + vehicle.length)][x - 1] == 0:

                        i = 0
                        while self.field[self.size - (y + vehicle.length + i)][x - 1] == 0:
                            i += 1
                            if y + vehicle.length - 1 + i == self.size:
                                break

                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x, y + i, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

        return child_fields


class PriorityQueue:

    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, board, priority):
        heapq.heappush(self.queue, (priority, self.index, board))
        self.index += 1

    def get_prio(self):
        return heapq.heappop(self.queue)[-1]

    def isempty(self):
        return len(self.queue) == 0
