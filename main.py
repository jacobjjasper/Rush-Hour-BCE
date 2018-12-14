""" Module containing the Main class for starting various Rush Hour solvers. """
import os, sys, csv
import numpy as np
import statistics as stat
import matplotlib.pyplot as plt

directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

import depth_first, breadth_first, breadth_first_small_archive, best_first, random
from rush import RushHour


class Main():
    """ Main class for starting various Rush Hour solvers.

    Attributes:
    board_no -- game number, needed in show_plot function
    board -- directory in data folder of the game to be solved
    rush -- RushHour object of the game to be solved
    results_csv -- directory to a csv-file in the results folder where the
                   results of the random solver will be registered.

    Methods:
    call_random -- call random solver using a bound (optional). Results will be
                   written to a csv-file in the results folder.
    show_plot -- helper function for call_random. Show the plot belonging to the
                 random game called.
    call_depth_first -- call depth first solver for Rush Hour game.
    call_breadth_first -- call breadth first solver for Rush Hour game.
    call best_first -- call best first solver for Rush Hour game.
    call_breadth_first_small_archive -- call breadth first solver for Rush Hour
                                        game with small archive
    """

    def __init__(self, board):
        self.board_no = board
        self.board = f"data/game{board}.txt"
        self.rush = RushHour(f"data/game{board}.txt")
        self.results_csv = f"results/random_bb_whole_step_results/csv_data/random_bb_whole_step_game{board}.csv"


    def call_random(self, show, runs, bound):
        """
        Runs random algorithm for {number} of times
        Plots all (including previous) results
        """

        # makes new game every time
        for i in range(runs):
            rush = RushHour(self.board)

            # run algorithm and get return values
            moves, runtime = random.random(rush, show, bound)
            bound = moves
            print(moves)

            # add values to csv file
            with open(self.results_csv, 'a') as outfile:
                writer = csv.writer(outfile)
                writer.writerow([moves, runtime])

        # plot histogram
        moves_info = self.show_plot(self.results_csv, 'Random')

        # print results
        [print(f"{key}: {value}") for key, value in moves_info.items()]

    def show_plot(self, infile, algorithm):

        algorithm = algorithm

        # load infile
        with open(infile) as data:
            reader = csv.DictReader(data, fieldnames = ['moves', 'runtime'])

            # read infile and make list of no. of moves
            moves = []
            for row in reader:
                moves.append(int(row['moves']))

            moves.sort(reverse = True)

            # information
            moves_info = {}
            moves_info['total runs'] = len(moves)
            moves_info['min'] = min(moves)

            # histogram
            plt.style.use('ggplot')
            plt.rcParams["axes.edgecolor"] = "0.15"
            plt.rcParams["axes.linewidth"]  = 1.25
            plt.grid(b = True, axis = 'y', zorder = 0)

            plt.plot(moves)

            plt.suptitle('Number of steps to solution, branch & bound', fontsize = 16)
            plt.title(f"{algorithm} solutions of game {self.board_no}")
            plt.xlabel('Runs')
            plt.ylabel('Number of moves')
            plt.show()

            return moves_info

    def call_depth_first(self):
        """ Run Depth First algorithm """

        rush = RushHour(self.board)
        winnings = depth_first.depth_first(rush)
        print(f"Moves: {min(winnings)} (best of {len(winnings)} wins)")

    def call_breadth_first(self):
        rush = RushHour(self.board)
        moves, states = breadth_first.breadth_first(rush)
        print(f"Moves: {moves}, States: {states}")

    def call_best_first(self, heuristic):
        rush = RushHour(self.board)
        moves, states = best_first.best_first(rush, heuristic)
        print(f"Moves: {moves}, States: {states}")

    def call_breadth_first_small_archive(self):
        rush = RushHour(self.board)
        moves, states = algorithms.breadth_first_small_archive(rush)
        print(f"Moves: {moves}, States: {states}")

if __name__ == "__main__":
    game = sys.argv[1]
    algorithm = sys.argv[2]

    # initiaze game
    main = Main(game)

    # call algorithm via Main
    if algorithm == "show":
        main.rush.show_field(list(main.rush.vehicles.values()), False)
    elif algorithm == "play":
        main.rush.show_field(list(main.rush.vehicles.values()), False)
        main.rush.play(game)
    elif algorithm == "random":
        show = sys.argv[3]
        runs = int(sys.argv[4])
        if len(sys.argv[1:]) == 5:
            bound = int(sys.argv[5])
        else:
            bound = 0
        main.call_random(show, runs, bound)
    elif algorithm == "depth_first":
        main.call_depth_first()
    elif algorithm == "breadth_first":
        main.call_breadth_first()
    elif algorithm == "best_first":
        heuristic = sys.argv[3]
        main.call_best_first(heuristic)
    elif algorithm == "breadth_first_small_archive":
        main.call_breadth_first_small_archive()
