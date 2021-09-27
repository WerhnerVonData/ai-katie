import os
import pytest
from katie.rl.replay_memory import ReplayMemory

_file_name = "buffer.pickle"
_file_name_no_extension = "buffer"


def _fill_memory(replay_memory: ReplayMemory, data: str = ""):
    for n in range(0, replay_memory._capacity):
        replay_memory.append_memory(str(n) + data)


def test_save_memory():
    rm = ReplayMemory()
    _fill_memory(rm)
    rm.save_memory_buffer(_file_name)
    assert (os.path.exists(_file_name))
    os.remove(_file_name)


def test_save_memory_wrong_file_format():
    rm = ReplayMemory()
    _fill_memory(rm)
    with pytest.raises(TypeError):
        rm.save_memory_buffer(_file_name_no_extension)


def test_load_memory():
    rm = ReplayMemory()
    _fill_memory(rm)
    rm.save_memory_buffer(_file_name)
    assert (os.path.exists(_file_name))

    rm_load = ReplayMemory()
    rm_load.load_memory_buffer(_file_name)

    assert (rm._buffer == rm_load._buffer)
    os.remove(_file_name)


def test_load_memory_no_existing_file():
    rm = ReplayMemory()
    with pytest.raises(FileNotFoundError):
        rm.load_memory_buffer(_file_name)


def test_load_memory_wrong_format_file():
    rm = ReplayMemory()
    with pytest.raises(TypeError):
        rm.load_memory_buffer(_file_name_no_extension)


def test_load_memory_buffer_is_cleaned():
    rm = ReplayMemory()
    _fill_memory(rm)
    rm.save_memory_buffer(_file_name)
    assert (os.path.exists(_file_name))

    rm_load = ReplayMemory()
    _fill_memory(rm_load, data="TEST")
    rm_load.load_memory_buffer(_file_name)

    assert (rm._buffer == rm_load._buffer)
    os.remove(_file_name)

# TODO:
# - Test that will verify that buffer removes exceeding data from left side
# - Test the buffer was cleaned from previous data after load
# - Test that the current buffer is untouched when the loading fails
# - Optional hashing mechanism - https://www.quickprogrammingtips.com/python/how-to-calculate-sha256-hash-of-a-file-in-python.html