from src.katie.rl.replay_memory import ReplayMemory


def test_replay_memory_creation():
    default_capacity = 10000
    rm = ReplayMemory()
    assert (default_capacity == rm.capacity)


def test_replay_memory_creation_with_custom_capacity():
    for capacity in range(10, 2000, 100):
        rm = ReplayMemory(capacity=capacity)
        assert (capacity == rm.capacity)


def test_replay_memory_batch_sampling():
    capacity = 15000
    batch_size = 200
    rm = ReplayMemory(capacity=capacity)
    for n in range(0, capacity):
        rm.append_memory(n)
    expected_number_of_iterations = capacity/batch_size
    iteration = 0
    for batch in rm.sample_batch(batch_size):
        iteration += 1
    assert (expected_number_of_iterations == iteration)


def test_sample_batch_negative_batch_size():
    batch_size = -50
    rm = ReplayMemory()
    for n in range(0, rm.capacity):
        rm.append_memory(n)
    expected_number_of_iterations = 0
    iteration = 0
    for batch in rm.sample_batch(batch_size):
        iteration += 1
    assert (expected_number_of_iterations == iteration)


def test_sample_batch_zeo_batch_size():
    batch_size = 0
    rm = ReplayMemory()
    for n in range(0, rm.capacity):
        rm.append_memory(n)
    expected_number_of_iterations = 0
    iteration = 0
    for batch in rm.sample_batch(batch_size):
        iteration += 1
    assert (expected_number_of_iterations == iteration)

