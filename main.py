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
        self.board = f"data/game{board}.txt"
        # self.rush = RushHour(f"data/game{board}.txt")
        # self.results_csv = f"results/random2_game{board}.csv"


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
        moves_info = self.hist_plot(self.results_csv)

        # print results
        [print(f"{key}: {value}") for key, value in moves_info.items()]

    def hist_plot(self, infile):

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
            plt.hist(moves, bins = 30, rwidth = 0.8)
            plt.title('Frequency distribution random Rush Hour solver', fontsize = 16)
            plt.xticks(np.arange(0, moves_info['max'] + 1000, 20000))
            plt.xlabel('Number of moves (one car, one block)')
            plt.ylabel('Frequency')
            plt.show()

            return moves_info

    def call_depth_first(self, number):

        # makes new game every time
        for i in range(number):
            rush = RushHour(self.board)

            # run algorithm
            algorithms.depth_first(rush)


if __name__ == "__main__":
    main = Main(3)
    # main.rush.show_field()
    # child_fields = main.rush.get_child_fields_2(list(main.rush.vehicles.values()))
    # for i in range(len(child_fields)):
    #     main.rush.fill_field(child_fields[i])
    #     main.rush.show_field()

    # main.call_random(0)
    main.call_depth_first(1)
