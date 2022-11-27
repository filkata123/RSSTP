from internal import Internal
from external import External

class robot_arm:
    
    def __init__(self, joints_n : int, arm_lengths : float, obstacles : list, initial_position: int, goal_position: tuple, actions):
        """
        -joints_n = number of joints : int : > 0
        -arm_lengths = arm lenghts : float (TODO: List<float> with size n)
        -obstacles = list of obstacles in the form [[x1,y1], radius_1, ..., [x_n,y_n], radius_n]
        -initial_position = initial position of arm in degress : int 0-359 (TODO: List<int> with size n)
        -goal_position = desired point for the arm to reach in coordinates [x,y] (TODO: in degrees?)
        -actions = list of initial possible actions in the form [(0, 1, ... n)]
        """

        self.ext = External(joints_n, initial_position, arm_lengths, obstacles, goal_position)
        self.int = Internal(actions, 0)

    def update_position(self, action : int):
        """
        action = e.g. 0 = left 1 =r ight 
        """
        if self.int.transition(action) >= 0:
            self.ext.update(action)

            print("Updated position: " + str(self.get_arm_position())) 

            if self.is_desired_position_reached():
                print("Home positon reached")

    def get_arm_position(self):
        return self.ext.get_position()

    def is_desired_position_reached(self):
        return self.ext.get_sensory_data()

    # Helper functions
    def split_node(self, n):
        print(self.int.split(n))

    def merge_nodes(self, n, m):
        print(self.int.merge(n, m))

    def add_connection_between_nodes(self, n, m, k):
        print(self.int.add(n, m, k))

    def delete_conection_between_nodes(self, n, m, k):
        print(self.int.delete(n,m,k))


