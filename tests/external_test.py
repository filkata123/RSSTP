# Get the current working directory
import pytest

from src.external import External

@pytest.fixture
def external_object():
    n = 1
    p = 90.0
    l = 2.0
    o = [[1,2],1,[-1,-2],1]

    return External(n,p,l,o)

def test_update_right(external_object):
    assert external_object.update(0) == 91.0

def test_get_position_to_the_right(external_object):
    external_object.l=2.0
    assert external_object.getPosition(91.0) == (-0.03,2.0)

def test_Hit_Obs(external_object):
    assert external_object.hitObstacle((1.0,2.0)) == True

def test_feedback(external_object):
    assert external_object.getSensoryData((-0.14,2.0)) == 1

def test_update_left(external_object):
    external_object.p=90.0
    assert external_object.update(1) == 89.0

def test_get_position_to_the_left(external_object):
    external_object.l=2.0
    assert external_object.getPosition(89) == (0.03,2.0)

def test_Miss_Obs(external_object):
    assert external_object.hitObstacle((1.6,1.2)) == False #p=36.86

def test_no_feedback(external_object):
    assert external_object.getSensoryData((1.0,2.0)) == 0
