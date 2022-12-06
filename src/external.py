import math
from shapely.geometry import LineString, Point

import matplotlib.pyplot as plt
import numpy as np

class External:
    def __init__(self, n, p, l, o, d, feedback):
        """ Constructor of External

        Args:
            n (int > 0): number of joints
            p (array<int>): arm lenghts with size n
            l (array<int>): initial position of arm
            o (array<...>): list of obstacles with form [[x,y], size, ... [x_n,y_n], size_n]
            d (int): arm step - rotate by how many angles
            feedback (list<tuple<floats>>): points, which will create sensory feedback when reached

        Raises:
            Exception: Initial position intersects with obstacles
        """

        self.n = n
        self.l = l
        self.o = o
        self.p = p
        self.d = d
        self.feedback = feedback
        collision, *_ = self.__hit_obstacle(self.p)
        if collision:
            raise Exception("Initial position must not intersect with obstacles")

    # Private methods
    
    def _calculate_coordinates(self, position):
        """ Calculate coordinates of join based on position of arm

        Args:
            position (int): Position in degrees

        Returns:
            list<float>: list of arm coordinates
        """
        lengths=[]
        coordinates=[]
        for i in range(self.n):
            lengths.append(self.l[i])
        
        p=0
        x=0
        y=0

        for i in range(self.n):
            p = p + position[i]

            temp_x = round(lengths[i]*math.cos(math.radians(p)),2)
            temp_y = round(lengths[i]*math.sin(math.radians(p)),2)
            x = round((x + temp_x),2)
            y = round((y + temp_y),2)
            coordinates.append((x,y))

        return coordinates # this will always return x,y for joint i
    

    def __hit_obstacle(self, position):
        """ Check whether any collision will ocur at given position
        Args:
            position (int): Position to be checked

        Returns:
            bool: Has collision ocurred?
            bool: Has the arm collided with an obstacle?
            int: Arm n which has collided
            int: Object/Arm n with which the checked arm has collided
        """
        collision = False
        obstacle_collision = False
        collided_arm = 0
        collided_object = 0

        arms = []
        center = []
        circle = []

        # range determiners
        n_obstacles = int(len(self.o)/2)
        n_arms = self.n

        # create obstacles
        if len(self.o) == 0:
            print ("No obstacles in environment")
            return collision, obstacle_collision, collided_arm, collided_object 
        else: 
            for i in range(0,len(self.o),2):
                center.append(Point(self.o[i][0],self.o[i][1]))
                circle.append(center[int(i/2)].buffer(self.o[i+1]).boundary)
        
        coordinates = self._calculate_coordinates(position) 
        for i in range(n_arms):
            # constructing of 1 arm with 1 node at origin with length l
            
            if i == 0:
                arms.append(LineString([(0,0), (coordinates[i][0], coordinates[i][1])]))
            else:
                arms.append(LineString([(coordinates[i-1][0], coordinates[i-1][1]), (coordinates[i][0], coordinates[i][1])]))

        if (i > 0):
            # checking collision between arms
            for i in range(n_arms):

                # make sure adjacent arms cant be on top of eahcother
                if (position[i] <= 181 and position[i] >= 179):
                    collision = True
                    obstacle_collision = False
                    collided_arm = i - 1
                    collided_object = i
                    return collision, obstacle_collision, collided_arm, collided_object 

                # check intersection between arms
                for j in range(i, n_arms):  
                    if (n_arms - j > 2):
                        if(arms[i].intersects(arms[j + 2])):
                            collision = True
                            obstacle_collision = False
                            collided_arm = i
                            collided_object = j + 2
                            return collision, obstacle_collision, collided_arm, collided_object


        # checking collision between arms and obstacles
        for i in range(n_obstacles):           
            for j in range(n_arms):
                if  (circle[i].intersects(arms[j])):
                    collision = True
                    obstacle_collision = True
                    collided_arm = j
                    collided_object = i
                    return collision, obstacle_collision, collided_arm, collided_object
        
        # return no collision
        return collision, obstacle_collision, collided_arm, collided_object

    # Public methods
    def get_sensory_data(self):
        """ get sensory data by checking if all joints are in their home positions

        Returns:
            bool : True if all joints are in home positions 
        """

        joints_in_home_position = 0
        coordinates = self._calculate_coordinates(self.p)
        for i  in range(self.n):
            if coordinates[i] == self.feedback[i]:      
                joints_in_home_position = joints_in_home_position + 1
        
        #TODO change to float in future implementations
        if joints_in_home_position == self.n:
            return True
        else:
            return False

    def get_position(self):
        """ Get p and also the actual geometry of the arm, i.e. the coordinates of the joints. 

        Returns:
            list: Coordinates of all joints
        """
        coordinates = []
        
        coordinates = self._calculate_coordinates(self.p)   
        self.plot(coordinates)
        return self.p, coordinates


    def update(self, a):
        """ Use action a to move respective joint. If a = 2k for some k,
        then the k:th joint moves counterclockwise, 
        and if a = 2k + 1 for some k, then the k:th joint moves clockwise.

        Args:
            a (int): Action a; 0 ≤ a < 2n
        """
        new_position=[]
        for i in range(self.n):
            new_position.append(self.p[i])

        #move clockwise
        if a % 2 == 0: 
            k = int(a/2) 
            while (new_position[k] + self.d < 0):
                new_position[k] = new_position[k] + 360
            new_position[k] = (new_position[k] + self.d) % 360
        #move counterclockwise
        else: 
            k = int((a-1)/2)
            while (new_position[k] - self.d < 0):
                new_position[k] = new_position[k] + 360
            new_position[k] = (new_position[k] - self.d) % 360
        
        coordinates_after_move = self._calculate_coordinates(new_position)
        collision, obstacle_collision, collided_arm, collided_object  = self.__hit_obstacle(new_position)

        if not collision:
            # move joint to new position
            self.p[k] = new_position[k] 
        elif obstacle_collision:
            print('Position of joint ' + str(collided_arm) +' (' + str(coordinates_after_move[k]) + ') is unreachable due to object ' + str(collided_object)+'! \n')
        else:
            print('arm ' + str(collided_arm) + ' intersects with arm ' + str(collided_object) + '! \n')

    def plot(self, coordinates):

        x_coordinates=[0]
        y_coordinates=[0]

        for coordinate in coordinates:
            x_coordinates.append(coordinate[0])
            y_coordinates.append(coordinate[1])

        plt.plot(x_coordinates, y_coordinates)
        plt.axis([-3, 3.5, -3, 3])

        for i in range(0,len(self.o),2):
            circle = plt.Circle(self.o[i],self.o[i+1], color='#e2e2e2')
            plt.gca().add_patch(circle)        

        plt.grid()
        plt.show()
