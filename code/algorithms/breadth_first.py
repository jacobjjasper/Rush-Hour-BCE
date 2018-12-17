""" Module containing a Breadth First algorithm to solve Rush Hour. Contains a
function breadth_first, which solves a Rush Hour game using depth first search.
"""
from rush import RushHour
from collections import deque


def breadth_first(game):
    """ Create queue for all child fields of Rush Hour board, get first in
    first out. Check if field is unique, if so, append to queue.
    Return number of moves needed to solve the game and number of states checked.

    Keyword arguments:
    game -- RushHour object
    """
    queue = deque()
    moves = 0
    states = 0
    vehicles = list(game.vehicles.values())
    queue.append(vehicles)
    queue.append(moves)

    while not game.won(vehicles):
        vehicles = queue.popleft()
        moves = queue.popleft()
        game.fill_field(vehicles)
        child_fields = game.get_child_fields_whole_step(vehicles)
        moves += 1
        states += 1
        print(moves, states)
        for field in child_fields:
            if game.is_unique(field):
                queue.append(field)
                queue.append(moves)

    return moves, states
