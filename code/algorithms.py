from rush import RushHour
import time
import secrets

def random(game):
    """ Comments """
    start = time.clock()

    game_vehicles = list(game.vehicles.values())
    child_fields = game.get_child_fields(game_vehicles)

    moves = 0

    while not game.won():

        # get random child field and fill game
        vehicles = secrets.choice(child_fields)
        game.fill_field(vehicles)

        # increment moves
        moves += 1


        # get new childs
        child_fields = game.get_child_fields(vehicles)

        # game.show_field()

    print(f"Solved with {moves} moves in {round(time.clock() - start, 2)} seconds")
    return f"Solved with {moves} moves in {round(time.clock() - start, 2)} seconds"
