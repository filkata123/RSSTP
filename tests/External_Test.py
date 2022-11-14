# Example file for testing suite
import unittest
# Get the current working directory
import External

n = 1
p = 90
l = 2
o = [[1,2],1,[-1,-2],1]

obj = External.External(n,p,l,o)

class TestCalc(unittest.TestCase):
    def test_feedback(self):
        assert External.Get_S([1,2],[1,2]) == 1
    def test_no_feedback(self):
        assert External.Get_S([0,2],[1,2]) == 0
    
    def test_Hit_Obs(self):
        assert obj.hitObstacle([1,2], [1,2]) == True
    def test_Miss_Obs(self):
        assert obj.hitObstacle([2,0], [1,2]) == False
        
    def test_get_position(self):
        assert obj.getPosition(90) == (0,2)
    def test_get_position_Wrong_length(self):
        assert obj.getPosition(90) == (2,0)


    def test_update_right(self):
        assert obj.update(0) == 91
    def test_update_left(self):
        assert obj.update(1) == 89
        
if __name__ == '__main__':
    unittest.main()