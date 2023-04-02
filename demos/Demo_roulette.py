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
    # Moving untill finding sensory feedback point.
    for x in range (360):  
        arm.update_position(right)
        print("x:{}".format(x))
        if (arm._ext.get_sensory_data() == True):
            break
    print("sensory feedback is True -> arm is in sensory feedback point")

    # Move a full circle
    state_counter = 0
    for x in range (360):
        arm.update_position(right)
        state_counter += 1
        if (arm._ext.get_sensory_data() == True):
            break
    print("the arm rotated a full circle.")

    # x = muistin pituus
    #
    #for loop: (x --> x - state_counter, x--)

        #compare_result = arm.compare_testing(x, x-1)
        # if (compare_result == 1):
        #     arm.split_node(1)

    tm = arm.get_transition_matrix()
    print(tm)


    

        

        # sensory_feedback = arm._ext.get_sensory_data()
        # print("Sensory for loopin alussa(rivi 32): {}".format(sensory_feedback))
        # print("Get_data liikkumisen jälkeen(35): {}".format(arm._ext.get_sensory_data()))
        # if (sensory_feedback != arm._ext.get_sensory_data()):
        #     if (arm._ext.get_sensory_data() == True):
        #         break
        #     print(arm.split_node(0))   

        #     print(sensory_feedback)
        #     print(arm._ext.get_sensory_data())


except Exception as e:
    print("Exception encountered: " + str(e))  
