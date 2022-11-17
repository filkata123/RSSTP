# Example file for testing suite
import os
cwd = os.getcwd()

import sys
sys.path.append(cwd+'/src/')
# Get the current working directory
import External
n = 1
p = 90.0
l = 2.0
o = [[1,2],1,[-1,-2],1]

obj = External.External(n,p,l,o)

#add a proper test case
class TestCalc():

    def test_update_right(self):
        assert obj.update(0) == 91.0
    def test_get_position_to_the_right(self):
        obj.l=2.0
        assert obj.getPosition(91.0) == (0.0,2.0)
    def test_Hit_Obs(self):
        assert obj.hitObstacle((1.0,2.0)) == True
    def test_feedback(self):
        assert obj.getSensoryData((-0.14,2.0)) == 1

    def test_update_left(self):
        obj.p=90.0
        assert obj.update(1) == 89.0
    def test_get_position_to_the_left(self):
        obj.l=2.0
        assert obj.getPosition(91) == (0.0,2.0)
    def test_Miss_Obs(self):
        assert obj.hitObstacle((1.6,1.2)) == False #p=36.86
    def test_no_feedback(self):
        assert obj.getSensoryData((1.0,2.0)) == 0
        


