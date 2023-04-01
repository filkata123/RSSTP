import numpy as np
from msrgym import robot_arm

#ONE ARM
n = 1
p = [90]
l = [2]
o = []
d = 90
feedback = [(0.0, -2.0)]

#TWO ARMS
# n = 2
# p = [90, 120]
# l = [2, 1]
# o = []
# d = 10
#feedback = [(-1.64, 1.15), (1.0,0.07)]


right = 1
actions = list([right])

try:
    arm = robot_arm(n, p, l, o, d, feedback, actions, True, True)
    
    

    print("*" * 20 + " Initial set of actions: 1 state " + "*" * 20)
    for x in range (4):
        sensory_feedback = arm._ext.get_sensory_data()
        print("Sensory for loopin alussa(rivi 32): {}".format(sensory_feedback))
        arm.update_position(right)

        print("Get_data liikkumisen jälkeen(35): {}".format(arm._ext.get_sensory_data()))
        if (sensory_feedback != arm._ext.get_sensory_data()):
            if (arm._ext.get_sensory_data() == True):
                break
            print(arm.split_node(0))   

            print(sensory_feedback)
            print(arm._ext.get_sensory_data())


except Exception as e:
    print("Exception encountered: " + str(e))  
