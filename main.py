# voeg de huidige structuur toe aan path
import os, sys
import csv
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
# sys.path.append(os.path.join(directory, "code", "classes"))
# sys.path.append(os.path.join(directory, "code", "algoritmes"))

import numpy as np
import statistics as stat
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import algorithms
from rush import RushHour



class Main():

    def __init__(self, board):
        self.board_no = board
        self.board = f"data/game{board}.txt"
        self.rush = RushHour(f"data/game{board}.txt")
        # self.results_csv = f"results/random_1_step_game{board}.csv"
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
            moves, runtime = algorithms.random(rush, show, bound)
            bound = moves
            print(moves)

            # add values to csv file
            with open(self.results_csv, 'a') as outfile:
                writer = csv.writer(outfile)
                writer.writerow([moves, runtime])

        # plot histogram
        moves_info = self.hist_plot(self.results_csv, 'Random')

        # print results
        [print(f"{key}: {value}") for key, value in moves_info.items()]

    def hist_plot(self, infile, algorithm):

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
            moves_info['max'] = max(moves)
            moves_info['min'] = min(moves)
            moves_info['mean'] = round(np.mean(moves), 2)
            moves_info['median'] = np.median(moves)
            moves_info['stddev'] = round(np.std(moves), 2)

            # histogram
            plt.style.use('ggplot')
            plt.rcParams["axes.edgecolor"] = "0.15"
            plt.rcParams["axes.linewidth"]  = 1.25
            plt.grid(b = True, axis = 'y', zorder = 0)
            # plt.hist(moves, bins = 50, rwidth = 1, zorder = 3,edgecolor='black', linewidth=1.2)

            # log scale
            # plt.hist(moves, bins=np.logspace(1, round(np.log10(moves_info['max'])), 70), rwidth = 0.85, zorder = 3)
            # plt.gca().set_xscale("log")

            plt.plot(moves)

            plt.suptitle('Number of steps to solution, branch & bound', fontsize = 16)
            plt.title(f"{algorithm} solutions of game {self.board_no}")
            plt.xlabel('Runs')
            plt.ylabel('Number of moves')
            plt.show()

            return moves_info

    def call_depth_first(self):

        # makes new game every time
        rush = RushHour(self.board)

        # run algorithm
        winnings = algorithms.depth_first(rush)
        print(f"Moves: {min(winnings)} (best of {len(winnings)} wins)")

    def call_breadth_first(self):
        rush = RushHour(self.board)
        moves, states = algorithms.breadth_first(rush)
        print(f"Moves: {moves}, States: {states}")

    def call_best_first(self, heuristic):
        rush = RushHour(self.board)
        moves, states = algorithms.best_first(rush, heuristic)
        print(f"Moves: {moves}, States: {states}")

    def call_breadth_first_2(self):
        rush = RushHour(self.board)
        moves, states = algorithms.breadth_first_2(rush)
        print(f"Moves: {moves}, States: {states}")

if __name__ == "__main__":
    game = sys.argv[1]
    algorithm = sys.argv[2]

    # initiaze game
    main = Main(game)

    # call algorithm via Main
    if algorithm == "show":
        main.rush.show_field2(list(main.rush.vehicles.values()), False)
    elif algorithm == "play":
        main.rush.show_field2(list(main.rush.vehicles.values()), True)
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
    elif algorithm == "breadth_first_2":
        main.call_breadth_first_2()
