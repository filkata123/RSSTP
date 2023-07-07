import pytest
from external import External

def test_distance_from_obstacle():
    # one arm
    n = 1
    p = [95]
    l = [2]
    o = [[1,2],1,[-1,-2],1]
    d = 1
    feedback = [(-0.14,2.0)]
    obj = External(n, p, l, o, d, feedback)

    expected = [[0.17004273426230032, 3.075414089390182]]

    assert obj.distance_from_obstacle() == expected

test_distance_from_obstacle()

def test_distance_from_obstacle2():
    # three arms
    n = 3
    p = [330,3,357] 
    l = [3,2,1]
    o = [[1.5,1],0.5,[1.5,-1.5],0.5]
    d = 5
    feedback = [(2.6, -1.5), (4.38, -2.41), (5.25, -2.91)] 
    obj = External(n, p, l, o, d, feedback)

    expected = [[2.2313000567495327, 0.6000000000000001], [3.9634627812943615, 2.5203476621077914], [4.917619403391124, 3.5063200071886422]]

    assert obj.distance_from_obstacle() == expected

test_distance_from_obstacle2()

def test_get_sensory_data_float1():
    # one arm
    # arm is at the sensory feedbackpoint
    n = 1
    p = [90]
    l = [2]
    o = [[1,2],0.1,[-1,-2],0.1]
    d = 1
    feedback = [(0,2.0)]
    obj = External(n, p, l, o, d, feedback)

    expected = 1.0

    assert obj.get_sensory_data_float() == expected

test_get_sensory_data_float1()

def test_get_sensory_data_float2():
    # one arm
    # arm is as far away from sensory feedbackpoint as possible
    n = 1
    p = [90]
    l = [2]
    o = [[1,2],0.1,[-1,-2],0.1]
    d = 1
    feedback = [(0,-2.0)]
    obj = External(n, p, l, o, d, feedback)

    expected = 0.0

    assert obj.get_sensory_data_float() == expected

test_get_sensory_data_float2()

def test_get_sensory_data_float3():
    # one arm
    # arm is not at the sensory feedback point
    n = 1
    p = [90]
    l = [2]
    o = [[1,2],0.1,[-1,-2],0.1]
    d = 1
    feedback = [(0.3, 1.0)]
    obj = External(n, p, l, o, d, feedback)

    expected = 0.6570236076350138

    assert obj.get_sensory_data_float() == expected

test_get_sensory_data_float3()

def test_get_sensory_data_float4():
    # three arms
    # the arm is in the sensory feedback point
    n = 3
    p = [330,3,357] 
    l = [3,2,1]
    o = [[1.5,1],0.5,[1.5,-1.5],0.5]
    d = 5
    feedback = [(2.6, -1.5), (4.38, -2.41), (5.25, -2.91)] 
    obj = External(n, p, l, o, d, feedback)

    expected = 1.0

    assert obj.get_sensory_data_float() == expected

test_get_sensory_data_float4()

def test_get_sensory_data_float5():
    # three arms
    # the arm is not in the sensory feedback point
    n = 3
    p = [330,3,357] 
    l = [3,2,1]
    o = [[1.5,1],0.5,[1.5,-1.5],0.5]
    d = 5
    feedback = [(1.6, -1.5), (4.28, -2.0), (4.25, 0.0)] 
    obj = External(n, p, l, o, d, feedback)

    expected = 0.8212809738261679

    assert obj.get_sensory_data_float() == expected

test_get_sensory_data_float5()