class Internal:
    
    #Constructor of Internal class
    def_init_(self, mt, st):
        self.transition_matrix = mt
        self.current_state = st

    def split(n):
        #this function changes the transition graph G by splitting a node into two nodes. All the incoming and outgoing transitions are dublicated.

    def merge(n,m):
        #Opposite of split. Remove columns n, m and rows n, m and add instead one row and one column which are obtained by taking unions of elements of original rows/columns.

    def add(n,m,k):
        #add a connection from n to m with label k, meaning that anm := anm ∪ {k}.

    def delete(n,m,k):
        #remove the connection from n to m, if it has label k, meaning that anm := anm \ {k}.

    def transition(k):
        #This is a non-deterministic transition.
        
    