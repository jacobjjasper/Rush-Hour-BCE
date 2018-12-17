""" Module containing a Depth First algorithm to solve Rush Hour. Contains a
function depth_first, which solves a Rush Hour game using depth first search.
"""
from rush import RushHour


def depth_first(game):
    """ Depth First search until game is won. Last in first out. Check if newly
    generated field is unique and, if so, append to stack. Once the game is won,
    return the number of moves needed to get to that solution.

    Keyword arguments:
    game -- RushHour object
    """
    stack = []
    moves = 0
    vehicles = list(game.vehicles.values())
    stack.append(vehicles)
    stack.append(moves)

    while not game.won(vehicles):
        moves = stack.pop()
        vehicles = stack.pop()
        game.fill_field(vehicles)
        child_fields = game.get_child_fields_whole_step(vehicles)
        moves += 1
        for field in child_fields:
            if game.is_unique(field):
                stack.append(field)
                stack.append(moves)

    return moves
