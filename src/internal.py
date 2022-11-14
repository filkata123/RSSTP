import numpy as np
class Internal:
    
    #Constructor of Internal class
    def __init__(self, mt, st):
        self.transition_matrix = mt
        self.current_state = st
    
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

    #TODO implement functions (remaining: add, delete, transition)
    def add(self,n,m,k):
        #add a connection from n to m with label k, meaning that anm := anm ∪ {k}.
        A = np.array([[['A11','B11','C11','D11'],['A12','B12','C12','D12']],[['A21','B21','C21','D21'],['A22','B22','C22','D22']]])
        return A
    def delete(self,n,m,k):
        #remove the connection from n to m, if it has label k, meaning that anm := anm \ {k}.
        A = np.array([[['A11','B11','C11','D11'],['A12','B12','C12','D12']],[['A21','B21','C21','D21'],['A22','B22','C22','D22']]])
        return A
    def transition(self,k):
        #This is a non-deterministic transition.
        A = np.array([[['A11','B11','C11','D11'],['A12','B12','C12','D12']],[['A21','B21','C21','D21'],['A22','B22','C22','D22']]])
        return A
        