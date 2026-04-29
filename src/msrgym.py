
from internal import Internal
from external import External
from memory import Memory

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
        self._mem = Memory()

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
            print(f"Sensory feedback float: {self._ext.get_sensory_data_float()}")  # Teemu and Rafi
            if self.is_desired_position_reached():
                print("Home positon reached")
            
            # -----------Teemu's & Rafi's code: --------------------------------------------------------

            #Initialize Memory() class and update data to memory list
            self._mem.update_memory(action, self.get_current_internal_state(), self.is_desired_position_reached())
            #memory_step = Memory(action, self.get_current_internal_state(), self.is_desired_position_reached())
            #Memory.memory.append(memory_step.make_list_from_data())      #updates data_list element data to memory list
            self.is_deterministic()     #check and print determinism
            self._ext.distance_from_obstacle()  #check and print distances from obstacles

    def compare_memory(self, n, m):
        '''
        Helper function for compare() function of Memory class

        Args:
            n (int) : index n where a submemory would be created
            m (int) : index m where a submemory would be created
        Returns:
            int : return code
        '''
        return self._mem.compare(n, m)

    def draw_graph_from_tm(self, tm):
        '''Draws and displays a graph from transition matrix.
        
        Args:
            tm: transition matrix
        '''
        self._int.draw_graph_from_tm(tm)

    def is_deterministic(self):
        '''
        Checks if the matrix is deterministic and prints the result.
        Returns:
            Bool: True if matrix is not deterministic, False otherwise
        '''
        return self._int.is_deterministic()
    
    def get_sensory_data_float(self):
        '''
        Get sensory feedback as a float between 0-1. Calculate the distance between the joint and its home position and
        scale the distance between 0-1. Returns the average result of every joint.

        Returns:
            float:
            1 = joint is at its home position;
            0 = joint is as far away from its home position as possible
        
        '''
        return self._ext.get_sensory_data_float()

#----- Teemu's and Rafi's code ends here ---------------------------------------------  

    def get_memory_size(self):
        '''
        Return length of memory list.
        Retruns:
            int : length of memory
        '''
        return self._mem.get_memory_size()

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
    

