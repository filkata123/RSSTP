from memory import Memory

#test_compare when previous actions are different
def test_compare_different_actions():
    mem = Memory()
    mem.update_memory(0, 0, False)
    mem.update_memory(1, 1, True)
    mem.update_memory(0, 2, False)

    assert mem.compare(1, 2) == 0

#test_compare when previous actions are the same, but internal states are different
def test_compare_different_states():
    mem = Memory()
    mem.update_memory(0, 0, False)
    mem.update_memory(0, 1, True)
    mem.update_memory(0, 2, False)

    assert mem.compare(1, 2) == 1

#test_compare when previous actions and internal states are the same, but sensations are different
def test_compare_different_sensations():
    mem = Memory()
    mem.update_memory(0, 0, False)
    mem.update_memory(0, 1, True)
    mem.update_memory(0, 1, False)

    assert mem.compare(1, 2) == 2

#test_compare when previous actions, internal states, and sensations are the same
def test_compare_same():
    mem = Memory()
    mem.update_memory(0, 0, False)
    mem.update_memory(0, 1, True)
    mem.update_memory(0, 1, True)

    assert mem.compare(1, 2) == 3

# n > m tests
def test_compare_n_greater_than_m_identical():
    mem = Memory()
    mem.update_memory(0, 0, False)
    mem.update_memory(0, 1, True)
    mem.update_memory(0, 1, True)
    assert mem.compare(2, 1) == 3  

def test_compare_n_greater_than_m_different():
    mem = Memory()
    mem.update_memory(0, 0, False)
    mem.update_memory(0, 1, True)
    mem.update_memory(0, 2, False)
    assert mem.compare(2, 1) == 1

# Test invalid inputs
def test_compare_invalid_n_too_large():
    mem = Memory()
    mem.update_memory(0, 0, False)
    mem.update_memory(0, 1, True)
    assert mem.compare(5, 1) == -1

def test_compare_invalid_m_too_large():
    mem = Memory()
    mem.update_memory(0, 0, False)
    mem.update_memory(0, 1, True)
    assert mem.compare(0, 5) == -1

def test_compare_invalid_negative_n():
    mem = Memory()
    mem.update_memory(0, 0, False)
    assert mem.compare(-1, 0) == -1

def test_compare_invalid_negative_m():
    mem = Memory()
    mem.update_memory(0, 0, False)
    assert mem.compare(0, -1) == -1

def test_compare_n_equals_m():
    # n == m is explicitly returned as -1
    mem = Memory()
    mem.update_memory(0, 0, False)
    mem.update_memory(0, 1, True)
    assert mem.compare(1, 1) == -1

def test_compare_empty_memory():
    mem = Memory()
    assert mem.compare(0, 1) == -1

