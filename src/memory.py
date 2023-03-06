#import numpy as np
#import random
#import copy

class Memory():
    # default attribute here (class object attrubute)
    # pi = 3.14
    steps_taken =+ 2
    memory = []

    def __init__(self, previous_action, internal_state, sensation):
        # attribute initialize
        #Memory.steps_taken =+ 2
        #self.steps = Memory.steps_taken
        self.previous_action = previous_action
        self.internal_state = internal_state
        self.sensation = sensation

    def make_list_from_data(self): #method
        data_list = []
        #data_list.append(self.steps)
        data_list.append(self.previous_action)
        data_list.append(self.internal_state)
        data_list.append(self.sensation)
        #print(data_list)
        return data_list
    
    def print_memory(self):
        for element in enumerate(Memory.memory):
            print(element)

    


#make instance

