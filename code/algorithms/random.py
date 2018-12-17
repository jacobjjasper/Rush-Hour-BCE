""" File containing random algorithm to solve Rush Hour. Contains a function
random which solves a Rush Hour game using random search.
"""
from rush import RushHour
import secrets


def random(game, show, bound):
    """ Move random vehicle until the game is won. Return number of moves
    needed to solve the game.

    Keyword arguments:
    game -- RushHour object
    show -- boolean for visualization
    bound -- bound for branch & bound (default 0)
    """
    vehicles = list(game.vehicles.values())
    child_fields = game.get_child_fields_whole_step(vehicles)
    moves = 0

    while not game.won(vehicles):
        vehicles = secrets.choice(child_fields)
        game.fill_field(vehicles)
        if show:
            game.show_field(vehicles, True)
        moves += 1
        if moves == bound:
            return moves
        child_fields = game.get_child_fields_whole_step(vehicles)

    print(moves)
    return moves
