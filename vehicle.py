

class Vehicle:
    """
    Vehicle class for game of Rush Hour
    """

    def __init__(self, id, x, y, orientation):
        self.id = id
        self.size = 2

        if x in range(1,7):
            self.x = x
        else:
            raise ValueError(f"Invalid x: {x}")

        if y in range(1,7):
            self.y = y
        else:
            raise ValueError(f"Invalid y: {y}")

        if orientation.upper() == 'H':
            self.orientation = orientation
            self.x_end = self.x + (self.size - 1)
            if self.x_end > 6:
                raise ValueError("Invalid position")
        elif orientation.upper() == 'V':
            self.orientation = orientation
            self.y_end = self.y + (self.size - 1)
            if self.y_end > 6:
                raise ValueError("Invalid position")
        else:
            raise ValueError(f"Invalid orientation: {orientation}")




        self.options = []

        def __str__(self):
            return f"Car {id}, x: {x}, y:{y}, orientation: {orientation}"

        def __repr__(self):
            return f"Car {id}, x: {x}, y:{y}, orientation: {orientation}"
