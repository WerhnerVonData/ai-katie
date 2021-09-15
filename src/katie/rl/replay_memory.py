import numpy as np
from collections import deque

"""
ReplayMemory class gives an ability to store and give back data in random batches.
Memory has a limited buffer based on the FIFO queue.
"""


class ReplayMemory:
    def __init__(self, capacity=10000):
        self.capacity = capacity
        self.buffer = deque()

    def sample_batch(self, batch_size):
        """
        Creates an iterator that returns random batches from the buffer.
        The batch size has to be smaller than the current number of data elements.
        :param batch_size: batch size
        :return: iterator returning random batches
        """
        if batch_size <= 0:
            return
        ofs = 0
        vals = list(self.buffer)
        np.random.shuffle(vals)
        while (ofs + 1) * batch_size <= len(self.buffer):
            yield vals[ofs * batch_size:(ofs + 1) * batch_size]
            ofs += 1

    def append_memory(self, data):
        """

        :param data:
        :return:
        """
        self.buffer.append(data)
        while len(self.buffer) > self.capacity:
            self.buffer.popleft()

    def is_buffer_full(self, capacity_percantage=100):
        """

        :return:
        """
        return len(self.buffer) >= self.capacity
