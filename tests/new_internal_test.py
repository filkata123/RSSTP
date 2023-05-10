import numpy as np
import pytest
from internal import Internal

def test_is_deterministic_1():
    # transition matrix is not deterministic
    obj = Internal(np.array([[[0,1],[2,5]],
                             [[2,4],[1,2,3]]], dtype = object))
    
    assert obj.is_deterministic() == False

test_is_deterministic_1()

def test_is_deterministic_2():
    # transition matrix is deterministic
    obj = Internal(np.array([[[0,1],[2,5]],
                             [[2,4],[1,3]]], dtype = object))
    
    assert obj.is_deterministic() == True

test_is_deterministic_2()

def test_is_deterministic_3():
    # transition matrix is empty (and deterministic)
    obj = Internal(np.array([[[],[]],
                             [[],[]]], dtype = object))
    
    assert obj.is_deterministic() == True

test_is_deterministic_3()

def test_draw_graph_from_tm():
    # Draws a graph of transition matrix. Does not return anything. Correctedness of the graph has to be checked manually.
    obj = Internal(np.array([[[0,1],[2,5]],
                             [[2,4],[1,3]]], dtype = object))
    obj.draw_graph_from_tm(obj.get_transition_matrix())

    pass

test_draw_graph_from_tm()
