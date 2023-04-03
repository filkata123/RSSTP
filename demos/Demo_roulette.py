import numpy as np
from msrgym import robot_arm
from memory import Memory

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

    # Split nodes 3 times because full circle takes 4 movements meaning 3 nodes need to be added.
    memory_length = len(Memory.memory)
    split_counter = 0
    for x in range(memory_length-1, memory_length-state_counter, -1):
        print(x)  
        compare_result = arm.compare_testing(x, x-1)
        if (compare_result == 1):
            print("split")
            arm.split_node(split_counter)
            print(x)

        tm = arm.get_transition_matrix()
        print(tm)
        print("-----------------------------------")
        split_counter += 1
    

    counter_test_x = 0
    counter_test_y = 1
    for i in range(len(arm.get_transition_matrix())):
        for j in range(len(arm.get_transition_matrix())):
            # print("tm length:")
            # print(len(arm.get_transition_matrix()))
            # print("i, j:")
            # print(i, j)
            if (i, j) != (counter_test_x, counter_test_y):
                
                arm.delete_conection_between_nodes(i, j, 1)

        counter_test_x += 1
        counter_test_y = (counter_test_y + 1) % 4


    tm = arm.get_transition_matrix()
    print(tm)


except Exception as e:
    print("Exception encountered: " + str(e))  
