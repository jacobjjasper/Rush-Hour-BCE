"""
File containing Breadth First algorithm.
"""

from rush import RushHour
from collections import deque

def breadth_first(game):
    """
    First in first out
    """

    # deque for fast appends and pops
    queue = deque()
    moves = 0
    states = 0

    vehicles = list(game.vehicles.values())

    # append field and moves to queue
    queue.append(vehicles)
    queue.append(moves)

    while not game.won(vehicles):

        # get first item from queue
        vehicles = queue.popleft()

        moves = queue.popleft()

        # fill game.field with vehicles
        game.fill_field(vehicles)
        # game.show_field2(vehicles, True)

        # get childs
        child_fields = game.get_child_fields_whole_step(vehicles)

        moves += 1
        states += 1
        print(moves, states)

        # check if field is in archive and add to queue
        # ADDED: moves in is_unique(). Delete also in function when we don't use
        # the archive trick
        for field in child_fields:
            if game.is_unique(field):
                queue.append(field)
                queue.append(moves)
        # game.update_archive(moves)

    return moves, states
