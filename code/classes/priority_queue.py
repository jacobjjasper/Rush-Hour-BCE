""" Module containing PriorityQueue class used by the Best First algorithm. """
import heapq


class PriorityQueue:
    """ Class for a priority queue.

    Attributes:
    queue -- list of fields to be checked
    index -- index in the queue

    Methods:
    push -- add board and its priority to the queue
    get_prio -- get the item with the highest priority from the queue.
    """

    def __init__(self):
        self.queue = []
        self.index = 0


    def push(self, board, priority):
        """ Insert the board into the queue, using its priority to establish a
        priority queue.

        Keyword arguments:
        board -- list containing the generation layer of the field and its vehicles,
                 with vehicles being a list of vehicle objects.
        priority -- score rendered by the used heuristic
        """
        heapq.heappush(self.queue, (priority, self.index, board))
        self.index += 1


    def get_prio(self):
        """ Pop the item with the highest priority from the queue. Return both
        the generation layer of the field as well as a list of the vehicles in
        the field.
        """

        return heapq.heappop(self.queue)[-1]
