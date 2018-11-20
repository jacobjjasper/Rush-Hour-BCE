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

# CHANGE RESULT_CSV NAME WHEN CHANGING ALGORITHM
RESULT_CSV = 'results/random.csv'

class Main():

    def __init__(self, board):
        for i in range(1):
            rush = RushHour(board)

            # rush.show_field()
            moves, runtime = algorithms.random(rush)

            with open(RESULT_CSV, 'a') as outfile:
                writer = csv.writer(outfile)
                writer.writerow([moves, runtime])

            print(i)

        moves_info = self.hist_plot(RESULT_CSV)
        print(moves_info)

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


if __name__ == "__main__":
    Main("data/game1.txt")
    # rush = RushHour("data/game4.txt")
    # rush.show_field()
