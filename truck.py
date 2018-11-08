from vehicle import Vehicle

class Truck(Vehicle):

    """
    Truck (child of Vehicle) class for Rush Hour game
    """

    def __init__(self, id, x, y, orientation):
        Vehicle.__init__(self, id, x, y, orientation)
        self.size = 3
