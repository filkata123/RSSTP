import numpy as np
import random
class Internal:
    
    #Constructor of Internal class
    def __init__(self, mt, st):
        self.transition_matrix = mt
        self.current_state = st
        for n in range(np.shape(self.transition_matrix)[0]):
            for m in range(np.shape(self.transition_matrix)[1]):
                self.transition_matrix[n,m] = tuple(set(self.transition_matrix[n,m]))

    
    def split(self,n):
        #this function changes the transition graph G by splitting a node into two nodes. All the incoming and outgoing transitions are dublicated.
        row = self.transition_matrix[n,:].reshape(1,np.shape(self.transition_matrix)[1])             #extract desired row
        self.transition_matrix = np.vstack((self.transition_matrix,row))                             #add it to the matrix
        col = self.transition_matrix[:,n].reshape(np.shape(self.transition_matrix)[0],1)             #extract desired col
        self.transition_matrix = np.hstack((self.transition_matrix,col))                             #add it to the matrix
        return self.transition_matrix

    def merge(self,n,m):
        #Opposite of split. Remove columns n, m and rows n, m and add instead one row and one column which are obtained by taking unions of elements of original rows/columns.
        row1 = self.transition_matrix[n,:].reshape(1,np.shape(self.transition_matrix)[1])           #extract row n
        row2 = self.transition_matrix[m,:].reshape(1,np.shape(self.transition_matrix)[1])           #extract row m
        row1 += row2                                                                                #merge rows
        for i in range(np.shape(self.transition_matrix)[1]):
            row1[0,i]= tuple(set(row1[0,i]))                                                        #remove duplicates
        self.transition_matrix[n,:] = row1.ravel()                                                  #update row n
        self.transition_matrix = np.delete(self.transition_matrix,m, axis=0)                        #delete row m
        col1 = self.transition_matrix[:,n].reshape(np.shape(self.transition_matrix)[0],1)           #extract column n
        col2 = self.transition_matrix[:,m].reshape(np.shape(self.transition_matrix)[0],1)           #extract column m
        col1 += col2                                                                                #merge columns
        for i in range(np.shape(self.transition_matrix)[0]):
            col1[i,0]= tuple(set(col1[i,0]))                                                        #remove duplicates
        self.transition_matrix[:,n] = col1.ravel()                                                  #update column n
        self.transition_matrix = np.delete(self.transition_matrix,m, axis=1)                        #remove column m                                                     
        return self.transition_matrix

    def add(self,n,m,k):
        #add a connection from n to m with label k, meaning that anm := anm ∪ {k}.
        self.transition_matrix[n,m] += (k,)                                                         #add k to Amn
        self.transition_matrix[n,m] = tuple(set(self.transition_matrix[n,m]))                       #sort elements in Amn
        return self.transition_matrix

    def delete(self,n,m,k):
        #remove the connection from n to m, if it has label k, meaning that anm := anm \ {k}.
        temp = list(self.transition_matrix[n,m])                                                    #extract Amn as a list
        try:
            temp.remove(k)                                                                          #remove k from Amn if found
        except ValueError:
            print("Specified path does not exist")                                                  #if not  k is not in Amn print message 
        self.transition_matrix[n,m] = tuple(temp)                                                   #update Amn in transition matrix
        return self.transition_matrix
    
    def transition(self,k):
        #This is a non-deterministic transition.
        possible_transitions= list()                                                                #initiate a list of possible next states
        for i in range (np.shape(self.transition_matrix)[0]):                                       #iterate through all tuples in current row   
            if k in self.transition_matrix[self.current_state,i]:                                   # if k is a tuple add its column to possible transitions
                possible_transitions.append(i)
        try:
            self.current_state = random.choice(possible_transitions)                                #update current state to one of the possible transitions
        except:
            print("This transition is not possible")                                                #if k is not found in any tuple print this message
        return self.current_state
