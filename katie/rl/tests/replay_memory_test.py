from katie.rl.replay_memory import ReplayMemory


def test_replay_memory_creation():
    default_capacity = 10000
    rm = ReplayMemory()
    assert (default_capacity == rm.capacity)


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


