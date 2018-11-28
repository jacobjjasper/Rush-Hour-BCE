from rush import RushHour
import time
import secrets
from collections import deque
import heapq


class PriorityQueue:

    def __init__(self):
        self.queue = []
        self.index = 0

    def push(self, board, priority):
        heapq.heappush(self.queue, (-priority, self.index, board))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]

    def isempty(self):
        return len(self.queue) == 0

class BlockCheck:
    """Checks number of cars blocking the red car from exiting the board"""

    def check(self, board):
        red_car_x =
