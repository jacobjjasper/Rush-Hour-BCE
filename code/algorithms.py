from rush import RushHour
import secrets

def random(game):
    """ Comments """
    game_vehicles = list(game.vehicles.values())
    child_fields = game.get_child_fields(game_vehicles)

    moves = 0

    while not game.won():


        vehicles = secrets.choice(child_fields)

        # increment moves
        moves += 1
        print(moves)

        # get new childs
        child_fields = game.get_child_fields(vehicles)

        game.show_field()

        if moves == 15:
            break
