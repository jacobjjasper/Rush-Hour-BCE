from rush import RushHour, PriorityQueue
import time
import secrets
from collections import deque

def random(game, bound):
    """ Comments """
    start = time.clock()

    vehicles = list(game.vehicles.values())
    child_fields = game.get_child_fields_whole_step(vehicles)

    moves = 0

    while not game.won(vehicles):

        # get random child field and fill game
        vehicles = secrets.choice(child_fields)
        game.fill_field(vehicles)

        # increment moves
        moves += 1
        if moves == bound:
            return moves, 0

        # get new childs
        child_fields = game.get_child_fields_whole_step(vehicles)

    print(f"Solved with {moves} moves in {round(time.clock() - start, 2)} seconds")
    return moves, (time.clock() - start)

def depth_first(game):
    """
    Last in first out
    """

    stack = []
    moves = 0

    initial_vehicles = list(game.vehicles.values())

    stack.append(initial_vehicles)
    stack.append(moves)

    while not game.won():

        # get last item in stack
        moves = stack.pop()
        vehicles = stack.pop()

        # fill game.field with vehicles
        game.fill_field(vehicles)
        game.show_field()

        # get childs
        child_fields = game.get_child_fields_whole_step(vehicles)

        moves += 1
        print(moves)

        # check if field is in archive and add to stack
        for field in child_fields:
            if game.is_unique(field):
                stack.append(field)
                stack.append(moves)

        if moves == 1000:
            break

    return moves

def breadth_first(game):
    """
    First in first out
    """

    # deque for fast appends and pops
    queue = deque()
    moves = 0

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
        # game.show_field()

        # get childs
        child_fields = game.get_child_fields_every_step(vehicles)

        moves += 1
        # print(moves)

        # check if field is in archive and add to queue
        for field in child_fields:
            if game.is_unique(field):
                queue.append(field)
                queue.append(moves)

    return moves


def piority(game):
    """ Breadth-First with priority """

    # to proberen:
    # deque for fast appends and pops
    queue = PriorityQueue()
    moves = 0

    initial_vehicles = list(game.vehicles.values())

    # append field and moves to queue
    queue.push([moves, initial_vehicles], 0)

    while not queue.isempty():
    # while not game.won():

        # get first (highest priority) item from queue
        moves, vehicles = queue.get_prio()

        # fill game.field with vehicles
        game.fill_field(vehicles)
        # game.show_field()

        if game.won():
            return moves

        # get childs
        child_fields = game.get_child_fields_1_step(vehicles)

        moves += 1

        print(moves)

        # check if field is in archive and add to queue
        for field in child_fields:
            if game.is_unique(field):
                priority = moves + game.check_block(field)
                queue.push([moves, field], priority)
        # if moves == 2:
        #     return True

        # return moves
    return "QUEUE EMPTY"
