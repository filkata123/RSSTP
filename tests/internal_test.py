import numpy as np
import pytest
from src.internal import Internal

obj = Internal(list([0,1,2,3,4]),0)

# -------------------------------------------------------------split--------------------------------------------------------------------------------------------
def test_split_1():
    n = 0
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[0,1],[2,3],[4,3],[0,1]],
                         [[1,2],[],[3],[1,2]],
                         [[2,4],[1,2,3],[1],[2,4]],
                         [[0,1],[2,3],[4,3],[0,1]]], dtype = object)
    assert (np.array_equal(obj.split(n) , expected))

def test_split_2():
    n = 1
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[0,1],[2,3],[4,3],[2,3]],
                         [[1,2],[],[3],[]],
                         [[2,4],[1,2,3],[1],[1,2,3]],
                         [[1,2],[],[3],[]]], dtype = object)
    assert (np.array_equal(obj.split(n) , expected))

def test_split_3():    
    n = 2
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[0,1],[2,3],[4,3],[4,3]],
                         [[1,2],[],[3],[3]],
                         [[2,4],[1,2,3],[1],[1]],
                         [[2,4],[1,2,3],[1],[1]]], dtype = object)
    assert (np.array_equal(obj.split(n) , expected))

def test_split_4():    
    n = 0
    obj.transition_matrix = np.array([[[0,1,2,3,4]]], dtype = object)

    expected = np.array([[[0,1,2,3,4],[0,1,2,3,4]],
                         [[0,1,2,3,4],[0,1,2,3,4]]], dtype = object)
    assert (np.array_equal(obj.split(n) , expected))

# -------------------------------------------------------------merge--------------------------------------------------------------------------------------------
def test_merge_1():
    n = 0
    m = 1
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[0,1,2,3],[3,4]],
                         [[1,2,3,4],[1]]], dtype = object)
    assert (np.array_equal(obj.merge(n,m) , expected ))

def test_merge_2():    
    n = 0
    m = 2
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object) 

    expected = np.array([[[0,1,2,3,4],[1,2,3]],
                         [[1,2,3],[]]], dtype = object)
    assert (np.array_equal(obj.merge(n,m) ,expected ))

def test_merge_3():
    n = 1
    m = 2
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[0,1],[2,3,4]],
                         [[1,2,4],[1,2,3]]], dtype = object)
    assert (np.array_equal(obj.merge(n,m) , expected ))

# -------------------------------------------------------------add----------------------------------------------------------------------------------------------
def test_add_1():
    n = 0
    m = 1
    k = 0
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[0,1],[0,2,3],[4,3]],
                         [[1,2],[],[3]],
                         [[2,4],[1,2,3],[1]]], dtype = object)
    assert (np.array_equal(obj.add(n,m,k) , expected))

def test_add_2():
    n = 1
    m = 1
    k = 3
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[0,1],[2,3],[4,3]],
                         [[1,2],[3],[3]],
                         [[2,4],[1,2,3],[1]]], dtype = object)
    assert (np.array_equal(obj.add(n,m,k) , expected ))

def test_add_3():
    n = 2
    m = 2
    k = 0
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[0,1],[2,3],[4,3]],
                         [[1,2],[],[3]],
                         [[2,4],[1,2,3],[0,1]]], dtype = object)
    assert (np.array_equal(obj.add(n,m,k) , expected))

# -------------------------------------------------------------delete-------------------------------------------------------------------------------------------
def test_delete_1():
    n = 0
    m = 0
    k = 0
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[1],[2,3],[4,3]],
                         [[1,2],[],[3]],
                         [[2,4],[1,2,3],[1]]], dtype = object)
    assert (np.array_equal(obj.delete(n,m,k) , expected))

def test_delete_2():
    n = 1
    m = 2
    k = 3
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[0,1],[2,3],[4,3]],
                         [[1,2],[],[]],
                         [[2,4],[1,2,3],[1]]], dtype = object)
    assert (np.array_equal(obj.delete(n,m,k) , expected))

def test_delete_3():
    n = 2
    m = 1
    k = 2
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = np.array([[[0,1],[2,3],[4,3]],
                         [[1,2],[],[3]],
                         [[2,4],[1,3],[1]]], dtype = object)
    assert (np.array_equal(obj.delete(n,m,k) , expected))

def test_delete_4():
    n = 2
    m = 1
    k = 0
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = -1
    assert (np.array_equal(obj.delete(n,m,k) , expected))

# -------------------------------------------------------------transition---------------------------------------------------------------------------------------
def test_transition_1():
    k = 0
    obj.current_state = 0
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = [0]
    assert (obj.transition(k) in expected)

def test_transition_2():
    k = 3
    obj.current_state = 0
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = [1,2]
    assert (obj.transition(k) in expected)

def test_transition_3():
    k = 2
    obj.current_state = 2
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = [0,1]
    assert (obj.transition(k) in expected)

def test_transition_4():
    k = 0
    obj.current_state = 1
    obj.transition_matrix = np.array([[[0,1],[2,3],[4,3]],
                                      [[1,2],[],[3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object)

    expected = [-1]
    assert (obj.transition(k) in expected)
    