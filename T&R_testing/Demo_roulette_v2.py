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
    # Move #1
    for x in range (1):  
        arm.update_position(right)
        print(Memory.memory)
    
    # Move #2
    for x in range (1):  
        arm.update_position(right)
        print(Memory.memory)
        compare_value = arm.compare_testing(x, x+1)
        if (compare_value == 3):
            break
    
    # Move #3
    for x in range(1):
        arm.update_position(right)
        print(Memory.memory)
        compare_value = arm.compare_testing(x+1, x+2)
        if (compare_value == 3):
            compare_value = arm.compare_testing(x, x+1)
            if (compare_value == 3):
                break
    
    # Move #4
    for x in range(1):
        arm.update_position(right)
        print(Memory.memory)
        compare_value = arm.compare_testing(x+2, x+3)
        if (compare_value == 3):
            break
        elif (compare_value == 2):
            #Split node
            transition_matrix = arm.get_transition_matrix()
            most_recent_node = len(transition_matrix) - 1
            print(most_recent_node)
            arm.split_node(most_recent_node)
            #Delete connection
            arm.delete_conection_between_nodes(most_recent_node, most_recent_node, 1)

            compare_value = arm.compare_testing(x+1, x+2)
            if (compare_value == 2):
                #Split node
                transition_matrix = arm.get_transition_matrix()
                most_recent_node = len(transition_matrix) - 1
                print(most_recent_node)
                arm.split_node(most_recent_node)
                #Delete connection
                arm.delete_conection_between_nodes(most_recent_node-1, most_recent_node+1, 1)
                arm.delete_conection_between_nodes(most_recent_node, most_recent_node-1, 1)
                arm.delete_conection_between_nodes(most_recent_node, most_recent_node, 1)
                arm.delete_conection_between_nodes(most_recent_node+1, most_recent_node, 1)

                compare_value = arm.compare_testing(x, x+1)
                if (compare_value == 2):
                    #Split node
                    transition_matrix = arm.get_transition_matrix()
                    most_recent_node = len(transition_matrix) - 1
                    print(most_recent_node)
                    arm.split_node(most_recent_node)
                    #Delete connection
                    arm.delete_conection_between_nodes(most_recent_node-1, most_recent_node+1, 1)
                    arm.delete_conection_between_nodes(most_recent_node, most_recent_node-2, 1)
                    arm.delete_conection_between_nodes(most_recent_node, most_recent_node, 1)
                    arm.delete_conection_between_nodes(most_recent_node+1, most_recent_node, 1)


    # Move #5
    for x in range(1):
        arm.update_position(right)
        #print(Memory.memory)


    #Print the transition matrix
    transition_matrix = arm.get_transition_matrix()
    print(transition_matrix)
   
except Exception as e:
    print("Exception encountered: " + str(e))  
