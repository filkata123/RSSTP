
"""Make a Memory() class for saving data"""
class Memory():
    # default attribute here (class object attrubute)
    memory = []

    def __init__(self, previous_action, internal_state, sensation):
        # attribute initialize
        self.previous_action = previous_action
        self.internal_state = internal_state
        self.sensation = sensation

    def make_list_from_data(self): #method
        data_list = []
        data_list.append(self.previous_action)
        data_list.append(self.internal_state)
        data_list.append(self.sensation)
        return data_list
    
    def print_memory(self):
        # Prints all elements of the memory by numbered 
        for element in enumerate(Memory.memory):
            print(element)

    


#make instance

