from rush import RushHour, PriorityQueue
import time
import secrets
from collections import deque

def breadth_first_2(game):
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

    previous = []
    current = []

    previous.append(game.create_hash_hex(vehicles))

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
        for field in child_fields:
            hash = game.create_hash_hex(field)
            if not hash in previous:
                queue.append(field)
                queue.append(moves)
                current.append(hash)

        # exchange previous for child fields
        previous = current

    return moves, states
