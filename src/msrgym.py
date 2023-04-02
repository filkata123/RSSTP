
from internal import Internal
from external import External
from memory import Memory
from statistics import mode  # for counting charecter reappearence in is_deterministic() method
import matplotlib.pyplot as plt # for draw_graph_from_tm() method
import graphviz
from matplotlib import image as mpimg

class robot_arm:
    
    def __init__(self, joints_n : int, initial_position: list, arm_lengths : list, obstacles : list, arm_steps : int, goal_position: tuple, actions, visualise_ext = False, visualise_int = False):
        """Create a robot arm with charactersitics passed in arguments
        
        Args:
            joints_n (int): number of joints - joints_n > 0
            initial_position (array): array of initial positions of the arms in degress : int 0-359
            arm_lengths (array): aray of ints with size n
            obstacles (list): list of obstacles in the form [[x1,y1], radius_1, ..., [x_n,y_n], radius_n]
            arm_steps (int): how many rotation steps should the hand(s) have
            goal_position (tuple): desired point for the arm to reach in coordinates [x,y]
            actions (list): list of initial possible actions in the form [(0, 1, ... n)]
            visualise_ext (bool - optional): Whether arm movement should be visualized. Default: False
            visualise_int (bool - optional): Whether transition matrix should be visualized. Default: False
        """
        self._ext = External(joints_n, initial_position, arm_lengths, obstacles, arm_steps, goal_position)
        self._int = Internal(actions)

        self.visualise_ext = visualise_ext
        self.visualise_int = visualise_int

    def update_position(self, action : int):
        """ Update position of robot arm through an action from the possible actions set in the constructor

        Args:
            action (int): e.g. 0 = left 1 = right 
        """
        
        if self._int.transition(action) >= 0:
            self._ext.update(action)

            print("______________________________________________________________________________")
            if(self.visualise_ext):                
                self._ext.visualise_arm()
  
            if(self.visualise_int):
                self.draw_graph_from_tm(self.get_transition_matrix())   # Teemu and Rafi
                print("Transition matrix: ") 
                print(self.get_transition_matrix())
            print("Updated position: " + str(self.get_arm_position()))
            print("Internal state after update: " + str(self.get_current_internal_state()))
            print("\n")

            if self.is_desired_position_reached():
                print("Home positon reached")
            
            # -----------Teemu's & Rafi's code: --------------------------------------------------------

            #Initialize Memory() class and update data to memory list
            memory_step = Memory(action, self.get_current_internal_state(), self.is_desired_position_reached())
            Memory.memory.append(memory_step.make_list_from_data())      #updates data_list element data to memory list
            
            self.is_deterministic()     #check and print determinism
            self._ext.distance_from_obstacle()  #check and print distances from obstacles

    
    @staticmethod
    def compare_testing(n, m):
        '''
        Used for testing Memory.compare() method. Makes a dataframe from the memory and calls compare() with parameters.
          Called at the end of demo_msrgym.py.
        '''
        dataframe = Memory.make_dataframe(Memory.memory)   #make (pandas) dataframe from memory
        value = Memory.compare(n, m, dataframe)
        return value

    
    def draw_graph_from_tm(self, tm):
        '''Draws and displays a graph from transition matrix.
            Takes transition matrix (tm) as an argument.
            Logic: 
            Check if the matrix index [i][j] is empty. If the index is empty, that means that
            there is no link from i to j. If the index is not empty, 
            there is a link from i to j -> add edge [i, j] to Graph labeled with the action(s).
        '''
        
        G = graphviz.Digraph('transition_matrix_graph', filename='tm_graph', format="png")
        G.attr(rankdir='LR', size='8,5')

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

        transition_matrix = self._int.get_transition_matrix()

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
    
#----- Teemu's and Rafi's code ends here ---------------------------------------------  

    def get_arm_position(self):
        """ Get current arm positions

        Returns:
            tuple(list<int>, list<(float, float)>): The position of the arm(s) in degrees and coordinates (for end point of arm(s))
        """
        return self._ext.get_position()

    def is_desired_position_reached(self):
        """ Check whether the set desired position has been reached by the hand.

        Returns:
            bool: True if reached
        """
        return self._ext.get_sensory_data()

    def get_current_internal_state(self):
        """ Get the current internal state

        Returns:
            int: Current state
        """
        return self._int.get_current_state()

    def get_transition_matrix(self):
        """ Get current transition matrix

        Returns:
            NDArray: Transition matrix
        """
        return self._int.get_transition_matrix()
        
    # Helper functions
    def split_node(self, n):
        """ Split node n into two nodes, duplicating transitions.

        Args:
            n (int): Node number to split

        Returns:
            NDArray (on success): Resulting matrix after split

            or

            int (on failure): a -1 showing that some matrix validation has failed
        """
        return self._int.split(n)

    def merge_nodes(self, n, m):
        """ Merge nodes 1 and 2 by removing columns and rows n,m and creating one row and column with taking the union of the two nodes

        Args:
            n (int): node 1
            m (int): node 2

        Returns:
            NDArray (on success): Resulting matrix after merge

            or

            int (on failure): a -1 showing that some matrix validation has failed
        """
        return self._int.merge(n, m)

    def add_connection_between_nodes(self, n, m, k):
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
        return self._int.add(n, m, k)

    def delete_conection_between_nodes(self, n, m, k):
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
        return self._int.delete(n,m,k)
    

