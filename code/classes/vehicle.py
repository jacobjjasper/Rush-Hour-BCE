""" Vehicle class, representing a car or truck on a Rush Hour board. """


class Vehicle:
    """ Vehicle class for game of Rush Hourself.

    Attributes:
    id -- vehicle id (int)
    length -- 2 or 3 for car or truck
    x -- x coordinate (left)
    y -- y coordinate (upper)
    orientation -- 'H' for horizontal, 'V' for vertical
    """


    def __init__(self, id, x, y, orientation, length):
        self.id = id
        self.length = length
        self.x = x
        self.y = y
        self.orientation = orientation
