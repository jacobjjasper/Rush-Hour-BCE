from rush import RushHour, PriorityQueue


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
