import numpy as np
import random
import copy

import matplotlib.pyplot as plt # for draw_graph_from_tm() method
import graphviz
from matplotlib import image as mpimg
from statistics import mode  # for counting charecter reappearence in is_deterministic() method

class Internal:
    def __init__(self, actions):
        """ Internal constructor

        Args:
            actions (list): list of initial possible actions e.g. list([0,1,2,3,4])
        """
        self.set_transition_matrix(actions)
        self.set_current_state(0)

    def get_transition_matrix(self):
        """ Transition matrix getter

        Returns:
            NDArray : Transition matrix
        """
        return self.__transition_matrix

    def set_transition_matrix(self, new_matrix):
        """ Transition matrix setter

        Args:
            new_matrix (list):  list of actions e.g. list([0,1,2,3,4]) or an ND matrix

        Returns:
            int: -1 if setter fails due to failed validation
        """

        #TODO check shape of matrix
        if isinstance(new_matrix, list):
            self.__transition_matrix = np.ndarray(shape= (1,1), dtype= object)                      #create initial 1x1 matrix
            self.__transition_matrix[0,0] = new_matrix                                              #fill matrix with list of possible actions
            self.__transition_matrix[0,0].sort()                                                    #sort matrix
        elif isinstance(new_matrix, np.ndarray):
            if len(np.shape(new_matrix)) <= 1:
                return -1
            if isinstance(new_matrix[0,0],np.ndarray):
                self.__transition_matrix = np.ndarray(shape= (np.shape(new_matrix)[0],np.shape(new_matrix)[1]), dtype= object)
                for i in range(np.shape(new_matrix)[0]):
                    for j in range(np.shape(new_matrix)[1]):
                        self.__transition_matrix[i,j] = new_matrix[i,j].tolist()
                        self.__transition_matrix[i,j].sort()
            elif isinstance(new_matrix[0,0], list):
                self.__transition_matrix = new_matrix
            else:
                return -1
        else:
            print("invalid input, use a list or square numpy array with more than one element")
            return -1

    def get_current_state(self):
        """ Current state getter

        Returns:
            int: Current state
        """
        return self.__current_state

    def set_current_state(self, new_state):
        """Current state setter

        Args:
            new_state (int): A state from all possible states in matrix

        Returns:
            int: -1 if setter fails due to failed validation 
        """
        if not (isinstance(new_state, int)):
            return -1
        if new_state < np.shape(self.__transition_matrix)[0] and new_state >= 0:
            self.__current_state = new_state
        else:
            return -1
    
    def split(self,n):
        """ Split node n into two nodes, duplicating transitions.

        Args:
            n (int): Node number to split

        Returns:
            NDArray (on success): Resulting matrix after split

            or

            int (on failure): a -1 showing that some matrix validation has failed
        """
        if(self.__transition_matrix_validation() == -1):                                               #validating transition matrix
            return -1
        
        row_length = len(self.__transition_matrix)
        col_length = len(self.__transition_matrix[0])
        
        if (n >= row_length) | (n >= col_length):                                                  #checking is argument n is less then the N or M of transition matix       
            return -1
        
        #this function changes the transition graph G by splitting a node into two nodes. All the incoming and outgoing transitions are dublicated.
        row = copy.deepcopy([self.__transition_matrix[n,:]])                                        #extract desired row
        self.__transition_matrix = np.vstack((self.__transition_matrix,row))                        #add it to the matrix
        col = copy.deepcopy(self.__transition_matrix[:,n])                                          #extract desired col
        col = np.expand_dims(col, axis = 1)                                                         #convert it to correct shape
        self.__transition_matrix = np.hstack((self.__transition_matrix,col))                        #add it to the matrix
        return self.__transition_matrix

    def merge(self,n,m):
        """ Merge nodes 1 and 2 by removing columns and rows n,m and creating one row and column with taking the union of the two nodes

        Args:
            n (int): node 1
            m (int): node 2

        Returns:
            NDArray (on success): Resulting matrix after merge

            or

            int (on failure): a -1 showing that some matrix validation has failed
        """
        if(self.__transition_matrix_validation() == -1):                                              #checking is argument n and m is less then the N & M of transition matix
            return -1
        
        row_length = len(self.__transition_matrix)
        col_length = len(self.__transition_matrix[0])
 
        if (n >= row_length) | (n >= col_length) | (m >= row_length)| (m >= col_length):            #checking the argurment n and m is less then the N x M of transition matix
            return -1
        
        if (n == m):                                                                                #checking if n and m are same (invalid arguments)
            return -1

        #Opposite of split. Remove columns n, m and rows n, m and add instead one row and one column which are obtained by taking unions of elements of original rows/columns.
        row1 = np.array([self.__transition_matrix[n,:]])                                            #extract row n
        row2 = np.array([self.__transition_matrix[m,:]])                                            #extract row m
        row1 += row2                                                                                #merge rows                    
        for i in range(len(row1[0])):
            row1[0,i]= list(set(row1[0,i]))                                                         #remove duplicates
        self.__transition_matrix[n,:] = row1                                                        #update row n
        self.__transition_matrix = np.delete(self.__transition_matrix,m, axis=0)                    #delete row m
        col1 = np.array(self.__transition_matrix[:,n])                                              #extract column n
        col2 = np.array(self.__transition_matrix[:,m])                                              #extract column m
        col1 += col2                                                                                #merge columns 
        for i in range(len(col1[:])):
            col1[i]= list(set(col1[i]))                                                             #remove duplicates
        self.__transition_matrix[:,n] = col1                                                        #update column n
        self.__transition_matrix = np.delete(self.__transition_matrix,m, axis=1)                    #remove column m                                                     
        return self.__transition_matrix

    def add(self,n,m,k):
        """Create a connection between node 1 and 2 through action k.

        Args:
            n (int): node 1
            m (int): node 2
            k (int): action

        Returns:
            NDArray (on success): Resulting matrix after add

            or

            int (on failure): a -1 showing that some matrix validation has failed
        """
        if(self.__transition_matrix_validation() == -1):                                               #validating transition matrix
            return -1

        row_length = len(self.__transition_matrix)
        col_length = len(self.__transition_matrix[0])
 
        if (n >= row_length) | (m >= col_length):                                                  #checking the argument n and m is less then the N x M of transition matix
            return -1
        
        #add a connection from n to m with label k, meaning that anm := anm ∪ {k}.
        if k not in self.__transition_matrix[n,m]:                                                  #check if connection already exists
            self.__transition_matrix[n,m].append(k)                                                 #if not add k to Amn
            self.__transition_matrix[n,m].sort()                                                    #sort elements in Amn
            return self.__transition_matrix
        else:
            print("this connection already exists")                                                 #if yes print this message
            return -1

    def delete(self,n,m,k):
        """Delete a connection between node 1 and 2 of action k.

        Args:
            n (int): node 1
            m (int): node 2
            k (int): action

        Returns:
            NDArray (on success): Resulting matrix after deletion

            or
            
            int (on failure): a -1 showing that some matrix validation has failed
        """
        if(self.__transition_matrix_validation() == -1):                                               #validating transition matrix
            return -1
       
        row_length = len(self.__transition_matrix)
        col_length = len(self.__transition_matrix[0])

        if (n >= row_length) | (m >= col_length):                                                   #checking is argument n and m is less then the N & M of transition matix
            return -1

        #remove the connection from n to m, if it has label k, meaning that anm := anm \ {k}.
        if k in self.__transition_matrix[n,m]:                                                      #check if connection exists
            self.__transition_matrix[n,m].remove(k)                                                 #if yes remove k from Amn if found
            return self.__transition_matrix
        else:
            print("Specified path does not exist")                                                  #if not  k is not in Amn print message 
            return -1
    

    def transition(self,k):
        """ Transition between states through action k

        Args:
            k (int): Action

        Returns:
            int: New state after action or -1 on failed validation
        """
        if(self.__transition_matrix_validation() == -1):                                               #validating transition matrix
            return -1
        
        #This is a non-deterministic transition.
        possible_transitions = list()                                                               #initiate a list of possible next states
        for i in range (np.shape(self.__transition_matrix)[0]):                                     #iterate through all tuples in current row   
            if k in self.__transition_matrix[self.__current_state,i]:                               #if k is a tuple add its column to possible transitions
                possible_transitions.append(i)
        try:
            self.__current_state = random.choice(possible_transitions)                              #update current state to one of the possible transitions
            return self.__current_state
        except:
            print("This transition is not possible")                                                #if k is not found in any tuple print this message
            return -1

    def __transition_matrix_validation(self):
        """ Validate transition matrix

        Returns:
            int: 1 on success; -1 on failed validation
        """
        row_length = len(self.__transition_matrix)                                                  #extracting rows of transition matrix
        col_length = len(self.__transition_matrix[0])                                               #extracting rows of transition matrix

        if (row_length == 0) | (col_length == 0):                                                   #checking if transition matrix is empty
            return -1
        
        if row_length != col_length:                                                                #checking square matrix
            return -1
        
        for row_index in range(row_length):                                                         #checking size of rows inside each intermediate column wrt row or column
            intermediate_col_length = len(self.__transition_matrix[row_index])
            if row_length != intermediate_col_length:
                return -1
        return 1

    #TODO: Get list of all states


# Teemu's and Rafi's code: -------------

    def draw_graph_from_tm(self, tm):
        '''Draws and displays a graph from transition matrix.
            Takes transition matrix (tm) as an argument.
            Logic: 
            Check if the matrix index [i][j] is empty. If the index is empty, that means that
            there is no link from i to j. If the index is not empty, 
            there is a link from i to j -> add edge [i, j] to Graph labeled with the action(s).
        '''
        
        G = graphviz.Digraph('transition_matrix_graph', filename='tm_graph', format="png")
        G.attr(rankdir='LR', size='20')

        for i in range(len(tm)):     #for every row
            for j in range(len(tm[i])):     #for every column
                if tm[i][j]:     #if index is not empty
                    G.edge(str(i), str(j), label=str(tm[i][j])) #add edge: index (i, j) with label=actions 

        G.render()  #this makes the png file
        image = mpimg.imread("tm_graph.png")
        plt.imshow(image)
        plt.show()
        plt.figure(2)
        plt.clf()

    def is_deterministic(self):
        '''
        Checks if the matrix is deterministic and prints the result.
        Returns:
            True: if matrix is not deterministic
            False: if matrix is not deterministic
        '''
        # test_matrix = [[[0,1],[2]],
        #                [[0],[4,3], [2,1]],
        #                [[7],[0,7], [2,1]],
        #                [[0,0],[1,0]]]

        transition_matrix = self.get_transition_matrix()

        # for i in test_matrix:
        for i in transition_matrix:
            action_by_matrix_row =[] #this list keeps track of actions in a matrix row
            for j in i:
                for k in j:
                    action_by_matrix_row.append(k)  #add actions to the list

            # counts how many times the most common action has appeared in the matrix row
            identical_action_counter = action_by_matrix_row.count(mode(action_by_matrix_row)) 

            if identical_action_counter >= 2:   #if an action appears more than one time per row, that means that the matrix is not deterministic
                print("Transition matrix is not deterministic")
                return False
        print("Transition matrix is deterministic")
        return True