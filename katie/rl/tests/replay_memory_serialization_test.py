import os
import pytest
from katie.rl.replay_memory import ReplayMemory

_file_name = "buffer.pickle"
_file_name_no_extension = "buffer"

def test_save_memory():
    rm = ReplayMemory()
    for n in range(0, rm._capacity):
        rm.append_memory(n)
    rm.save_memory_buffer(_file_name)
    assert (os.path.exists(_file_name))
    os.remove(_file_name)


def test_save_memory_wrong_file_format():
    rm = ReplayMemory()
    for n in range(0, rm._capacity):
        rm.append_memory(n)
    with pytest.raises(TypeError):
        rm.save_memory_buffer(_file_name_no_extension)


def test_load_memory():
    rm = ReplayMemory()
    for n in range(0, rm._capacity):
        rm.append_memory(n)
    rm.save_memory_buffer(_file_name)
    assert (os.path.exists(_file_name))

    rm_load = ReplayMemory()

    os.remove(_file_name)


def test_load_memory_no_existing_file():
    rm = ReplayMemory()
    with pytest.raises(FileNotFoundError):
        rm.load_memory_buffer(_file_name)


def test_load_memory_wrong_format_file():
    rm = ReplayMemory()
    with pytest.raises(TypeError):
        rm.load_memory_buffer(_file_name_no_extension)
