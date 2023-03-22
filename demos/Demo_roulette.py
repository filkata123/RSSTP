import numpy as np
from msrgym import robot_arm

#ONE ARM
n = 1
p = [90]
l = [2]
o = []
d = 20
feedback = [(-1.64, 1.15)]

#TWO ARMS
# n = 2
# p = [90, 120]
# l = [2, 1]
# o = []
# d = 10
#feedback = [(-1.64, 1.15), (1.0,0.07)]

left = 0
right = 1
actions = list([left,right])

try:
    arm = robot_arm(n, p, l, o, d, feedback, actions, True, True)
    
    print("*" * 20 + " Initial set of actions: 1 state " + "*" * 20)
    for x in range (20):
        arm.update_position(right)    
    for x in range (60):
        arm.update_position(left)

#     print("*" * 20 + " Reset position " + "*" * 20)
#     # Reset
#     for x in range (5):
#         arm.update_position(right)

#     print("*" * 20 + " Split initial node " + "*" * 20)
#     print(arm.split_node(0))
#     print("delete (0 -> 1) k = left")
#     print(arm.delete_conection_between_nodes(0, 1, left))
#     print("delete (1 -> 0) k = right")
#     print(arm.delete_conection_between_nodes(1, 0, right))

#     print("*" * 20 + " Try same movement with new transition matrix " + "*" * 20)
#     for x in range (7):
#         arm.update_position(right)
#     for x in range (9):
#         arm.update_position(left)

#     print("*" * 20 + "Merge nodes" + "*" * 20)
#     print(arm.merge_nodes(0, 1))

#     print("*" * 20 + " Reset position " + "*" * 20)
#     # Reset
#     for x in range (5):
#         arm.update_position(right)
    
#     print("*" * 20 + " Remove right action " + "*" * 20)
#     print(arm.delete_conection_between_nodes(0, 0, right))
#     arm.update_position(right)

#     print("*" * 20 + " Add right action " + "*" * 20)
#     print(arm.add_connection_between_nodes(0, 0, right))
#     arm.update_position(right)
except Exception as e:
    print("Exception encountered: " + str(e))  
