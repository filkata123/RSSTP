# Get the current working directory
import pytest

from external import External

# fixture resets all setings on use
@pytest.fixture
def external_fixture_one_arm():
    n = 1
    p = [95]
    l = [2]
    o = [[1,2],1,[-1,-2],1]
    d = 1
    feedback = [(-0.14,2.0)]

    return External(n, p, l, o, d, feedback)

def test_update_left(external_fixture_one_arm):
    external_fixture_one_arm.update(0)

    assert external_fixture_one_arm.get_position() == ([96.0], [(-0.21, 1.99)])

def test_update_right(external_fixture_one_arm):
    external_fixture_one_arm.update(1)

    assert external_fixture_one_arm.get_position() == ([94.0], [(-0.14, 2.0)])

def test_no_feedback(external_fixture_one_arm):
    external_fixture_one_arm.update(0)

    assert external_fixture_one_arm.get_sensory_data() == 0

def test_feedback(external_fixture_one_arm):
    external_fixture_one_arm.update(1)

    assert external_fixture_one_arm.get_sensory_data() == 1

def test_hit_obs(external_fixture_one_arm):
    for x in range(10):
        external_fixture_one_arm.update(1)
    assert external_fixture_one_arm.get_position()[0] == [91]


def test_initial_p_intersects_object():
    n = 1
    p = [90]
    l = [2]
    o = [[1,2],1,[-1,-2],1]
    d = 1
    feedback = [(-0.14,2.0)]

    with pytest.raises(Exception) as exc_info:
        External(n, p, l, o, d, feedback)

    assert exc_info.value.args[0] == 'Initial position must not intersect with obstacles'

def test_no_objects_one_arms(capsys):
    n = 1
    p = [0]
    l = [3]
    o = []
    d = 5
    feedback = [(3.0, 0.0)]
    
    External(n, p, l, o, d, feedback)
    captured = capsys.readouterr()
    assert captured.out == 'no obstacles in space\n'

#----------------------------------THREE ARMS-----------------------------------------------------#
@pytest.fixture
def external_fixture_three_arm():
    n = 3
    p = [330,3,357] 
    l = [3,2,1]
    o = [[1.5,1],0.5,[1.5,-1.5],0.5]
    d = 5
    #feedback = [(3.0, 0.0),(1.0,0.07),(2.0,0.07)]
    feedback = [(2.6, -1.5), (4.38, -2.41), (5.25, -2.91)] 
    return External(n, p, l, o, d, feedback)

def test_update_joint0_left(external_fixture_three_arm):
    external_fixture_three_arm.update(0)

    assert external_fixture_three_arm.get_position() == ([335, 3, 357], [(2.72, -1.27), (4.57, -2.02), (5.48, -2.44)])

def test_update_joint0_right(external_fixture_three_arm):
    external_fixture_three_arm.update(1)

    assert external_fixture_three_arm.get_position() == ([330, 3, 357], [(2.6, -1.5), (4.38, -2.41), (5.25, -2.91)])

def test_update_joints_joint1_left(external_fixture_three_arm):
    external_fixture_three_arm.update(2)

    assert external_fixture_three_arm.get_position() == ([330, 8, 357], [(2.6, -1.5), (4.45, -2.25), (5.36, -2.67)])

def test_update_joint1_right(external_fixture_three_arm):
    external_fixture_three_arm.update(3)

    assert external_fixture_three_arm.get_position() == ([330, 358, 357], [(2.6, -1.5), (4.3, -2.56), (5.12, -3.13)])

def test_update_joint2_left(external_fixture_three_arm):
    external_fixture_three_arm.update(4)

    assert external_fixture_three_arm.get_position() == ([330, 3, 2], [(2.6, -1.5), (4.38, -2.41), (5.29, -2.83)])

def test_update_joint2_right(external_fixture_three_arm):
    external_fixture_three_arm.update(5)

    assert external_fixture_three_arm.get_position() == ([330, 3, 352], [(2.6, -1.5), (4.38, -2.41), (5.2, -2.98)])


def test_no_feedback(external_fixture_three_arm):
    external_fixture_three_arm.update(0)

    assert external_fixture_three_arm.get_sensory_data() == 0

def test_feedback(external_fixture_three_arm):

    assert external_fixture_three_arm.get_sensory_data() == 1

@pytest.fixture
def external_fixture_three_arm_2():
    n = 3
    p = [0,178,182] 
    l = [3,2,1]
    o = [[1.5,1],0.5,[1.5,-1.5],0.5]
    d = 5
    feedback = [(3.0, 0.0),(1.0,0.07),(2.0,0.07)]
    return External(n, p, l, o, d, feedback)

def test_3joints_move(external_fixture_three_arm_2):
    for x in range (3):

        if x%3 == 0:
            external_fixture_three_arm_2.update(0)
        elif x%3 ==1:
            external_fixture_three_arm_2.update(3)
        elif x%3==2:           
            external_fixture_three_arm_2.update(4)
    
    assert external_fixture_three_arm_2.get_position()[0] == [5, 173, 187]

def test_hit_obs_1(external_fixture_three_arm_2,capsys):
    for x in range(7):
        external_fixture_three_arm_2.update(1)
        captured = capsys.readouterr()
    
    assert captured.out == "Position of joint 0 ((2.46, -1.72)) is unreachable due to object 1! \n\n"

@pytest.fixture
def external_fixture_three_arm_3():
    n = 3
    p = [330, 3, 237] 
    l = [3,2,1]
    o = [[1.5,1],0.5,[1.5,-1.5],0.5]
    d = 5
    feedback = [(3.0, 0.0),(1.0,0.07),(2.0,0.07)]
    return External(n, p, l, o, d, feedback)

def test_hit_obs_0(external_fixture_three_arm_3,capsys):
    for x in range(13):
        external_fixture_three_arm_3.update(0)
        captured = capsys.readouterr()
    
    assert captured.out == "Position of joint 0 ((2.82, 1.03)) is unreachable due to object 0! \n\n"

@pytest.fixture
def external_fixture_three_arm_4():
    n = 3
    p = [15, 3, 237]
    l = [3,2,1]
    o = [[1.5,1],0.5,[1.5,-1.5],0.5]
    d = 5
    feedback = [(3.0, 0.0),(1.0,0.07),(2.0,0.07)]
    return External(n, p, l, o, d, feedback)

def test_hit_joints_not_adjacent(external_fixture_three_arm_4,capsys):
    for x in range(35):
        external_fixture_three_arm_4.update(3)
        captured = capsys.readouterr()
    
    assert captured.out == "arm 0 intersects with arm 2! \n\n"

@pytest.fixture
def external_fixture_three_arm_5():
    n = 3
    p = [15, 218, 237]
    l = [3,2,1]
    o = [[1.5,1],0.5,[1.5,-1.5],0.5]
    d = 5
    feedback = [(3.0, 0.0),(1.0,0.07),(2.0,0.07)]
    return External(n, p, l, o, d, feedback)

def test_hit_joints_adjacent(external_fixture_three_arm_5,capsys):
    for x in range(12):
        external_fixture_three_arm_5.update(5)
        captured = capsys.readouterr()
    
    assert captured.out == "arm 2 intersects with arm 1! \n\n"

@pytest.fixture
def external_fixture_three_arm_6():
    n = 3
    p = [15, 218, 182]
    l = [3,2,1]
    o = [[1.5,1],0.5,[1.5,-1.5],0.5]
    d = 5
    feedback = [(3.0, 0.0),(1.0,0.07),(2.0,0.07)]
    return External(n, p, l, o, d, feedback)

def test_hit_obs_joint1(external_fixture_three_arm_6,capsys):
    for x in range(2):
        external_fixture_three_arm_6.update(1)
        captured = capsys.readouterr()
    
    assert captured.out == "Position of joint 1 ((2.99, 0.26)) is unreachable due to object 1! \n\n"   


def test_no_objects_Three_arms(capsys):
    n = 3
    p = [0,178,183]
    l = [3,2,1]
    o = []
    d = 5
    feedback = [(3.0, 0.0),(1.0,0.07),(2.0,0.07)]
    
    External(n, p, l, o, d, feedback)
    captured = capsys.readouterr()
    assert captured.out == 'no obstacles in space\n'

def test_initial_p_intersects_object():
    n = 3
    p = [0,178,180]
    l = [3,2,1]
    o = [[1.5,1],0.5,[1.5,-1.5],0.5]
    d = 5
    feedback = [(3.0, 0.0),(1.0,0.07),(2.0,0.07)]
    with pytest.raises(Exception) as exc_info:
        External(n, p, l, o, d, feedback)

    assert exc_info.value.args[0] == 'Initial position must not intersect with obstacles'

    
