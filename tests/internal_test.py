import numpy as np
import pytest
from internal import Internal

# ----------------------------------------------------transition matrix getter and setter--------------------------------------------------------------------------
def test_get_transition_matrix():
    obj = Internal(list([0,1,2,3]))
    expected = np.ndarray(shape = (1,1),dtype= object)
    expected[0,0] = list([0,1,2,3])

    assert(obj.get_transition_matrix() == expected)

def test_set_transition_matrix_1():
    obj = Internal(list([0,1,2,3]))
    obj.set_transition_matrix(list([0,1]))
    expected = np.ndarray(shape = (1,1),dtype= object)
    expected[0,0] = list([0,1])
    assert(obj.get_transition_matrix() == expected)

def test_set_transition_matrix_2():
    obj = Internal(list([0,1,2,3]))
    obj.set_transition_matrix(np.array([[[1,2],[1,3]],
                                        [[2,3],[1]]],dtype = object))
    expected = np.array([[[1,2],[1,3]],
                         [[2,3],[1]]],dtype = object)
    assert(np.array_equal(obj.get_transition_matrix(),expected))

def test_set_transition_matrix_3():
    obj = Internal(list([0,1,2,3]))
    obj.set_transition_matrix(np.array([[[1,2],[1,3]],
                                        [[2,3],[1,1]]],dtype = object))
    expected = np.ndarray(shape =(2,2),dtype= object)
    expected[0,0] = list([1,2]);expected[0,1] = list([1,3])
    expected[1,0] = list([2,3]);expected[1,1] = list([1,1])
    assert(np.array_equal(obj.get_transition_matrix(),expected))

# TODO msh uncomment this
# def test_set_transition_matrix_4(): #adding input validation to the setter makes this work but breaks shabbirs tests
#     obj = Internal(list([0,1,2,3]))
#     assert(obj.set_transition_matrix(np.array([[[0,1],[2,5],[4,3]],
#                                                [[2,4],[1,2,3],[1]]], dtype = object)) == -1)

def test_get_current_state():
    obj = Internal(list([0,1,2,3]))
    assert(obj.get_current_state() == 0)

def test_set_current_state_1():
    obj = Internal(np.array([[[0,1],[2,5]],
                             [[2,4],[1,2,3]]], dtype = object))
    obj.set_current_state(1)
    assert(obj.get_current_state() == 1)

def test_set_current_state_2():
    obj = Internal(list([0,1,2,3]))
    assert(obj.set_current_state(1) == -1)

def test_set_current_state_3():
    obj = Internal(list([0,1,2,3]))
    assert(obj.set_current_state(-4) == -1)

# -------------------------------------------------------------split--------------------------------------------------------------------------------------------
#-------------Transition matrix abnormal dimension check---------------------------

def test_split_abnormal_1():
    # Row is not equal to column
    n = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.split(n) , -1))

def test_split_abnormal_2():
    # Row is not equal to column
    n = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.split(n) , -1))
    
#def test_split_abnormal_3():  #Mourad: this matrix is not a proper matrix so set_transition_matrix() blocks it
#    # Number of col is not equal to specific row
#    n = 0
#    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
#                             [[1,2], [],[3]],
#                             [[1,2], [3]],
#                             [[2,4],[1,2,3],[1]]], dtype = object))
#
#    assert (np.array_equal(obj.split(n) , -1))
 
def test_split_abnormal_4():
     # Out of boundary state or stage
    n = 4
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.split(n) , -1))

def test_split_abnormal_5():
     # Out of boundary state or stage

    n = 3
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.split(n) , -1))



def test_split_abnormal_7():
     # Boundary test already done in normal test mode
    n = 2
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1],[2,5],[4,3],[4,3]],
                            [[1,2],[],[3],[3]],
                            [[2,4],[1,2,3],[1],[1]],
                            [[2,4],[1,2,3],[1],[1]]], dtype = object)
    
    assert (np.array_equal(obj.split(n) , expected))

#-----------------------normal tests-------------------------
def test_split_1():
    n = 0
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1],[2,3],[4,3],[0,1]],
                         [[1,2],[],[3],[1,2]],
                         [[2,4],[1,2,3],[1],[2,4]],
                         [[0,1],[2,3],[4,3],[0,1]]], dtype = object)
    assert (np.array_equal(obj.split(n) , expected))

def test_split_2():
    n = 1
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1],[2,3],[4,3],[2,3]],
                         [[1,2],[],[3],[]],
                         [[2,4],[1,2,3],[1],[1,2,3]],
                         [[1,2],[],[3],[]]], dtype = object)
    assert (np.array_equal(obj.split(n) , expected))

def test_split_3():    
    n = 2
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1],[2,3],[4,3],[4,3]],
                         [[1,2],[],[3],[3]],
                         [[2,4],[1,2,3],[1],[1]],
                         [[2,4],[1,2,3],[1],[1]]], dtype = object)
    assert (np.array_equal(obj.split(n) , expected))

def test_split_4():  
    n = 0
    obj = Internal(list([0,1,2,3,4]))

    expected = np.ndarray(shape= (2,2), dtype= object)
    expected[0,0]=list([0,1,2,3,4]) ;expected[0,1]= list([0,1,2,3,4])
    expected[1,0]=list([0,1,2,3,4]) ;expected[1,1]= list([0,1,2,3,4])
    assert (np.array_equal(obj.split(n) , expected))

# -------------------------------------------------------------merge--------------------------------------------------------------------------------------------
#-------------Transition matrix abnormal dimension check---------------------------
def test_merge_abnormal_1():
    # Row is not equal to column
    n = 0
    m = 1
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.merge(n,m) , -1))

def test_merge_abnormal_2():
    # Row is not equal to column
    n = 0
    m = 1
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.merge(n,m) , -1))
    
# def test_merge_abnormal_3(): #same as above improper matrix does not make it past set_transition_matrix()
#      # Number of col is not equal to specific row

#     n = 0
#     m = 1
#     obj = Internal(np.array([[[0,1],[2,5],[4,3]],
#                              [[1,2], [3]],
#                              [[1,2],[], [3]],
#                              [[2,4],[1,2,3],[1]]], dtype = object))

#     assert (np.array_equal(obj.merge(n,m) , -1))
 
def test_merge_abnormal_4():
     # Merge comound out of boundary

    n = 0
    m = 5
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.merge(n,m) , -1))

def test_merge_abnormal_5():
     # Merge comound out of boundary

    n = 5
    m = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.merge(n,m) , -1))

def test_merge_abnormal_6():
     # Same row and colums

    n = 2
    m = 2
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.merge(n,m) , -1))



# def test_merge_abnormal_7(): #Mourad: same as split case
#      # Empty row check

#     n = 0
#     m = 2
#     obj = Internal(np.array([[]], dtype = object)) #Mourad: again not a 1x1 matrix

#     assert (np.array_equal(obj.merge(n,m) , -1))

#-----------------------normal tests-------------------------
def test_merge_1():
    n = 0
    m = 1
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1,2,3],[3,4]],
                         [[1,2,3,4],[1]]], dtype = object)
    assert (np.array_equal(obj.merge(n,m) , expected ))

def test_merge_2():    
    n = 0
    m = 2
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object)) 

    expected = np.array([[[0,1,2,3,4],[1,2,3]],
                         [[1,2,3],[]]], dtype = object)
    assert (np.array_equal(obj.merge(n,m) ,expected ))

def test_merge_3():
    n = 1
    m = 2
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1],[2,3,4]],
                         [[1,2,4],[1,2,3]]], dtype = object)
    assert (np.array_equal(obj.merge(n,m) , expected ))

# -------------------------------------------------------------add----------------------------------------------------------------------------------------------
#-------------Abnormal Tests ---------------------------

def test_add_abnormal_1():
    # Row is not equal to column
    n = 0
    m = 1
    k = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.add(n,m,k) , -1))

def test_add_abnormal_2():
    # Row is not equal to column
    n = 0
    m = 1
    k = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.add(n,m,k) , -1))
    
# def test_add_abnormal_3():
    # Number of col is not equal to specific row

    # n = 0
    # m = 1
    # k = 0
    # obj = Internal(np.array([[[0,1],[2,5],[4,3]],
    #                                   [[1,2], [3]],
    #                                   [[1,2],[], [3]],
    #                                   [[2,4],[1,2,3],[1]]], dtype = object))

    # assert (np.array_equal(obj.add(n,m,k) , -1))
 
def test_add_abnormal_4():
     # Merge comound out of boundary

    n = 0
    m = 5
    k = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.add(n,m,k) , -1))

def test_add_abnormal_5():
    # Merge comound out of boundary

    n = 5
    m = 0
    k = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                                      [[1,2],[], [3]],
                                      [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.add(n,m,k) , -1))


# def test_add_abnormal_6():
#      # Empty row check

#     n = 0
#     m = 0
#     k = 0
#     obj = Internal(np.array([[]], dtype = object))

#     assert (np.array_equal(obj.add(n,m,k) , -1))
#-----------------------normal tests-------------------------
def test_add_1():
    n = 0
    m = 1
    k = 0
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1],[0,2,3],[4,3]],
                         [[1,2],[],[3]],
                         [[2,4],[1,2,3],[1]]], dtype = object)
    assert (np.array_equal(obj.add(n,m,k) , expected))

def test_add_2():
    n = 1
    m = 1
    k = 3
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1],[2,3],[4,3]],
                         [[1,2],[3],[3]],
                         [[2,4],[1,2,3],[1]]], dtype = object)
    assert (np.array_equal(obj.add(n,m,k) , expected ))

def test_add_3():
    n = 2
    m = 2
    k = 0
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1],[2,3],[4,3]],
                         [[1,2],[],[3]],
                         [[2,4],[1,2,3],[0,1]]], dtype = object)
    assert (np.array_equal(obj.add(n,m,k) , expected))

# -------------------------------------------------------------delete-------------------------------------------------------------------------------------------
#-------------Abnormal Tests ---------------------------

def test_delete_1_1():
    # Row is not equal to column
    n = 0
    m = 1
    k = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.delete(n,m,k) , -1))

def test_delete_1_2():
    # Row is not equal to column
    n = 0
    m = 1
    k = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.delete(n,m,k) , -1))
    
# def test_delete_1_3():
#      # Number of col is not equal to specific row

#     n = 0
#     m = 1
#     k = 0
#     obj = Internal(np.array([[[0,1],[2,5],[4,3]],
#                                       [[1,2], [3]],
#                                       [[1,2],[], [3]],
#                                       [[2,4],[1,2,3],[1]]], dtype = object))

#     assert (np.array_equal(obj.delete(n,m,k) , -1))
 
def test_delete_1_4():
     # Merge comound out of boundary

    n = 0
    m = 5
    k = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.delete(n,m,k) , -1))

def test_delete_1_5():
     # Merge comound out of boundary

    n = 5
    m = 0
    k = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    assert (np.array_equal(obj.delete(n,m,k) , -1))


# def test_delete_1_6():
#      # Empty row check

#     n = 0
#     m = 0
#     k = 0
#     obj = Internal(np.array([[]], dtype = object))

#     assert (np.array_equal(obj.delete(n,m,k) , -1))
#-----------------------normal tests-------------------------
def test_delete_1():
    n = 0
    m = 0
    k = 0
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[1],[2,3],[4,3]],
                         [[1,2],[],[3]],
                         [[2,4],[1,2,3],[1]]], dtype = object)
    assert (np.array_equal(obj.delete(n,m,k) , expected))

def test_delete_2():
    n = 1
    m = 2
    k = 3
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1],[2,3],[4,3]],
                         [[1,2],[],[]],
                         [[2,4],[1,2,3],[1]]], dtype = object)
    assert (np.array_equal(obj.delete(n,m,k) , expected))

def test_delete_3():
    n = 2
    m = 1
    k = 2
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = np.array([[[0,1],[2,3],[4,3]],
                         [[1,2],[],[3]],
                         [[2,4],[1,3],[1]]], dtype = object)
    assert (np.array_equal(obj.delete(n,m,k) , expected))

def test_delete_4():
    n = 2
    m = 1
    k = 0
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))

    expected = -1
    assert (np.array_equal(obj.delete(n,m,k) , expected))

# -------------------------------------------------------------transition---------------------------------------------------------------------------------------
#-------------Abnormal Tests ---------------------------
def test_transition_abnormal_1():
    # Row is not equal to column
    k = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))
    obj.set_current_state(0)

    assert (np.array_equal(obj.transition(k) , -1))

def test_transition_abnormal_2():
    # Row is not equal to column
    k = 0
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))
    obj.set_current_state(0)

    assert (np.array_equal(obj.transition(k) , -1))
    
# def test_transition_1_3():
#      # Number of col is not equal to specific row

#     k = 0
#     obj = Internal(np.array([[[0,1],[2,5],[4,3]],
#                                       [[1,2], [3]],
#                                       [[1,2],[], [3]],
#                                       [[2,4],[1,2,3],[1]]], dtype = object))
#     obj.set_current_state(0)

#     assert (np.array_equal(obj.transition(k) , -1))
 
def test_transition_abnormal_4():
     # Merge comound out of boundary
    k = 6
    obj = Internal(np.array([[[0,1],[2,5],[4,3]],
                             [[1,2],[], [3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))
    obj.set_current_state(0)

    assert (np.array_equal(obj.transition(k) , -1))

# def test_transition_1_5(): this time the set_current_state() blocks invalid input
#      # Invalid current state

#     k = 0
#     obj = Internal(np.array([[[0,1],[2,5],[4,3]],
#                                       [[1,2],[], [3]],
#                                       [[2,4],[1,2,3],[1]]], dtype = object))
#     obj.set_current_state(5)

#     assert (np.array_equal(obj.transition(k) , -1))
    
# def test_transition_1_6():
#      # Empty row check

#     k = 0
#     obj = Internal(np.array([[]], dtype = object))
#     obj.set_current_state(0)

    assert (np.array_equal(obj.transition(k) , -1))
#-----------------------normal tests-------------------------
def test_transition_1():
    k = 0
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))
    obj.set_current_state(0)

    expected = [0]
    assert (obj.transition(k) in expected)

def test_transition_2():
    k = 3
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))
    obj.set_current_state(0)

    expected = [1,2]
    assert (obj.transition(k) in expected)

def test_transition_3():
    k = 2
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))
    obj.set_current_state(2)

    expected = [0,1]
    assert (obj.transition(k) in expected)

def test_transition_4():
    k = 0
    obj = Internal(np.array([[[0,1],[2,3],[4,3]],
                             [[1,2],[],[3]],
                             [[2,4],[1,2,3],[1]]], dtype = object))
    obj.set_current_state(1)

    expected = [-1]
    assert (obj.transition(k) in expected)
    