"""
File containing random algorithm.
"""

from rush import RushHour
import time
import secrets

def random(game, show, bound):
    """ Comments """
    start = time.clock()

    vehicles = list(game.vehicles.values())
    child_fields = game.get_child_fields_whole_step(vehicles)

    moves = 0

    while not game.won(vehicles):

        # get random child field and fill game
        vehicles = secrets.choice(child_fields)
        game.fill_field(vehicles)

        # show game
        if show:
            game.show_field2(vehicles, True)

        # increment moves
        moves += 1
        if moves == bound:
            return moves, 0

        # get new childs
        child_fields = game.get_child_fields_whole_step(vehicles)

    # print(f"Solved with {moves} moves in {round(time.clock() - start, 2)} seconds")
    print(moves)
    return moves, (time.clock() - start)
