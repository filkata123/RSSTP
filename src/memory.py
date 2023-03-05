#import numpy as np
#import random
#import copy

class Memory():
    # default attribute here (class object attrubute)
    # pi = 3.14
    steps_taken = 0
    #memory = []

    def __init__(self, prevaction, intstate, sensation):
        # attribute initialize
        Memory.steps_taken =+ 1
        self.steps = Memory.steps_taken
        self.prevaction = prevaction
        self.intstate = intstate
        self.sensation = sensation

    def make_list_from_data(self): #method
        data_list = []
        data_list.append(self.steps)
        data_list.append(self.prevaction)
        data_list.append(self.intstate)
        data_list.append(self.sensation)
        #print(data_list)
        return data_list
    
        #update_memory(self):
        '''
        Called after every move. Adds memorystep to the memory list.
        '''
        print("update_memory kutsuttu")
        memorystep = Memory(prevaction=1, intstate=0, sensation=0)
        Memory.memory.append(memorystep)


#make instance

#call method from class
#memorystep.make_list_from_data()
memory = []
memorystep = Memory(prevaction=1, intstate=0, sensation=0)
memory.append(memorystep)
print(memory[0].make_list_from_data())
#print(memory)