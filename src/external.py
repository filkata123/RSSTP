import math

from shapely.geometry import LineString, Point
import matplotlib.pyplot as plt

class External:
    def __init__(self, n, p, l, o, d, feedback):
        """ Constructor of External

        Args:
            n (int > 0): number of joints
            p (array<int>): initial position of arm
            l (array<int>): arm lengths with size n
            o (array<...>): list of obstacles with form [[x,y], size, ... [x_n,y_n], size_n]
            d (int): arm step - rotate by how many angles
            feedback (list<tuple<floats>>): points, which will create sensory feedback when reached

        Raises:
            Exception: Initial position intersects with obstacles
        """

        self._n = n
        self._l = l
        self._o = o
        self._p = p
        self._d = d
        self._feedback = feedback
        joint_to_move = 0   #none
        collision, *_ = self.__hit_obstacle(self._p, joint_to_move)
        if collision:
            raise Exception("Initial position must not intersect with obstacles")
        if len(self._o) == 0:
            print("no obstacles in space")

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
        for i in range(self._n):
            lengths.append(self._l[i])
        
        p=0
        x=0
        y=0

        for i in range(self._n):
            p = p + position[i]

            temp_x = round(lengths[i]*math.cos(math.radians(p)),2)
            temp_y = round(lengths[i]*math.sin(math.radians(p)),2)
            x = round((x + temp_x),2)
            y = round((y + temp_y),2)
            coordinates.append((x,y))
        return coordinates # this will always return x,y for joint i
    

    def __hit_obstacle(self, position, joint):
        """ Check whether any collision will ocur at given position
        Args:
            position (int): Position to be checked
            joint (int): Joint 

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
        n_obstacles = int(len(self._o)/2)
        n_arms = self._n
        
        coordinates = self._calculate_coordinates(position) 
        for i in range(n_arms):
            # constructing of 1 arm with 1 node at origin with length l
            
            if i == 0:
                arms.append(LineString([(0,0), (coordinates[i][0], coordinates[i][1])]))
            else:
                arms.append(LineString([(coordinates[i-1][0], coordinates[i-1][1]), (coordinates[i][0], coordinates[i][1])]))

        if (n_arms > 1):
                # Ensure that arms are dont clip
                if (self._p[joint] <= 181 + self._d and self._p[joint] >= 179 - self._d):
                    if(position[joint] <= 181 + self._d and position[joint] >= 179 - self._d):
                        collision = True
                        obstacle_collision = False
                        collided_arm = joint 
                        collided_object = joint - 1
                        return collision, obstacle_collision, collided_arm, collided_object
                # checking collision between arms
                for i in range(n_arms):
                    # make sure adjacent arms cant be on top of each other
                    if (position[i] <= 181 and position[i] >= 179 ):
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
        
            

        # create obstacles 
        for i in range(0,len(self._o),2):
                center.append(Point(self._o[i][0],self._o[i][1]))
                circle.append(center[int(i/2)].buffer(self._o[i+1]).boundary)

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
        coordinates = self._calculate_coordinates(self._p)
        for i  in range(self._n):
            if coordinates[i] == self._feedback[i]:      
                joints_in_home_position = joints_in_home_position + 1
        
        #TODO change return to float in future implementations
        #RETURNS BOOLEAN:
        
        if joints_in_home_position == self._n:
            return True
        else:
            return False    

    def get_position(self):
        """ Get p and also the actual geometry of the arm, i.e. the coordinates of the joints. 

        Returns:
            list: Coordinates of all joints
        """
        coordinates = []
        
        coordinates = self._calculate_coordinates(self._p)
        return self._p, coordinates


    def update(self, a):
        """ Use action a to move respective joint. If a = 2k for some k,
        then the k:th joint moves counterclockwise, 
        and if a = 2k + 1 for some k, then the k:th joint moves clockwise.

        Args:
            a (int): Action a; 0 ≤ a < 2n
        """
        new_position=[]
        for i in range(self._n):
            new_position.append(self._p[i])
        #move clockwise
        if a % 2 == 0: 
            k = int(a/2) 
            while (new_position[k] + self._d < 0):
                new_position[k] = new_position[k] + 360
            new_position[k] = (new_position[k] + self._d) % 360
        #move counterclockwise
        else: 
            k = int((a-1)/2)
            while (new_position[k] - self._d < 0):
                new_position[k] = new_position[k] + 360
            new_position[k] = (new_position[k] - self._d) % 360
        joint_to_move = k
        coordinates_after_move = self._calculate_coordinates(new_position)
        collision, obstacle_collision, collided_arm, collided_object = self.__hit_obstacle(new_position, joint_to_move)

        if not collision:
            # move joint to new position
            self._p[k] = new_position[k] 
        elif obstacle_collision:
            print('Position of joint ' + str(collided_arm) +' (' + str(coordinates_after_move[k]) + ') is unreachable due to object ' + str(collided_object)+'! \n')
        else:
            print('arm ' + str(collided_arm) + ' intersects with arm ' + str(collided_object) + '! \n')

    def visualise_arm(self):
        """ Visalise arm movement
        """

        coordinates = self._calculate_coordinates(self._p)
        x_coordinates=[0]
        y_coordinates=[0]

        for coordinate in coordinates:
            x_coordinates.append(coordinate[0])
            y_coordinates.append(coordinate[1])

        plt.ion()
        plt.plot(x_coordinates, y_coordinates)
        plt.axis([-5, 5.5, -5, 5])

        for i in range(0,len(self._o),2):
            circle = plt.Circle(self._o[i],self._o[i+1], color='#e2e2e2')
            plt.gca().add_patch(circle)        

        plt.grid()
        plt.figure(1)#Teemu and Rafi
        plt.pause(0.1) # value can be changed
        plt.clf()


# ---Teemu ja rafin koodi-----
    def distance_from_obstacle(self):
        '''
        Calculates the distance between the tip of the arm and obstacles.
        Prints the distance for every joint and obstacle individually.
        Returns a list containing list of distances for evvry joint.
        e.g. [[joint 0 obstacle 0, joint 0 obstacle 1], [joint 1 obstacle 0, joint 1 obstacle 1]]
        '''
        #get coordinates of the arm
        coordinates = self._calculate_coordinates(self._p)
        distances = []#list of distances for all joints for all obstacles

        for i in range(0, len(coordinates)):            #for every joint
            distance_for_joint = []#list of distances for a single joint for all obstacles.

            for k in range(0, len(self._o), 2):         #for every obstacle
                distance_x = self._o[k][0] - coordinates[i][0]        #distance in x axis
                distance_y = self._o[k][1] - coordinates[i][1]        #distance in y axis
                #calculate the distance with Pythagoras' theorem and subtract the radius of the obstacle
                distance_total = math.sqrt(distance_x**2 + distance_y**2) - self._o[k+1]
                distance_for_joint.append(distance_total)

                print("Distance between joint {} and obstacle {}: {}".format(i, k, distance_total))#obstacles are numbered 0, 2, 4,...
            distances.append(distance_for_joint)

        return distances
    
    def get_sensory_data_float(self):
        '''
        Get sensory feedback as a float between 0-1. Calculate the distance between the joint and its home position and
        scale the distance between 0-1. Returns the average result of every joint.
        Returns:
            float between 0 and 1
            1 = joint is at its home position
            0 = joint is as far away from its home position as possible
        
        '''
        coordinates = self._calculate_coordinates(self._p)
        all_results = []    # holds results for every joint individually

        for i in range(self._n):   # for every joint
            # max_distance is used for scaling the distance between 0-1
            # max_distance = (sensory feedback point's distance from origo) + (full arm length)

            # sensory feedback point's distance from origo:
            max_distance = math.sqrt(self._feedback[i][0]**2 + self._feedback[i][1]**2)

            # adding arm's length to max_distance up to current joint
            j = i
            while (j>=0):
                max_distance = max_distance + self._l[j]  #add joint length to max_distance
                j = j - 1

            # calculate distance between the joint and its home position:
            distance_x = self._feedback[i][0] - coordinates[i][0]   # distance in x axis
            distance_y = self._feedback[i][1] - coordinates[i][1]   # distance in y axis
            distance_total = math.sqrt(distance_x**2 + distance_y**2)
            #distance scaled between 0-1:
            distance_total_scaled = distance_total / max_distance
            result = 1 - distance_total_scaled
            # add the result to all_results
            all_results.append(result)

        # calculate the average result of every joint
        average_result = sum(all_results) / self._n

        return average_result   # return a value between 0-1 which tells how close the joints are to their home position on average





