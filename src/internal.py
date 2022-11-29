import numpy as np
import random
import copy
class Internal:
    
    #Constructor of Internal class
    def __init__(self, mt, st):
        self.current_state = st
        self.transition_matrix = np.ndarray(shape= (1,1), dtype= object)                            #create initial 1x1 matrix
        self.transition_matrix[0,0] = mt                                                            #fill matrix with list of possible actions
        self.transition_matrix[0,0].sort()                                                          #sort matrix
    
    def split(self,n):
        #this function changes the transition graph G by splitting a node into two nodes. All the incoming and outgoing transitions are dublicated.
        row = copy.deepcopy([self.transition_matrix[n,:]])                                          #extract desired row
        self.transition_matrix = np.vstack((self.transition_matrix,row))                            #add it to the matrix
        col = copy.deepcopy(self.transition_matrix[:,n])                                            #extract desired col
        col = np.expand_dims(col, axis = 1)                                                         #convert it to correct shape
        self.transition_matrix = np.hstack((self.transition_matrix,col))                            #add it to the matrix
        return self.transition_matrix

    def merge(self,n,m):
        #Opposite of split. Remove columns n, m and rows n, m and add instead one row and one column which are obtained by taking unions of elements of original rows/columns.
        row1 = np.array([self.transition_matrix[n,:]])                                              #extract row n
        row2 = np.array([self.transition_matrix[m,:]])                                              #extract row m
        row1 += row2                                                                                #merge rows                    
        for i in range(len(row1[0])):
            row1[0,i]= list(set(row1[0,i]))                                                         #remove duplicates
        self.transition_matrix[n,:] = row1                                                          #update row n
        self.transition_matrix = np.delete(self.transition_matrix,m, axis=0)                        #delete row m
        col1 = np.array(self.transition_matrix[:,n])                                                #extract column n
        col2 = np.array(self.transition_matrix[:,m])                                                #extract column m
        col1 += col2                                                                                #merge columns 
        for i in range(len(col1[:])):
            col1[i]= list(set(col1[i]))                                                             #remove duplicates
        self.transition_matrix[:,n] = col1                                                          #update column n
        self.transition_matrix = np.delete(self.transition_matrix,m, axis=1)                        #remove column m                                                     
        return self.transition_matrix

    def add(self,n,m,k):
        #add a connection from n to m with label k, meaning that anm := anm ∪ {k}.
        if k not in self.transition_matrix[n,m]:                                                    #check if connection already exists
            self.transition_matrix[n,m].append(k)                                                   #if not add k to Amn
            self.transition_matrix[n,m].sort()                                                      #sort elements in Amn
            return self.transition_matrix
        else:
            print("this connection already exists")                                                 #if yes print this message
            return -1

    def delete(self,n,m,k):
        #remove the connection from n to m, if it has label k, meaning that anm := anm \ {k}.
        if k in self.transition_matrix[n,m]:                                                        #check if connection exists
            self.transition_matrix[n,m].remove(k)                                                   #if yes remove k from Amn if found
            return self.transition_matrix
        else:
            print("Specified path does not exist")                                                  #if not  k is not in Amn print message 
            return -1

    def transition(self,k):
        #This is a non-deterministic transition.
        possible_transitions = list()                                                               #initiate a list of possible next states
        for i in range (np.shape(self.transition_matrix)[0]):                                       #iterate through all tuples in current row   
            if k in self.transition_matrix[self.current_state,i]:                                   # if k is a tuple add its column to possible transitions
                possible_transitions.append(i)
        try:
            self.current_state = random.choice(possible_transitions)                                #update current state to one of the possible transitions
            return self.current_state
        except:
            print("This transition is not possible")                                                #if k is not found in any tuple print this message
            return -1

    def get_current_state(self):
        return self.current_state