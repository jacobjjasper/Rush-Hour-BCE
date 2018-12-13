""" Module containing the RushHour object. """
from vehicle import Vehicle
import numpy as np
import matplotlib.pyplot as plt
import copy
import heapq
from matplotlib.offsetbox import OffsetImage, AnnotationBbox


class RushHour(object):
    """ Rush Hour class for loading and playing Rush Hour.

    Attributes:
    board -- directory in data folder of the game to be solved

    Methods:
    make_first_field -- make initial field
    fill_field -- fill a field with vehicles
    load_vehicle -- helper function for fill_field
    show_field -- visualise the board
    won -- check whether game is won
    get_child_fields_1_step -- get child fields, moving vehicles one coordinate
    get_child_fields_every_step -- get child fields, moving vehicles to every
                                   possible coordinate
    get_child_fields_whole_step -- get child fields, moving vehicles to the
                                   furthest possible coordinate
    is_unique -- check whether a field configuration has already been made
    create_hash -- helper function for is_unique
    create_hash_hex -- helper function for is_unique
    cars_to_exit -- heuristic checking the number of vehicles blocking the red car
    cars_in_traffic -- heuristic checking the number of vehicles to be moved in order
                       to move the red car
    check_traffic -- helper function for cars_in_traffic
    play -- hardcoded solution for games 1 to 7
    move -- helper function for play
    """


    def __init__(self, board):
        self.make_first_field(board)
        self.archive = set()
        self.archive.add(self.create_hash(list(self.vehicles.values())))


    def make_first_field(self, field):
        """ Create initial field from text file. Parse the text file to get the
        field size and each vehicle's properties. Also, initialise the field
        to be filled.

        Keyword arguments:
        field -- directory in data folder of the game to be solved
        """

        self.vehicles = {}

        with open(field) as file:
            reader = file.readlines()
            self.size = int(reader[0])
            reader.pop(0)
            self.field = [[0 for i in range(self.size)] for n in range(self.size)]

            for id, line in enumerate(reader, 2):
                line = line.strip()
                if self.size > 10:
                    line = line.split()
                type = line[0]
                x = int(line[1])
                y = int(line[2])
                orientation = line[3]
                if type == "C":
                    new = Vehicle(id, x, y, orientation, 2)
                elif type == "T":
                    new = Vehicle(id, x, y, orientation, 3)
                else:
                    print(line)
                self.vehicles[id] = new

        self.fill_field(list(self.vehicles.values()))


    def fill_field(self, vehicles):
        """ Fill field with vehicle objects. First, empty the current field.
        Then, call load_vehicle to fill the field with vehicle objects.

        Keyword arguments:
        vehicles -- list of vehicle objects
        """

        for index, y in enumerate(self.field):
            for i, x in enumerate(y):
                    self.field[index][i] = 0

        for vehicle in vehicles:
            self.load_vehicle(vehicle)


    def load_vehicle(self, vehicle):
        """ Load one vehicle objects into the field matrix.

        Keyword arguments:
        vehicle -- vehicle object to be loaded into the field
        """

        if vehicle.orientation.upper() == 'H':
            for i in range(vehicle.length):
                self.field[vehicle.y][vehicle.x + i] = vehicle

        if vehicle.orientation.upper() == 'V':
            for i in range(vehicle.length):
                self.field[vehicle.y + i][vehicle.x] = vehicle


    def show_field(self, vehicles, type):
        """ Show vehicles on Rush Hour board. Retreive background and vehicles
        images from data folder and place vehicles on their coordinates corresponding
        to pixels on the image/plot. Can show 6x6, 9x9 and 12x12 fields.

        Keyword arguments:
        vehicles -- list of vehicle objects to be shown
        type -- boolean (True = continuous representation, False = static representation)
        """

        # starting pixels x = 0, y = 0 on field image
        start_x = 78
        start_y = 45

        # block pixel width is slightly different per field size
        if self.size == 6:
            block_width = 72
        elif self.size == 9:
            block_width = 69
        elif self.size == 12:
            block_width = 68.5

        field = plt.imread(f"data/RushHourImages/RushHour{self.size}.jpg")
        fig, ax = plt.subplots()
        plt.imshow(field)
        plt.axis('off')

        for vehicle in vehicles:
            if vehicle.orientation == 'H':
                x = start_x + (vehicle.x * block_width)
                y = start_y + (vehicle.y * block_width)
                if vehicle.length == 2:
                    car = plt.imread(f"data/RushHourImages/Car{vehicle.id}.png")
                else:
                    car = plt.imread(f"data/RushHourImages/Truck{vehicle.id}.png")

                    # truck: the image coordinate is his middle, which changes with the length of the car
                    x += 40

            if vehicle.orientation == 'V':
                x = start_y + (vehicle.x * block_width)
                y = start_x + (vehicle.y * block_width)
                if vehicle.length == 2:
                    car = plt.imread(f"data/RushHourImages/Car-rotated{vehicle.id}.png")
                else:
                    car = plt.imread(f"data/RushHourImages/Truck-rotated{vehicle.id}.png")
                    y += 40

            if self.size == 6:
                imagebox = OffsetImage(car, zoom=0.6)
            elif self.size == 9:
                imagebox = OffsetImage(car, zoom=0.4)
            elif self.size == 12:
                imagebox = OffsetImage(car, zoom=0.3)

            imagebox.image.axes = ax
            xy = (x, y)
            ab = AnnotationBbox(imagebox, xy, frameon=False)
            ax.add_artist(ab)

        if type == True:
            plt.show(block=False)
            plt.pause(0.001)
            plt.close()
        else:
            plt.show()


    def won(self, vehicles):
        """ Check whether the game is won. Check whether the red car is situated
        in front of the exit. Return a boolean True when won, else False.

        Keyword arguments:
        vehicles -- list of vehicle objects
        """

        return vehicles[0].x == self.size - 2


    def get_child_fields_1_step(self, vehicles):
        """ Get child fields, moving vehicles one coordinate. The function is
        dependent on self.field being filled by the fill_field function. Return
        a list containing lists of possible vehicle configurations.

        Keyword arguments:
        vehicles -- list of vehicle objects
        """

        child_fields = []
        for vehicle in vehicles:
            if vehicle.orientation == 'H':

                # move left
                if vehicle.x != 0:
                    if self.field[vehicle.y][vehicle.x - 1] == 0:
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, vehicle.x - 1, vehicle.y,
                                              vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

                # move right
                if vehicle.x + vehicle.length != self.size:
                    if self.field[vehicle.y][vehicle.x + vehicle.length] == 0:
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, vehicle.x + 1, vehicle.y,
                                              vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

            if vehicle.orientation == 'V':

                # move up
                if vehicle.y != 0:
                    if self.field[vehicle.y - 1][vehicle.x] == 0:
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, vehicle.x, vehicle.y - 1,
                                              vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

                # move down
                if y + vehicle.length != self.size:
                    if self.field[vehicle.y + vehicle.length][vehicle.x] == 0:
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, vehicle.x, vehicle.y + 1,
                                              vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

        return child_fields


    def get_child_fields_every_step(self, vehicles):
        """ Get child fields, moving vehicles to every possible coordinate.
        The function is dependent on self.field being filled by the fill_field function.
        Return a list containing lists of possible vehicle configurations.

        Keyword arguments:
        vehicles -- list of vehicle objects
        """

        child_fields = []
        for vehicle in vehicles:

            if vehicle.orientation == 'H':

                # move left
                if vehicle.x != 0:
                        i = 1
                        while self.field[vehicle.y][vehicle.x - i] == 0:
                            new_vehicles = vehicles.copy()
                            new_vehicle = Vehicle(vehicle.id, vehicle.x - i, vehicle.y,
                                                  vehicle.orientation, vehicle.length)
                            new_vehicles[vehicle.id - 2] = new_vehicle
                            child_fields.append(new_vehicles)
                            if vehicle.x - i == 0:
                                break
                            else:
                                i += 1

                # move right
                if vehicle.x + vehicle.length != self.size:
                        i = 1
                        while self.field[vehicle.y][vehicle.x + vehicle.length - 1 + i] == 0:
                            new_vehicles = vehicles.copy()
                            new_vehicle = Vehicle(vehicle.id, vehicle.x + i, vehicle.y,
                                                  vehicle.orientation, vehicle.length)
                            new_vehicles[vehicle.id - 2] = new_vehicle
                            child_fields.append(new_vehicles)
                            if vehicle.x + vehicle.length + i == self.size:
                                break
                            else:
                                i += 1

            if vehicle.orientation == 'V':

                # move up
                if vehicle.y != 0:
                        i = 1
                        while self.field[vehicle.y - i][vehicle.x] == 0:
                            new_vehicles = vehicles.copy()
                            new_vehicle = Vehicle(vehicle.id, vehicle.x, vehicle.y - i,
                                                  vehicle.orientation, vehicle.length)
                            new_vehicles[vehicle.id - 2] = new_vehicle
                            child_fields.append(new_vehicles)
                            if y - i == 0:
                                break
                            else:
                                i += 1

                # move down
                if vehicle.y + vehicle.length != self.size:
                        i = 1
                        while self.field[vehicle.y + vehicle.length - 1 + i][vehicle.x] == 0:
                            new_vehicles = vehicles.copy()
                            new_vehicle = Vehicle(vehicle.id, vehicle.x, vehicle.y + i,
                                                  vehicle.orientation, vehicle.length)
                            new_vehicles[vehicle.id - 2] = new_vehicle
                            child_fields.append(new_vehicles)
                            if vehicle.y + vehicle.length + i == self.size:
                                break
                            else:
                                i += 1

        return child_fields


    def get_child_fields_whole_step(self, vehicles):
        """ Get child fields, moving vehicles to their furthest possible coordinate.
        The function is dependent on self.field being filled by the fill_field function.

        Keyword arguments:
        vehicles -- list of vehicle objects
        """

        child_fields = []
        for vehicle in vehicles:
            if vehicle.orientation == 'H':

                # move left
                if vehicle.x != 0:
                    if self.field[vehicle.y][vehicle.x - 1] == 0:
                        i = 0
                        while self.field[vehicle.y][vehicle.x - 1 - i] == 0:
                            i += 1
                            if vehicle.x - i == 0:
                                break
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, vehicle.x - i, vehicle.y,
                                              vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

                # move right
                if vehicle.x + vehicle.length != self.size:
                    if self.field[vehicle.y][vehicle.x + vehicle.length] == 0:
                        i = 0
                        while self.field[vehicle.y][vehicle.x + vehicle.length + i] == 0:
                            i += 1
                            if vehicle.x + vehicle.length + i == self.size:
                                break
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, vehicle.x + i, vehicle.y,
                                              vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

            if vehicle.orientation == 'V':

                # move up
                if vehicle.y != 0:
                    if self.field[vehicle.y - 1][vehicle.x] == 0:
                        i = 0
                        while self.field[vehicle.y - 1 - i][vehicle.x] == 0:
                            i += 1
                            if vehicle.y - i == 0:
                                break
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, vehicle.x, vehicle.y - i,
                                              vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

                # move down
                if vehicle.y + vehicle.length != self.size:
                    if self.field[vehicle.y + vehicle.length][vehicle.x] == 0:
                        i = 0
                        while self.field[vehicle.y + vehicle.length + i][vehicle.x] == 0:
                            i += 1
                            if vehicle.y + vehicle.length + i == self.size:
                                break
                        new_vehicles = vehicles.copy()
                        new_vehicle = Vehicle(vehicle.id, vehicle.x, vehicle.y + i,
                                              vehicle.orientation, vehicle.length)
                        new_vehicles[vehicle.id - 2] = new_vehicle
                        child_fields.append(new_vehicles)

        return child_fields


    def is_unique(self, field):
        """ Check whether a field configuration has already been made by storing
        it in an archive set. Hash field using create_hash function. Return true
        if field is not in archive, thus being unique.

        Keyword arguments:
        field -- list of vehicle objects
        """

        old_length = len(self.archive)
        self.archive.add(self.create_hash(field))
        return len(self.archive) > old_length


    def create_hash(self, vehicles):
        """ Create a unique respresentation of the field. The field is represented
        by an integer. Every vehicle is represented by a single digit in this
        integer, ordered by id: vehicle 1 will always be on the last place of the
        integer, vehicle 2 will be represented on the second to last place, et cetera.
        This order is always maintained, as the get_child_fields functions render
        lists of vehicles ordered based on their id. To avoid multiplying by a
        value of 0, 1 is added to every coordinate (which can be 0). This hash
        function does not work on fields larger than 9x9. Return the hash integer.

        Keyword arguments:
        vehicles -- list of vehicle objects
        """

        field = 0
        for i, vehicle in enumerate(vehicles):
            if vehicle.orientation == 'H':
                x = vehicle.x + 1
                field += x * pow(10, i)
            else:
                y = vehicle.y + 1
                field += y * pow(10, i)
        return field


    def create_hash_hex(self, vehicles):
        """ Create a unique respresentation of fields larger than 9x9. The field
        is represented in a string. Every vehicle is represented by a single character
        in this string, ordered by id: vehicle 1 will always be on the first place of the
        string, vehicle 2 will be represented on place two, et cetera. This order
        is always maintained, as the get_child_fields functions render lists of
        vehicles ordered based on their id. This function is made especially
        for fields of size 12x12. Return the hash string.

        Keyword arguments:
        vehicles -- list of vehicle objects
        """

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


    def cars_to_exit(self, vehicles):
        """ Heuristic: check how many cars are blocking the red car from leaving
        the board. Fewer cars between the red car and the exit eventually make
        for a higher priority, as the boards score is dependent on the number of
        cars between the red car and the exit.
        First, fill the field with vehicle objects. Check whether the red car,
        which is on index 0 of the vehicles list, is blocked by other vehicles.
        For every vehicle blocking the car, add 1 to blocking_vehicles. Return
        blocking_vehicles.

        Keyword arguments:
        vehicles -- list of vehicle objects
        """

        self.fill_field(vehicles)
        blocking_vehicles = 0

        if won(vehicles):
            return blocking_vehicles

        blocks_to_exit = self.size - (vehicles[0].x + 2)
        for i in range(blocks_to_exit):
            if not self.field[vehicles[0].y][vehicles[0].x + 2 + i] == 0:
                blocking_vehicles += 1

        return blocking_vehicles


    def cars_in_traffic(self, vehicles):
        """ Heuristic: starting from the red car, check how many vehicles need
        to be moved before the red car can move towards the exit.
        First, fill the field with vehicle objects. Check whether the red car,
        which is on index 0 of the vehicles list, can move towards the exit.
        If the car is blocked, add 1 to prio and check whether the blocking vehicle
        can move using the function check_traffic. If not, add 1 to prio and check
        whether its blocking vehicle can move, et cetera. Store which vehicles
        have already been checked, to prevent ending up in a loop. If a vehicle can
        indeed move, return prio.

        Keyword arguments:
        vehicles -- list of vehicle objects
        """

        self.fill_field(vehicles)
        prio = 0

        if won(vehicles):
            return prio

        # get first vehicle blocking exit
        i = 1
        while self.field[vehicles[0].y][vehicles[0].x + 1 + i] == 0:
            i += 1
            if vehicles[0].x + 1 + i == self.size:
                return prio
        vehicle = self.field[vehicles[0].y][vehicles[0].x + 1 + i]
        prio += 1

        archive = []
        archive.append(vehicle.id)
        blocking_traffic = self.check_traffic(vehicle)

        while not len(blocking_traffic) == 0:
            vehicle = blocking_traffic.pop(0)
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
        """ Helper function for cars_in_traffic. Check whether a vehicle is
        blocked by another vehicle. Relies on self.field to be filled beforehand
        with vehicle objects, which should happen in the cars_in_traffic function.
        Check whether the car can move one block in its orientaion. If a vehicle
        is blocking its movement. Append the blocking vehicle to blocking_traffic.
        Return blocking_traffic.

        Keyword arguments:
        vehicle -- vehicle object
        """

        blocking_traffic = []

        # check both down and up
        if vehicle.orientation == 'V':
            if not vehicle.y + vehicle.length == self.size:
                if not self.field[vehicle.y + vehicle.length][vehicle.x] == 0:
                    blocking_traffic.append(self.field[vehicle.y + vehicle.length][vehicle.x])
            if not vehicle.y == 0:
                if not self.field[vehicle.y - 1][vehicle.x] == 0:
                    blocking_traffic.append(self.field[vehicle.y - 1][vehicle.x])

        # check both right and left
        else:
            if not vehicle.x + vehicle.length == self.size:
                if not self.field[vehicle.y][vehicle.x + vehicle.length] == 0:
                    blocking_traffic.append(self.field[vehicle.y][vehicle.x + vehicle.length])
            if not vehicle.x == 0:
                if not self.field[vehicle.y][vehicle.x - 1] == 0:
                    blocking_traffic.append(self.field[vehicle.y][vehicle.x - 1])

        return blocking_traffic


    def play(self, game):
        """ Show visualization of game being won (hardcoded). Implement moves
        for the visualisation of a game being won. The moves are hardcoded for
        the purpose of being able to show a winning sequence of moves.

        Keyword arguments:
        game -- game id (1 to 7)
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
        """ Helper function for play function. Move one vehicle left, right,
        up or down a number of blocks. Show the resulting field using the function
        show_field.

        Keyword arguments:
        id -- the id of the vehicle to be moved
        move -- number of blocks to be moved (negative: left or up, positive:
                right or down)
        """

        vehicle = self.vehicles[id]
        if vehicle.orientation == 'H' :
            self.vehicles[id].x += move
        elif vehicle.orientation == 'V':
            self.vehicles[id].y += move
        self.fill_field(list(self.vehicles.values()))
        self.show_field(list(self.vehicles.values()), True)


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
