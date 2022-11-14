import os
import sys
import numpy as np
import pytest
cwd = os.getcwd()
sys.path.append(cwd+'/src/')
import internal

obj = internal.Internal(np.array([[(0,1,2,3,4)]], dtype = object),0)
# -------------------------------------------------------------Tests-------------------------------------------------------------------------------------------
def test_split():
    n = 0
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1),(2,3),(4,3),(0,1)],
                         [(1,2),(),(3,),(1,2)],
                         [(2,4),(1,2,3),(1,),(2,4)],
                         [(0,1),(2,3),(4,3),(0,1)]], dtype = object)
    assert (np.array_equal(obj.split(n) , expected))

    n = 1
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1),(2,3),(4,3),(2,3)],
                         [(1,2),(),(3,),()],
                         [(2,4),(1,2,3),(1,),(1,2,3)],
                         [(1,2),(),(3,),()]], dtype = object)
    assert (np.array_equal(obj.split(n) , expected))
    
    n = 2
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1),(2,3),(4,3),(4,3)],
                         [(1,2),(),(3,),(3,)],
                         [(2,4),(1,2,3),(1,),(1,)],
                         [(2,4),(1,2,3),(1,),(1,)]], dtype = object)
    assert (np.array_equal(obj.split(n) , expected))

def test_merge():
    n = 0
    m = 1
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1,2,3),(3,4)],
                         [(1,2,3,4),(1,)]], dtype = object)
    assert (np.array_equal(obj.merge(n,m) , expected ))
    
    n = 0
    m = 2
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object) 

    expected = np.array([[(0,1,2,3,4),(1,2,3)],
                         [(1,2,3),()]], dtype = object)
    assert (np.array_equal(obj.merge(n,m) ,expected ))

    n = 1
    m = 2
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1),(2,3,4)],
                         [(1,2,4),(1,2,3)]], dtype = object)
    assert (np.array_equal(obj.merge(n,m) , expected ))

def test_add():
    n = 0
    m = 1
    k = 0
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1),(0,2,3),(4,3)],
                         [(1,2),(),(3,)],
                         [(2,4),(1,2,3),(1,)]], dtype = object)
    assert (np.array_equal(obj.add(n,m,k) , expected))

    n = 1
    m = 1
    k = 3
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1),(2,3),(4,3)],
                         [(1,2),(3,),(3,)],
                         [(2,4),(1,2,3),(1,)]], dtype = object)
    assert (np.array_equal(obj.add(n,m,k) , expected ))

    n = 2
    m = 2
    k = 0
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1),(2,3),(4,3)],
                         [(1,2),(),(3,)],
                         [(2,4),(1,2,3),(0,1)]], dtype = object)
    assert (np.array_equal(obj.add(n,m,k) , expected))

def test_delete():
    n = 0
    m = 0
    k = 0
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(1,),(2,3),(4,3)],
                         [(1,2),(),(3,)],
                         [(2,4),(1,2,3),(1,)]], dtype = object)
    assert (np.array_equal(obj.delete(n,m,k) , expected))

    n = 1
    m = 2
    k = 3
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1),(2,3),(4,3)],
                         [(1,2),(),()],
                         [(2,4),(1,2,3),(1,)]], dtype = object)
    assert (np.array_equal(obj.delete(n,m,k) , expected))

    n = 2
    m = 1
    k = 2
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1),(2,3),(4,3)],
                         [(1,2),(),(3,)],
                         [(2,4),(1,3),(1,)]], dtype = object)
    assert (np.array_equal(obj.delete(n,m,k) , expected))

    n = 2
    m = 1
    k = 0
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = np.array([[(0,1),(2,3),(4,3)],
                         [(1,2),(),(3,)],
                         [(2,4),(1,2,3),(1,)]], dtype = object)
    assert (np.array_equal(obj.delete(n,m,k) , expected))

def test_transition():
    k = 0
    obj.current_state = 0
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = (0,)
    assert (obj.transition(k) in expected)

# TODO test examples (remaining: transition)
    k = 3
    obj.current_state = 0
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = (1,2)
    assert (obj.transition(k) in expected)

    k = 2
    obj.current_state = 2
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = (0,1)
    assert (obj.transition(k) in expected)

    k = 0
    obj.current_state = 1
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],
                                      [(1,2),(),(3,)],
                                      [(2,4),(1,2,3),(1,)]], dtype = object)

    expected = (1,)
    assert (obj.transition(k) in expected)
retcode = pytest.main()
