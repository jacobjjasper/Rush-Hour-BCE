""" Module containing Depth First algorithm to solve Rush Hour. Contains a
function depth_first, which solves a Rush Hour game using depth first search."""
from rush import RushHour


def depth_first(game):
    """ Depth First algorithm until game is won. Last in first out.

    Keyword arguments:
    game -- RushHour object
    """

    stack = []
    moves = 0
    bound = 1
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
