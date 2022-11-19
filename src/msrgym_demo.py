import numpy as np
from msrgym import robot_arm

n = 1
l = 2
o = [[1,2],1,[-1,-2],1]
p = 95
feedback = (-0.35, 1.97)

left = 0
right = 1
actions = np.array([[(1,)],], dtype = object)

try:
    arm = robot_arm(n, l, o, p, feedback, actions)

    for x in range (7):
        arm.update_position(right)

    arm.update_position(left)

    arm.split_node(0)
    #arm.add_connection_between_nodes(0,0, left)

    #for x in range (10):
    #   arm.update_position(left)
except Exception as e:
    print("Exception encountered: " + str(e))    