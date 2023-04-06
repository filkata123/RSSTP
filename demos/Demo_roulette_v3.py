import numpy as np
from msrgym import robot_arm
from memory import Memory

#ONE ARM
n = 1
p = [90]
l = [2]
o = []
d = 90
feedback = [(0.0, 2.0)]

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

    # Move 4 times (full circle)
    for x in range (4):  
        arm.update_position(right)
        #print(Memory.memory)

        # Call compare_testing() as many times as there are element in Memory.memory
        for y in range(len(Memory.memory)):
            # Set arguments n and m for compare_testing()
            n = x-y
            m = x-y-1
            if (n >= 0) and (m >= 0):
                compare_value = arm.compare_testing(n, m)
                
                # Split node if a contradiction is found
                if (compare_value == 1):
                    transition_matrix = arm.get_transition_matrix()
                    most_recent_node = len(transition_matrix) - 1
                    arm.split_node(most_recent_node)

                    # Delete "wrong" transitions in transition matrix
                    # Deletes all the transitions between states except transitions (0,1), (1,2), (2,3), etc.
                    counter_test_x = 0
                    counter_test_y = 1
                    for i in range(len(arm.get_transition_matrix())-1):     # for every row except the last row
                        for j in range(len(arm.get_transition_matrix())):   # for every element in a row
                            # print("i, j:")
                            # print(i, j)
                            if (i, j) != (counter_test_x, counter_test_y):

                                arm.delete_conection_between_nodes(i, j, 1)
                                
                        counter_test_x += 1
                        counter_test_y = (counter_test_y + 1) % (len(arm.get_transition_matrix()))

                    for j in range(len(arm.get_transition_matrix())):       # for every element in the last row
                        if (j != 0) and (j != len(arm.get_transition_matrix())-1):
                            arm.delete_conection_between_nodes(len(arm.get_transition_matrix())-1, j, 1)
                            

    transition_matrix = arm.get_transition_matrix()
    print(transition_matrix)  
    arm.draw_graph_from_tm(transition_matrix)  

except Exception as e:
    print("Exception encountered: " + str(e))  

"""
    # Move #2
    for x in range (1):  
        arm.update_position(right)
        print(Memory.memory)
        compare_value = arm.compare_testing(x, x+1)
        if (compare_value == 2):
            break
    
    # Move #3
    for x in range(1):
        arm.update_position(right)
        print(Memory.memory)
        compare_value = arm.compare_testing(x+1, x+2)
        if (compare_value == 2):
            compare_value = arm.compare_testing(x, x+1)
            if (compare_value == 2):
                break
    
    # Move #4
    for x in range(1):
        arm.update_position(right)
        print(Memory.memory)
        compare_value = arm.compare_testing(x+2, x+3)
        if (compare_value == 2):
            break
        elif (compare_value == 1):
            #Split node
            transition_matrix = arm.get_transition_matrix()
            most_recent_node = len(transition_matrix) - 1
            print(most_recent_node)
            arm.split_node(most_recent_node)

            #Delete connections
            #deletes all the connections between nodes except connections (0,1), (1,2), (2,3), ...
            counter_test_x = 0
            counter_test_y = 1
            for i in range(len(arm.get_transition_matrix())-1):
                for j in range(len(arm.get_transition_matrix())):
                    # print("tm length:")
                    # print(len(arm.get_transition_matrix()))
                    # print("i, j:")
                    # print(i, j)
                    if (i, j) != (counter_test_x, counter_test_y):
                        
                        arm.delete_conection_between_nodes(i, j, 1)

                counter_test_x += 1
                counter_test_y = (counter_test_y + 1) % (len(arm.get_transition_matrix()))

    transition_matrix = arm.get_transition_matrix()
    print(transition_matrix)
    """


