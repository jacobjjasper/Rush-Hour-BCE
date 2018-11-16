# voeg de huidige structuur toe aan path
import os, sys
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
# sys.path.append(os.path.join(directory, "code", "classes"))
# sys.path.append(os.path.join(directory, "code", "algoritmes"))

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import algorithms
from rush import RushHour

class Main():
    algorithms.random()




if __name__ == "__main__":
    Main()
