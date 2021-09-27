import pickle
import numpy as np
from collections import deque

"""
ReplayMemory class gives an ability to store and give back data in random batches.
Memory has a limited buffer based on the FIFO queue.
"""


class ReplayMemory:
    def __init__(self, capacity=10000):
        self._capacity = capacity
        self._buffer = deque()

    def sample_batch(self, batch_size: int):
        """
        Creates an iterator that returns random batches from the buffer.
        The batch size has to be smaller than the current number of data elements.
        :param batch_size: batch size
        :return: iterator returning random batches
        """
        if batch_size <= 0:
            return
        ofs = 0
        vals = list(self._buffer)
        np.random.shuffle(vals)
        while (ofs + 1) * batch_size <= len(self._buffer):
            yield vals[ofs * batch_size:(ofs + 1) * batch_size]
            ofs += 1

    def append_memory(self, data):
        """
        Adds new data element to the replay memory buffer.
        When the capacity is reached, the oldest element in the
        buffer is removed.
        :param data: data element to add
        :return:
        """
        self._buffer.append(data)
        while len(self._buffer) > self._capacity:
            self._buffer.popleft()

    def get_current_buffer_size(self):
        """
        Return the current number of buffer elements
        :return: number of buffer elements
        """
        return len(self._buffer)

    def get_capacity(self):
        """
        Returns the maximum capacity of the memory
        :return: the memory set capacity
        """
        return self._capacity

    def is_buffer_full(self):
        """
        Tells if buffer reached the maximum value of the capacity.
        :return: True when the number of elements is equal of higher than the capacity.
        False otherwise.
        """
        return len(self._buffer) >= self._capacity

    def is_buffer_fulled_by_percentage_value(self, capacity_percantage=100):
        """
        Tells if buffer reached the given percentage of the capacity.
        The percentage value should be between 0 and 100.
        Negative values treat as 0% and value higher than 100 as 100%.
        :param capacity_percantage: the percentage of value of the buffer that we want to compare the capacity.
        :return: True when the elements in the buffer are equal or higher than
        the percentage value of the memory capacity, False otherwise.
        """
        percentage = capacity_percantage
        if percentage > 100:
            percentage = 100
        elif percentage < 0:
            percentage = 0
        return len(self._buffer) >= self._capacity * (percentage / 100.0)

    def save_memory_buffer(self, file_name: str):
        """
        Saves the buffer to pickle file.
        :param file_name: the name of the file. The file name must contain the '.pickle' extension.
        """
        if file_name.endswith(".pickle"):
            with open(file_name, 'wb') as f:
                pickle.dump(self._buffer, f)
                return
        raise TypeError("The file name {} does not ends with '.pickle' extension.".format(file_name))

    def load_memory_buffer(self, file_name: str):
        """
        Loads the buffer from the pickle file. Caution - it will clear the current content of the memory buffer.
        The loaded data will not exceed the memory capacity.
        :param file_name: the name of the file. The file name must contain the '.pickle' extension.
        If the file does not exist, or it has the wrong extension, the right exception is raised.
        If the pickle content is not iterable, the TypeError is raised.
        """
        if file_name.endswith(".pickle"):
            with open(file_name, 'rb') as f:
                self._buffer.clear()
                for data in pickle.load(f):
                    self._buffer.append(data)
                    if self.is_buffer_full():
                        return
                return
        raise TypeError("The file name {} does not ends with '.pickle' extension.".format(file_name))
