import numpy as np
class Internal:
    
    #Constructor of Internal class
    def _init_(self, mt, st):
        self.transition_matrix = mt
        self.current_state = st

    #TODO implement functions 
    def split(self,n):
        #this function changes the transition graph G by splitting a node into two nodes. All the incoming and outgoing transitions are dublicated.
        A = np.array([[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]])
        return A
    def merge(self,n,m):
        #Opposite of split. Remove columns n, m and rows n, m and add instead one row and one column which are obtained by taking unions of elements of original rows/columns.
        A = np.array([[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]])
        return A
    def add(self,n,m,k):
        #add a connection from n to m with label k, meaning that anm := anm ∪ {k}.
        A = np.array([[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]])
        return A
    def delete(self,n,m,k):
        #remove the connection from n to m, if it has label k, meaning that anm := anm \ {k}.
        A = np.array([[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]])
        return A
    def transition(self,k):
        #This is a non-deterministic transition.
        A = np.array([[['A','B','C','D'],['A','B','C','D']],[['A','B','C','D'],['A','B','C','D']]])
        return A
        