

class Vehicle:
    """
    Vehicle class for game of Rush Hour
    """

    def __init__(self, id, x, y, orientation, length):
        self.id = id
        self.length = length

        if x in range(1,7):
            self.x = x
        else:
            raise ValueError(f"Invalid x: {x} for vehicle id: {id}")

        if y in range(1,7):
            self.y = y
        else:
            raise ValueError(f"Invalid y: {y} for vehicle id: {id}")

        if orientation.upper() == 'H':
            self.orientation = orientation
            self.x_end = self.x + (self.length - 1)
            if self.x_end > 6:
                raise ValueError(f"Invalid position for vehicle id: {id}")
        elif orientation.upper() == 'V':
            self.orientation = orientation
            self.y_end = self.y + (self.length - 1)
            if self.y_end > 6:
                raise ValueError(f"Invalid position for vehicle id: {id}")
        else:
            raise ValueError(f"Invalid orientation: {orientation} for vehicle id: {id}")


        def __str__(self):
            return f"Vehicle {self.id}, x: {self.x}, y:{self.y}, orientation: {self.orientation}"

        def __repr__(self):
            return f"Vehicle {self.id}, x: {self.x}, y:{self.y}, orientation: {self.orientation}"
