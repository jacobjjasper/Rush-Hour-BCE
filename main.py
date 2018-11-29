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
from rush2 import RushHour



class Main():

    def __init__(self, board):
        self.board_no = board
        self.board = f"data2/game{board}.txt"
        self.rush = RushHour(f"data2/game{board}.txt")
        # self.results_csv = f"results/random_1_step_game{board}.csv"
        self.results_csv = f"results/random_whole_step_game{board}.csv"


    def call_random(self, number):
        """
        Runs random algorithm for {number} of times
        Plots all (including previous) results
        """

        # makes new game every time
        for i in range(number):
            rush = RushHour(self.board)

            # run algorithm and get return values
            moves, runtime = algorithms.random(rush)

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
            plt.hist(moves, bins=np.logspace(1, round(np.log10(moves_info['max'])), 70), rwidth = 0.85, zorder = 3)

            # bins = 10**(np.arange(0,7))
            # plt.hist(moves, bins = bins, rwidth = 0.8)
            plt.gca().set_xscale("log")
            plt.suptitle('Frequency distribution Rush Hour solver', fontsize = 16)
            plt.title(f"{algorithm} solutions of game {self.board_no}")
            plt.xlabel('Number of moves')
            plt.ylabel('Frequency')
            plt.show()

            return moves_info

    def call_depth_first(self):

        # makes new game every time
        rush = RushHour(self.board)

        # run algorithm
        print(f"Moves: {algorithms.depth_first(rush)}")

    def call_breadth_first(self):
        rush = RushHour(self.board)
        print(f"Moves: {algorithms.breadth_first(rush)}")

if __name__ == "__main__":
    main = Main(1)
    # main.rush.show_field()
    # for field in main.rush.get_child_fields_every_step(list(main.rush.vehicles.values())):
    #     main.rush.fill_field(field)
    #     main.rush.show_field()

    main.call_random(0)
    # main.call_depth_first()
    # main.call_breadth_first()
