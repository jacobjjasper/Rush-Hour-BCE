from rush import RushHour, PriorityQueue
import time
import secrets
from collections import deque

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

def depth_first(game):
    """
    Last in first out
    """

    stack = []
    moves = 0
    bound = 17
    winnings = []

    vehicles = list(game.vehicles.values())

    stack.append(vehicles)
    stack.append(moves)

    while not len(stack) == 0:

        # get last item in stack
        moves = stack.pop()
        vehicles = stack.pop()

        if moves > bound:
            continue

        if game.won(vehicles):
            bound = moves
            winnings.append(moves)
            print(moves,len(stack))

        # only make child fields if not won
        else:

            # fill game.field with vehicles
            game.fill_field(vehicles)
            # game.show_field2()

            # get childs
            child_fields = game.get_child_fields_whole_step(vehicles)

            # give these child move + 1
            moves += 1

            # check if field is in archive and lower than bound
            for field in child_fields:
                stack.append(field)
                stack.append(moves)

    return winnings

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
        for field in child_fields:
            if game.is_unique(field):
                queue.append(field)
                queue.append(moves)

    return moves, states

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


def best_first(game, heuristic):
    """ Best-First with priority """

    # to proberen:
    # deque for fast appends and pops
    queue = PriorityQueue()
    moves = 0
    states = 0

    vehicles = list(game.vehicles.values())

    # append field and moves to queue
    queue.push([moves, vehicles], 0)

    while not game.won(vehicles):

        # get first (highest priority) item from queue
        moves, vehicles = queue.get_prio()

        # fill game.field with vehicles
        game.fill_field(vehicles)
        # game.show_field2(vehicles, True)

        # get childs
        child_fields = game.get_child_fields_whole_step(vehicles)

        moves += 1
        states += 1
        print(moves)

        # check if field is in archive and add to queue
        for field in child_fields:
            if game.is_unique(field):
                if heuristic == "cars_to_exit":
                    priority = moves + game.cars_to_exit(field)
                elif heuristic == "cars_in_traffic":
                    priority = moves + game.cars_in_traffic(field)

                queue.push([moves, field], priority)



    return moves, states
