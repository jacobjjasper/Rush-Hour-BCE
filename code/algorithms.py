from rush import RushHour
import time
import secrets

def random(game):
    """ Comments """
    start = time.clock()

    game_vehicles = list(game.vehicles.values())
    child_fields = game.get_child_fields_2(game_vehicles)

    moves = 0

    while not game.won():

        # get random child field and fill game
        vehicles = secrets.choice(child_fields)
        game.fill_field(vehicles)

        # increment moves
        moves += 1

        # get new childs
        child_fields = game.get_child_fields(vehicles)

    # print(f"Solved with {moves} moves in {round(time.clock() - start, 2)} seconds")
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
        child_fields = game.get_child_fields_2(vehicles)

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
