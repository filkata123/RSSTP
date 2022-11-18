# Get the current working directory
import pytest

from src.external import External

# fixture resets all setings on use
@pytest.fixture
def external_fixture():
    n = 1
    p = 95.0
    l = 2.0
    o = [[1,2],1,[-1,-2],1]
    feedback = (-0.14,2.0)

    return External(n, p, l, o, feedback)

def test_update_left(external_fixture):
    external_fixture.update(0)

    assert external_fixture.get_position() == (96.0, (-0.21, 1.99))

def test_update_right(external_fixture):
    external_fixture.update(1)

    assert external_fixture.get_position() == (94.0, (-0.14, 2.0))

def test_no_feedback(external_fixture):
    external_fixture.update(0)

    assert external_fixture.get_sensory_data() == 0

def test_feedback(external_fixture):
    external_fixture.update(1)

    assert external_fixture.get_sensory_data() == 1

def test_Hit_Obs(external_fixture):
    for x in range(10):
        external_fixture.update(1)
    assert external_fixture.get_position()[0] == 91


def test_initial_p_intersects_object():
    n = 1
    p = 90.0
    l = 2.0
    o = [[1,2],1,[-1,-2],1]
    feedback = (-0.14,2.0)

    with pytest.raises(Exception) as exc_info:
        External(n, p, l, o, feedback)

    assert exc_info.value.args[0] == 'Initial position must not intersect with objects'

    
