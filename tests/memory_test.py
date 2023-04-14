from memory import Memory
import pandas as pd
import io
import sys

def test_make_list_from_data():
    memory_step = Memory(0, 0, False)
    expected = [0, 0, False]

    assert memory_step.make_list_from_data() == expected

test_make_list_from_data()

def test_print_memory():
    #initializing memory list with three elements. memory_step is needed to call the method.
    memory_step = Memory(1, 0, False)
    Memory.memory.append(memory_step.make_list_from_data())
    memory_step = Memory(0, 1, False)
    Memory.memory.append(memory_step.make_list_from_data())
    memory_step = Memory(0, 2, True)
    Memory.memory.append(memory_step.make_list_from_data())

    # from https://stackoverflow.com/questions/33767627/python-write-unittest-for-console-print
    capturedOutput = io.StringIO()                  # Create StringIO object
    sys.stdout = capturedOutput
    memory_step.print_memory()
    sys.stdout = sys.__stdout__
    expected = "(0, [1, 0, False])\n(1, [0, 1, False])\n(2, [0, 2, True])\n"

    assert capturedOutput.getvalue() == expected

test_print_memory()

def test_make_dataframe():
    test_data = []
    test_data.append([0, 0, False])
    test_data.append([0, 0, False])
    test_data.append([1, 2, True])
    expected = pd.DataFrame(test_data, columns=['Previous action', 'Internal state', 'Sensation'])

    assert Memory.make_dataframe(test_data).equals(expected)

test_make_dataframe()

#test_compare when previous actions are different
def test_compare1():
    test_memory = [[0, 0, False], [1, 1, True], [0, 2, False]]
    dataframe = pd.DataFrame(test_memory, columns=['Previous action', 'Internal state', 'Sensation'])

    assert Memory.compare(1, 2, dataframe) == 0

test_compare1()

#test_compare when previous actions are the same, but internal states are different
def test_compare2():
    test_memory = [[0, 0, False], [0, 1, True], [0, 2, False]]
    dataframe = pd.DataFrame(test_memory, columns=['Previous action', 'Internal state', 'Sensation'])

    assert Memory.compare(1, 2, dataframe) == 1

test_compare2()

#test_compare when previous actions and internal states are the same, but sensations are different
def test_compare3():
    test_memory = [[0, 0, False], [0, 1, True], [0, 1, False]]
    dataframe = pd.DataFrame(test_memory, columns=['Previous action', 'Internal state', 'Sensation'])

    assert Memory.compare(1, 2, dataframe) == 2

test_compare3()

#test_compare when previous actions, internal states, and sensations are the same
def test_compare4():
    test_memory = [[0, 0, False], [0, 1, True], [0, 1, True]]
    dataframe = pd.DataFrame(test_memory, columns=['Previous action', 'Internal state', 'Sensation'])

    assert Memory.compare(1, 2, dataframe) == 3

test_compare4()

