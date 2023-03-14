import pandas as pd
import numpy as np

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

    @staticmethod
    def make_dataframe(data):
        dataframe = pd.DataFrame(data, columns=['Previous action', 'Internal state', 'Sensation'])
        print(dataframe)
        return dataframe
        #print(dataframe.loc[1: ,'Sensation'])
        #print(len(dataframe.index))



    @staticmethod
    def compare(n, m, dataframe):
        '''
        Makes two sub memories from memory (dataframe) at indexes n and m. Compares the sub memories to each other.
        Prints 'Is different' if previous actions were the same but internal states or sensations are different.
        Otherwise prints 'Unknown'.
        '''

        #set sub_memory_length
        if n > m:
            sub_memory_length = len(dataframe) - n
        elif m > n:
            sub_memory_length = len(dataframe) - m
        else:
            print("Can not compare the element to itself")
            return
        
        print(n, m, sub_memory_length)
    

        #make sub memory dataframes
        sub_memory_1 = dataframe.loc[n:n+sub_memory_length-1].reset_index(drop=True)
        sub_memory_2 = dataframe.loc[m:m+sub_memory_length-1].reset_index(drop=True)

        #print(sub_memory_1)
        #print(sub_memory_2)
        if not (sub_memory_1.equals(sub_memory_2)): #if sub memories are not identical

            #make a comparison dataframe of the sub memories
            comparison = sub_memory_1.compare(sub_memory_2, keep_shape=True)
            print(comparison)

            #Go through the comparison dataframe to find not 'NaN' value
            for i in range(0, len(comparison), 1):
                for j in range(0, 5, 2):
                    if pd.notnull(comparison.iloc[i, j]):
                        print("Found a difference in index: {},{}".format(i,j))
                        if j==0:
                            print("Unknown: Previous action was different")
                            return
                        else: 
                            print("Is different: Internal state or Sensation is different")
                            return
        print("Unknown: Sub memories are identical")
        return

        


