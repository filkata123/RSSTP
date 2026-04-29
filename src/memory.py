import pandas as pd

"""Make a Memory() class for saving data"""
class Memory():
    # default attribute here (class object attrubute)

    def __init__(self, ):
        ''' Initializes an instance of Memory class.
        '''
        self.memory = [] # This list works as the robotic arm's memory.

    def update_memory(self, previous_action, internal_state, sensation):
        ''' Add new data to memory.
        Args:
            previous_action : previous action
            internal_state : internal state
            sensation : sensation
        '''
        self.memory.append([previous_action, internal_state, sensation])

    def get_memory_size(self):
        '''
        Return length of memory list.
        Retruns:
            int : length of memory
        '''
        return len(self.memory)
    
    def print_memory(self):
        '''
          Prints all elements of the memory by number 
        '''      
        for element in enumerate(self.memory):
            print(element)

    def compare(self, n, m):
        '''
        Makes two sub memories from memory (dataframe) at indexes n and m. Compares the sub memories to each other.
        Prints 'Is different' if previous actions were the same but internal states or sensations are different.
        Otherwise prints 'Unknown'.
        Returns -1 if invalid argument
                0 if "Unknown: Previous action was different"
                1 if "Is different: Internal state is different"
                2 if "Is different: Sensation is different"
                3 if "Unknown: Sub memories are identical"

        Args:
            n (int) : index n where a submemory would be created
            m (int) : index m where a submemory would be created
        
        Returns:
            int : return code
        '''
        dataframe = pd.DataFrame(self.memory, columns=['Previous action', 'Internal state', 'Sensation'])

        if ((n > (len(dataframe)-1)) or (n < 0)) or ((m > (len(dataframe)-1)) or (m < 0)):
            print("Invalid arguments n, m must be higher than 0 and lower than memory length.") 
            return -1
                
        #set sub_memory_length
        if n > m:
            sub_memory_length = len(dataframe) - n
        elif m > n:
            sub_memory_length = len(dataframe) - m
        else:
            print("Invalid arguments n, m. n and m must be not equal integers between 0 and (dataframe length-1).")
            return -1
        
        print("Compare called with arguments; n = {}, m = {}".format(n, m))
    

        #make sub memory dataframes
        sub_memory_1 = dataframe.loc[n:n+sub_memory_length-1].reset_index(drop=True)
        sub_memory_2 = dataframe.loc[m:m+sub_memory_length-1].reset_index(drop=True)

        #print(sub_memory_1)
        #print(sub_memory_2)
        if not (sub_memory_1.equals(sub_memory_2)): #if sub memories are not identical
            #make a comparison dataframe of the sub memories
            comparison = sub_memory_1.compare(sub_memory_2, keep_shape=True)
            #print(comparison)

            #Go through the comparison dataframe to find not 'NaN' value
            # TODO: This implementation only tells us the first different value, rather than all. Could lead to confusion.
            for i in range(0, len(comparison), 1):
                for j in range(0, 5, 2):
                    if pd.notnull(comparison.iloc[i, j]):
                        #print("Found a difference in index: {},{}".format(i,j))
                        if j==0:
                            print("Unknown: Previous action was different")
                            return 0
                        if j==2:
                            print("Is different: Internal state is different")
                            return 1
                        else: 
                            print("Is different: Sensation is different")
                            return 2
        else:
            print("Unknown: Sub memories are identical")       
            return 3


