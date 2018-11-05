
class Truck(object):

    def __init__(self, id, x, y, orientation):
        self.id = id
        self.size = 3

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
            self.x_end = self.x + (self.size - 1)
        elif orientation.upper() == 'V':
            self.orientation = orientation
            self.y_end = self.y + (self.size - 1)
        else:
            raise ValueError(f"Invalid orientation: {orientation}")

        if x_end > 5:
            raise ValueError("Invalid position")
        elif y_end > 5:
            raise ValueError("Invalid position")

        self.options = []

    def __str__(self):
        return f"Truck {id}, x: {x}, y:{y}, orientation: {orientation}"

    def __repr__(self):
        return f"Truck {id}, x: {x}, y:{y}, orientation: {orientation}"
