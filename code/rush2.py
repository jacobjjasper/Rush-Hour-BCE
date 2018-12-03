from vehicle import Vehicle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import copy
import heapq
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

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
            self.size = int(reader[0])
            reader.pop(0)

            # build field with list comprehension
            self.field = [[0 for i in range(self.size)] for n in range(self.size)]

            # get every line in file
            for id, line in enumerate(reader, 2):

                # strip from \n
                line = line.strip()

                if self.size > 10:
                    line = line.split()

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

        # horizontal
        if orientation.upper() == 'H':

            # if vehicle is of size 2, fill 2 spots
            for i in range(vehicle_length):

                # vehicle id on filled spot
                self.field[y][x + i] = vehicle

        # vertical
        if orientation.upper() == 'V':
            for i in range(vehicle_length):
                self.field[y + i][x] = vehicle

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
        all_colors = ['w', 'k', 'r',
                      'green', 'yellow', 'blue', 'orange', 'purple', 'cyan',
                      'magenta', 'lime', 'pink', 'teal', 'brown', 'maroon',
                      'olive', 'navy', 'grey',
                      'g', 'y', 'b', 'orange', 'purple', 'cyan', 'magenta',
                      'lime', 'pink', 'teal', 'brown', 'maroon',
                      'olive', 'navy', 'grey',
                      'g', 'y', 'b', 'orange', 'purple', 'cyan', 'magenta',
                      'lime', 'pink', 'teal', 'brown', 'maroon',
                      'olive', 'navy', 'grey']

        colors = all_colors[0:len(self.vehicles) + 2]
        cmap = ListedColormap(colors)

        plt.matshow(print_field, cmap=cmap)
        col_labels = range(self.size)
        row_labels = range(self.size)
        plt.xticks(range(1, self.size + 1), row_labels)
        plt.gca().xaxis.tick_bottom()
        plt.yticks(range(1, self.size + 1), col_labels)
        # plt.show(block=False)
        # plt.pause(0.0001)
        # plt.close()
        plt.show()

    def show_field2(self, vehicles):

        # horizontal
        x_coor_hor = [78, 151, 222, 294, 366]
        y_coor_hor = [49, 118, 192, 263, 331, 407]

        # vertical
        x_coor_vert = [43, 112, 183, 255, 326, 400]
        y_coor_vert = [80, 153, 226, 295, 371]

        # show field
        field = plt.imread('data2/RushHourImages/RushHour.jpg')

        fig, ax = plt.subplots()
        plt.imshow(field)
        plt.axis('off')

        for vehicle in vehicles:
            x = vehicle.x
            y = vehicle.y

            # horizontal
            if vehicle.orientation == 'H':
                x = x_coor_hor[x]
                y = y_coor_hor[y]
                if vehicle.length == 2:
                    car = plt.imread(f"data2/RushHourImages/Car{vehicle.id}.png")
                else:
                    car = plt.imread(f"data2/RushHourImages/Truck{vehicle.id}.png")
                    y += 40

            # vertical
            if vehicle.orientation == 'V':
                x = x_coor_vert[x]
                y = y_coor_vert[y]
                if vehicle.length == 2:
                    car = plt.imread(f"data2/RushHourImages/Car-rotated{vehicle.id}.png")
                else:
                    car = plt.imread(f"data2/RushHourImages/Truck-rotated{vehicle.id}.png")
                    y += 40

            imagebox = OffsetImage(car, zoom=0.6)
            imagebox.image.axes = ax
            xy = (x, y)
            ab = AnnotationBbox(imagebox, xy, frameon=False)
            ax.add_artist(ab)

        plt.show(block=False)
        plt.pause(0.0001)
        plt.close()

        # plt.show()


    def won(self, vehicles):
        """
        Game is won
        """
        # for i in range(self.size):
        #     if self.field[self.size//2 + 1][i] == 0 or 1:
        #
        #
        # first vehicle is always the red car
        return vehicles[0].x == self.size - 2


    def get_child_fields_1_step(self, vehicles):
        """ Comments """

        child_fields = []

        for vehicle in vehicles:

            x = vehicle.x
            y = vehicle.y

            # if vehicle is horizontal
            if vehicle.orientation == 'H':

                # if vehicle is not on left edge
                if x != 0:

                    # if not blocked by other vehicle
                    if self.field[y][x - 1] == 0:

                        # copy parent field
                        new_vehicles = vehicles.copy()

                        # create new vehicle
                        new_vehicle = Vehicle(vehicle.id, x - 1, y, vehicle.orientation, vehicle.length)

                        # exchange old with new vehicle, -2 because first vehicle id is 2
                        new_vehicles[vehicle.id - 2] = new_vehicle

                        # add to child_fields
                        child_fields.append(new_vehicles)

                # if vehicle is not on right edge
                if x + vehicle.length != self.size:

                    # if not blocked by other vehicle
                    if self.field[y][x + vehicle.length] == 0:
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x + 1, y, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

            # if vehicle is vertical
            if vehicle.orientation == 'V':

                # if vehicle is not on upper edge
                if y != 0:

                    # if not blocked by other vehicle, move up
                    if self.field[y - 1][x] == 0:
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x, y - 1, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

                # if vehicle is not on lower edge
                if y + vehicle.length != self.size:

                    # if not blocked by other vehicle, move down
                    if self.field[y + vehicle.length][x] == 0:
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x, y + 1, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

        return child_fields


    def get_child_fields_whole_step(self, vehicles):
        """ Comments """

        child_fields = []

        for vehicle in vehicles:

            x = vehicle.x
            y = vehicle.y

            # if vehicle is horizontal
            if vehicle.orientation == 'H':

                # if vehicle is not on left edge
                if x != 0:

                    # if not blocked by other vehicle, move left
                    if self.field[y][x - 1] == 0:

                        # check how many next blocks in field are 0
                        i = 0
                        while self.field[y][x - 1 - i] == 0:
                            i += 1

                            # break if next is not the edge
                            if x - i == 0:
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
                if x + vehicle.length != self.size:

                    # if not blocked by other vehicle, move right
                    if self.field[y][x + vehicle.length] == 0:

                        i = 0
                        while self.field[y][x + vehicle.length + i] == 0:
                            i += 1
                            if x + vehicle.length + i == self.size:
                                break

                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x + i, y, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

            # if vehicle is vertical
            if vehicle.orientation == 'V':

                # if vehicle is not on upper edge
                if y != 0:

                    # if not blocked by other vehicle, move up
                    if self.field[y - 1][x] == 0:

                        i = 0
                        while self.field[y - 1 - i][x] == 0:
                            i += 1
                            if y - i == 0:
                                break

                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x, y - i, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

                # if vehicle is not on lower edge
                if y + vehicle.length != self.size:

                    # if not blocked by other vehicle, move down
                    if self.field[y + vehicle.length][x] == 0:

                        i = 0
                        while self.field[y + vehicle.length + i][x] == 0:
                            i += 1
                            if y + vehicle.length + i == self.size:
                                break

                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, x, y + i, vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

        return child_fields


    def get_child_fields_every_step(self, vehicles):
        """ Comments """

        child_fields = []

        for vehicle in vehicles:

            x = vehicle.x
            y = vehicle.y

            # if vehicle is horizontal
            if vehicle.orientation == 'H':

                # if vehicle is not on left edge
                if x != 0:

                        # check how many next blocks in field are 0
                        i = 1
                        while self.field[y][x - i] == 0:

                            # get parent field
                            new_vehicles = vehicles.copy()

                            # create new vehicle
                            new_vehicle = Vehicle(vehicle.id, x - i, y, vehicle.orientation, vehicle.length)

                            # exchange old with new vehicle
                            new_vehicles[vehicle.id - 2] = new_vehicle

                            # add to child_fields
                            child_fields.append(new_vehicles)

                            # break if next is on the edge
                            if x - i == 0:
                                break
                            else:

                                # go to next place
                                i += 1


                # if vehicle is not on right edge
                if x + vehicle.length != self.size:

                        i = 1
                        while self.field[y][x + vehicle.length - 1 + i] == 0:
                            new_vehicles = vehicles.copy()
                            new_vehicle = Vehicle(vehicle.id, x + i, y, vehicle.orientation, vehicle.length)
                            new_vehicles[vehicle.id - 2] = new_vehicle
                            child_fields.append(new_vehicles)

                            if x + vehicle.length + i == self.size:
                                break
                            else:
                                i += 1

            # if vehicle is vertical
            if vehicle.orientation == 'V':

                # if vehicle is not on upper edge
                if y != 0:

                        i = 1
                        while self.field[y - i][x] == 0:
                            new_vehicles = vehicles.copy()
                            new_vehicle = Vehicle(vehicle.id, x, y - i, vehicle.orientation, vehicle.length)
                            new_vehicles[vehicle.id - 2] = new_vehicle
                            child_fields.append(new_vehicles)

                            if y - i == 0:
                                break
                            else:
                                i += 1

                # if vehicle is not on lower edge
                if y + vehicle.length != self.size:

                        i = 1
                        while self.field[y + vehicle.length - 1 + i][x] == 0:
                            new_vehicles = vehicles.copy()
                            new_vehicle = Vehicle(vehicle.id, x, y + i, vehicle.orientation, vehicle.length)
                            new_vehicles[vehicle.id - 2] = new_vehicle
                            child_fields.append(new_vehicles)

                            if y + vehicle.length + i == self.size:
                                break
                            else:
                                i += 1

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
        return len(self.archive) > old_length


    def create_hash(self, vehicles):
        """ Creates a unique respresentation of field """

        field = 0

        for i, vehicle in enumerate(vehicles):
            if vehicle.orientation == 'H':

                # add coordinate to integer field, as if it's made up of
                # single digits -> from the last car id until the red car
                # coordinate + 1, because multiplying with 0 doesn't work
                # this only works for fields 9 x 9 or smaller
                x = vehicle.x + 1
                field += x * pow(10, i)
            else:
                y = vehicle.y + 1
                field += y * pow(10, i)

        return field


    def check_block(self, vehicles):
        """
        Checks whether a car is blocking the red car.
        Heuristic: fewer cars between the red car and the exit makes for a
        higher priority.
        """

        # get red car's x
        my_car = vehicles[0]

        # if red car is on x = 4, the game is finished
        # return 0 means priority = 0, i.e. the highest priority
        if my_car.x == 5:
            return 0

        # start at prio = 1 or (prio = 0??) when game is not yet finished
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
