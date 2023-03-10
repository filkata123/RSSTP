import pandas as pd

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

    def make_dataframe(self, data):
        dataframe = pd.DataFrame(data, columns=['Previous action', 'Internal state', 'Sensation'])
        print(dataframe)
        return dataframe
        #print(dataframe.loc[1: ,'Sensation'])
        #print(len(dataframe.index))




    def compare(self, n, m, dataframe):
        if n > m:
            sub_memory_length = len(dataframe.index) - n
        elif m > n:
            sub_memory_length = len(dataframe.index) - m
        else:
            print("Can not compare the element to itself")
            return
        
        print(n, m, sub_memory_length)
        sub_list_1 = dataframe.loc[n:sub_memory_length-1]
        sub_list_2 = dataframe.loc[m:sub_memory_length-1]

        print(sub_list_1)
        print(sub_list_2)
        


        pass
        


