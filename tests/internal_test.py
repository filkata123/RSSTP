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
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 0
    assert (np.array_equal(obj.split(n) , np.array([[(0,1),(2,3),(4,3),(0,1)],[(1,2),(),(3,),(1,2)],[(2,4),(1,2,3),(1,),(2,4)],[(0,1),(2,3),(4,3),(0,1)]], dtype = object)))
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 1
    assert (np.array_equal(obj.split(n) , np.array([[(0,1),(2,3),(4,3),(2,3)],[(1,2),(),(3,),()],[(2,4),(1,2,3),(1,),(1,2,3)],[(1,2),(),(3,),()]], dtype = object)))
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 2
    assert (np.array_equal(obj.split(n) , np.array([[(0,1),(2,3),(4,3),(4,3)],[(1,2),(),(3,),(3,)],[(2,4),(1,2,3),(1,),(1,)],[(2,4),(1,2,3),(1,),(1,)]], dtype = object)))

def test_merge():
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 0
    m = 1
    assert (np.array_equal(obj.merge(n,m) , np.array([[(0,1,2,3),(3,4)],[(1,2,3,4),(1,)]], dtype = object)))
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 0
    m = 2
    assert (np.array_equal(obj.merge(n,m) , np.array([[(0,1,2,3,4),(1,2,3)],[(1,2,3),()]], dtype = object)))
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 1
    m = 2
    assert (np.array_equal(obj.merge(n,m) , np.array([[(0,1),(2,3,4)],[(1,2,4),(1,2,3)]], dtype = object)))


def test_add():
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 0
    m = 1
    k = 0
    assert (np.array_equal(obj.add(n,m,k) , np.array([[(0,1),(0,2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)))
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 1
    m = 1
    k = 3
    assert (np.array_equal(obj.add(n,m,k) , np.array([[(0,1),(2,3),(4,3)],[(1,2),(3,),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)))
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 2
    m = 2
    k = 0
    assert (np.array_equal(obj.add(n,m,k) , np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(0,1)]], dtype = object)))
def test_delete():
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 0
    m = 0
    k = 0
    assert (np.array_equal(obj.delete(n,m,k) , np.array([[(1,),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)))
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 1
    m = 2
    k = 3
    assert (np.array_equal(obj.delete(n,m,k) , np.array([[(0,1),(2,3),(4,3)],[(1,2),(),()],[(2,4),(1,2,3),(1,)]], dtype = object)))
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 2
    m = 1
    k = 2
    assert (np.array_equal(obj.delete(n,m,k) , np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,3),(1,)]], dtype = object)))
    obj.transition_matrix = np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)
    n = 2
    m = 1
    k = 0
    assert (np.array_equal(obj.delete(n,m,k) , np.array([[(0,1),(2,3),(4,3)],[(1,2),(),(3,)],[(2,4),(1,2,3),(1,)]], dtype = object)))

# TODO test examples (remaining: transition)
def test_transition():
    k = 0
    assert (obj.transition(k) == [[['A11','B11','C11','D11'],['A12','B12','C12','D12']],[['A21','B21','C21','D21'],['A22','B22','C22','D22']]]).all

retcode = pytest.main()
