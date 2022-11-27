import numpy as np
from msrgym import robot_arm

n = 1
l = 2
o = [[1,2],1,[-1,-2],1]
p = 95
feedback = (-0.35, 1.97)

left = 0
right = 1

actions = list([left,right])

try:
    arm = robot_arm(n, l, o, p, feedback, actions)
    
    for x in range (7):
        arm.update_position(right)
    for x in range (9):
        arm.update_position(left)

    # Reset
    for x in range (5):
        arm.update_position(right)
    
    
    arm.split_node(0)
    print("delete 0 -> 1 k = left")
    arm.delete_conection_between_nodes(0, 1, left)
    print("delete 1 -> 0 k = right")
    arm.delete_conection_between_nodes(1, 0, right)
    for x in range (7):
        arm.update_position(right)
    for x in range (9):
        arm.update_position(left)
    #arm.add_connection_between_nodes(0,0, left)

    #for x in range (10):
    #   arm.update_position(left) 
except Exception as e:
    print("Exception encountered: " + str(e))    