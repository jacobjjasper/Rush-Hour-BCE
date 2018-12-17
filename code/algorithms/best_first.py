""" Module containing Best First algorithm to solve Rush Hour. Contains a
function best_first, which solves a Rush Hour game using breadth first search
combined with a heuristic of choice.
"""
from rush import RushHour
from priority_queue import PriorityQueue


def best_first(game, heuristic):
    """ Create priority queue for all child fields of Rush Hour board, get first
    in first out. Check if field is unique, then call heuristic and append to queue.
    Heuristic 'cars to exit' counts the number of cars blocking the red car to the exit.
    Hueristic 'cars in traffic' counts the number of cars to move, before the
    red car can be moved.
    Return number of moves needed to solve the game and number of states checked.

    Keyword arguments:
    game -- RushHour object
    heuristic -- string containing heuristic to apply
    """
    queue = PriorityQueue()
    moves = 0
    states = 0
    vehicles = list(game.vehicles.values())
    queue.push([moves, vehicles], 0)

    while not game.won(vehicles):
        moves, vehicles = queue.get_prio()
        game.fill_field(vehicles)
        child_fields = game.get_child_fields_whole_step(vehicles)
        moves += 1
        states += 1
        print(moves)
        for field in child_fields:
            if game.is_unique(field):
                if heuristic == "cars_to_exit":
                    priority = moves + game.cars_to_exit(field)
                elif heuristic == "cars_in_traffic":
                    priority = moves + game.cars_in_traffic(field)
                queue.push([moves, field], priority)

    return moves, states
