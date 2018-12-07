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

    def show_field2(self, vehicles, type):
        """
        Show vehicles in Rush Hour board
        Type is a boolean (T = continuous, F = static)
        """

        # get starting pixels x = 0, y = 0 on field image
        start_x = 78
        start_y = 45

        # block pixel width is slightly different per field size
        if self.size == 6:
            block_width = 72
        elif self.size == 9:
            block_width = 69
        elif self.size == 12:
            block_width = 68.5

        # get field without vehicles
        field = plt.imread(f"data/RushHourImages/RushHour{self.size}.jpg")

        # show field with subplots to park the vehicles
        fig, ax = plt.subplots()
        plt.imshow(field)
        plt.axis('off')

        # iterate through list of vehicles
        for vehicle in vehicles:
            x = vehicle.x
            y = vehicle.y

            # horizontal
            if vehicle.orientation == 'H':

                # give x and y their pixel coordinates
                x = start_x + (x * block_width)
                y = start_y + (y * block_width)

                # get car or truck image
                if vehicle.length == 2:
                    car = plt.imread(f"data/RushHourImages/Car{vehicle.id}.png")
                else:
                    car = plt.imread(f"data/RushHourImages/Truck{vehicle.id}.png")

                    # the image coordinate is his middle, which changes with the length of the car
                    x += 40

            # vertical
            if vehicle.orientation == 'V':

                # swap x and y starting coordinates
                x = start_y + (x * block_width)
                y = start_x + (y * block_width)

                # get image the same way, but rotated
                if vehicle.length == 2:
                    car = plt.imread(f"data/RushHourImages/Car-rotated{vehicle.id}.png")
                else:
                    car = plt.imread(f"data/RushHourImages/Truck-rotated{vehicle.id}.png")
                    y += 40

            # change the size of the vehicle images, depending on field size
            if self.size == 6:
                imagebox = OffsetImage(car, zoom=0.6)
            elif self.size == 9:
                imagebox = OffsetImage(car, zoom=0.4)
            elif self.size == 12:
                imagebox = OffsetImage(car, zoom=0.3)

            # place frame on vehicle to place on coordinate (set off frame after)
            imagebox.image.axes = ax
            xy = (x, y)
            ab = AnnotationBbox(imagebox, xy, frameon=False)
            ax.add_artist(ab)

        # show one field or close plot to show multiple continuously
        if type == True:
            plt.show(block=False)
            plt.pause(0.001)
            plt.close()
        else:
            plt.show()


    def won(self, vehicles):
        """
        Game is won
        """

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
        self.archive.add(self.create_hash_hex(field))

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

    def create_hash_hex(self, vehicles):
        """ Creates a unique respresentation of field """

        field = ""

        for i, vehicle in enumerate(vehicles):
            if vehicle.orientation == 'H':

                x = vehicle.x
                if x == 10:
                    x = "a"
                elif x == 11:
                    x = "b"
                field += str(x)
            else:
                y = vehicle.y
                if y == 10:
                    y = "a"
                elif y == 11:
                    y = "b"
                field += str(y)

        return field


    def cars_for_exit(self, vehicles):
        """
        Checks whether a car is blocking the red car.
        Heuristic: fewer cars between the red car and the exit makes for a
        higher priority.
        """

        self.fill_field(vehicles)

        # get red car's x
        my_car = vehicles[0]

        # if red car is on x = 4, the game is finished
        # return 0 means priority = 0, i.e. the highest priority
        if my_car.x == self.size - 2:
            return 0

        blocking_vehicles = 0
        blocks_to_exit = self.size - (my_car.x + 2)
        for i in range(blocks_to_exit):
            if not self.field[my_car.y][my_car.x + 2 + i] == 0:
                blocking_vehicles += 1

        return blocking_vehicles

    def cars_in_traffic(self, vehicles):
        self.fill_field(vehicles)

        prio = 0

        if vehicles[0].x == self.size - 2:
            return prio

        # check for first vehicle blocking
        i = 1
        while self.field[vehicles[0].y][vehicles[0].x + 1 + i] == 0:
            i += 1

            # return 0 if no vehicles blocking red car
            if vehicles[0].x + 1 + i == self.size:
                return 0

        # get first vehicle blocking exit
        vehicle = self.field[vehicles[0].y][vehicles[0].x + 1 + i]
        prio += 1

        archive = []
        archive.append(vehicle.id)

        # get vehicles that block current vehicle
        blocking_traffic = self.check_traffic(vehicle)

        while not len(blocking_traffic) == 0:

            # check blocking_traffic
            vehicle = blocking_traffic.pop(0)

            # if vehicle is checked, go to next
            if vehicle.id in archive:
                continue
            else:
                archive.append(vehicle.id)
                prio += 1



            list = self.check_traffic(vehicle)
            if len(list) == 0:
                break
            blocking_traffic.extend(list)


        return prio


    def check_traffic(self, vehicle):
        x = vehicle.x
        y = vehicle.y
        length = vehicle.length

        blocking_traffic = []

        if vehicle.orientation == 'V':

            # check below if other vehicle and if not edge
            if not y + length == self.size:
                if not self.field[y + length][x] == 0:
                    blocking_traffic.append(self.field[y + length][x])

            # check above
            if not y == 0:
                if not self.field[y - 1][x] == 0:
                    blocking_traffic.append(self.field[y - 1][x])

        # if vehicle is horizontal
        else:
            # check right
            if not x + length == self.size:
                if not self.field[y][x + length] == 0:
                    blocking_traffic.append(self.field[y][x + length])

            # check left
            if not x == 0:
                if not self.field[y][x - 1] == 0:
                    blocking_traffic.append(self.field[y][x - 1])

        return blocking_traffic

    def both(self, vehicles):
        return self.cars_for_exit(vehicles) + self.cars_in_traffic(vehicles)

    def play(self, game):
        """
        Show visualization of game being won (hardcoded)
        """
        if game == "1":
            self.move(6, -4)
            self.move(4, -1)
            self.move(8, 3)
            self.move(2, -3)
            self.move(7, -2)
            self.move(8, -2)
            self.move(9, -2)
            self.move(4, 4)
            self.move(9, 2)
            self.move(8, 2)
            self.move(2, 1)
            self.move(6, 4)
            self.move(2, -1)
            self.move(7, -1)
            self.move(8, -3)
            self.move(9, -3)
            self.move(3, -4)
            self.move(8, 3)
            self.move(9, 3)
            self.move(7, 3)
            self.move(2, 3)
            self.move(8, -3)
            self.move(3, 1)
            self.move(6, -4)
            self.move(3, -1)
            self.move(8, 3)
            self.move(2, -3)
            self.move(8, -2)
            self.move(9, -2)
            self.move(4, -4)
            self.move(5, -4)
            self.move(8, 2)
            self.move(9, 2)
            self.move(10, 3)
            self.move(2, 4)

            # leave red vehicle in place to show game is actually won
            for i in range(8):
                self.move(2, 0)




        elif game == "2":
            self.move(3, - 2)
            self.move(4, - 2)
            self.move(5, - 1)
            self.move(6, - 1)
            self.move(9, - 2)
            self.move(10, - 1)
            self.move(8, 2)
            self.move(2, - 1)
            self.move(7, 1)
            self.move(12, - 2)
            self.move(11, - 2)
            self.move(13, - 4)
            self.move(14, - 4)
            self.move(12, 2)
            self.move(8, - 1)
            self.move(10, 3)
            self.move(2, 3)
            for i in range(8):
                self.move(2, 0)

        elif game == "3":
            self.move(6, - 1)
            self.move(4, - 1)
            self.move(3, - 2)
            self.move(13, - 2)
            self.move(14, - 3)
            self.move(7, 2)
            self.move(11, 1)
            self.move(5, 3)
            self.move(11, - 1)
            self.move(8, - 1)
            self.move(7, - 3)
            self.move(11, 1)
            self.move(5, - 2)
            self.move(14, 3)
            self.move(13, 2)
            self.move(5, 2)
            self.move(2, 3)
            self.move(3, 2)
            self.move(9, - 1)
            self.move(7, - 1)
            self.move(2, 1)
            for i in range(8):
                self.move(2, 0)

        elif game == "4":
            self.move(15, 2)
            self.move(21, -1)
            self.move(22, -1)
            self.move(23, -1)
            self.move(18, 1)
            self.move(13, 1)
            self.move(3, 1)
            self.move(5, -1)
            self.move(6, -1)
            self.move(8, -3)
            self.move(7, 5)
            self.move(9, -1)
            self.move(10, -2)
            self.move(8, 4)
            self.move(6, 1)
            self.move(5, 5)
            self.move(6, -1)
            self.move(4, 4)
            self.move(3, -1)
            self.move(11, -2)
            self.move(2, -1)
            self.move(16, -5)
            self.move(14, 1)
            self.move(19, -1)
            self.move(20, -1)
            self.move(17, 1)
            self.move(12, 1)
            self.move(2, 7)
            for i in range(8):
                self.move(2, 0)

        elif game == "5":
            self.move(9, -3)
            self.move(7, 1)
            self.move(3, 1)
            self.move(13, -5)
            self.move(21, -5)
            self.move(12, -2)
            self.move(7, 2)
            self.move(8, -3)
            self.move(22, -2)
            self.move(19, -2)
            self.move(23, -2)
            self.move(14, 2)
            self.move(15, -1)
            self.move(24, -7)
            self.move(15, 1)
            self.move(14, -2)
            self.move(20, -3)
            self.move(16, 2)
            self.move(2, -2)
            self.move(10, 2)
            self.move(11, -3)
            self.move(6, 2)
            self.move(4, -1)
            self.move(18, -4)
            self.move(17, 1)
            self.move(10, 3)
            self.move(2, 3)
            for i in range(8):
                self.move(2, 0)

        elif game == "6":
            self.move(27, 1)
            self.move(19, 1)
            self.move(20, 1)
            self.move(17, 2)
            self.move(16, 1)
            self.move(3, -1)
            self.move(21, -1)
            self.move(7, -2)
            self.move(22, -2)
            self.move(20, 1)
            self.move(4, -1)
            self.move(10, -2)
            self.move(5, 1)
            self.move(20, 3)
            self.move(5, -1)
            self.move(10, 3)
            self.move(17, 1)
            self.move(19, -1)
            self.move(2, 7)
            for i in range(8):
                self.move(2, 0)

        elif game == "7":
            self.move(24, 1)
            self.move(20, -1)
            self.move(28, 1)
            self.move(13, 3)
            self.move(4, 3)
            self.move(9, -3)
            self.move(2, -1)
            self.move(14, -1)
            self.move(19, -1)
            self.move(10, -1)
            self.move(12, 2)
            self.move(16, -3)
            self.move(15, -1)
            self.move(22, 4)
            self.move(19, 1)
            self.move(14, 1)
            self.move(2, 1)
            self.move(9, 3)
            self.move(4, -3)
            self.move(13, -3)
            self.move(23, 1)
            self.move(20, 1)
            self.move(27, -6)
            self.move(23, -1)
            self.move(20, -1)
            self.move(38, -3)
            self.move(39, -1)
            self.move(43, -1)
            self.move(28, 2)
            self.move(13, 5)
            self.move(24, -1)
            self.move(4, 3)
            self.move(9, -2)
            self.move(11, -1)
            self.move(18, -2)
            self.move(2, 8)
            for i in range(8):
                self.move(2, 0)

    def move(self, id, move):
        """
        Move vehicle
        """
        vehicle = self.vehicles[id]
        

        # if vehicle is placed horizontally
        if vehicle.orientation == 'H' :

            # move vehicle
            self.vehicles[id].x += move

        elif vehicle.orientation == 'V':
            self.vehicles[id].y += move


        # fill field and show move quick
        self.fill_field(list(self.vehicles.values()))
        self.show_field2(list(self.vehicles.values()), True)


class PriorityQueue:
    """ Class for priority queue """
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
