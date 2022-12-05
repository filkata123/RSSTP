import math

from shapely.geometry import LineString, Point

import matplotlib.pyplot as plt
import numpy as np

#pip install shapely

class External:
    #Constructor of External
    def __init__(self, n, p, l, o, d, feedback):
        # n = number of joints : int : > 0
        # l = arm lenghts : List<float> with size n
        # o = list of obstacles
        # p = initial position of arm
        # d = arm step
        # feedback = point which will give feedback to algorithms

        self.n = n
        self.l = l
        self.o = o
        self.p = p
        self.d = d
        self.feedback = feedback
        results= self.__hit_obstacle(self.p)
        if results[0]:
            raise Exception("Initial position must not intersect with obstacles")

    # Private methods
    
    def _calculate_coordinates(self, new_position):
        lengths=[]
        coordinates=[]
        for i in range(self.n):
            lengths.append(self.l[i])
        
        p=0
        x=0
        y=0


        for i in range(self.n):
                p = p + new_position[i]

                temp_x = round(lengths[i]*math.cos(math.radians(p)),2)
                temp_y = round(lengths[i]*math.sin(math.radians(p)),2)
                #print("temp :( "+ str(temp_x) + " , " + str(temp_y) +" )")
                x = round((x + temp_x),2)
                y = round((y + temp_y),2)
                coordinates.append((x,y))
                #print(" x for joint "+ str(i) +  " ( "+ str(x) + " , "+ str(y) +" )")

        return coordinates # this will always return x,y for joint i
    

    def __hit_obstacle(self, new_position):
        # this will create 2 circles at (1,2) and (-1,-2) with radii 1
        # idealy when we create instance of class we fill in obstacles 
        # make use of self.o to create obs
        coordinates_2=[]
        line=[]
        center=[]
        circle=[]
        lines = []  
        i=0
        for i in range(self.n):
            lines.append(self.l[i])

        # range determiners
        nbr_of_obstacles = int(len(self.o)/2)
        nbr_of_lines = self.n

        
        


        if len(self.o) == 0:
            print ("No obstacles in environment")
            return False
        else: 
               
            for i in range(0,len(self.o),2):
                center.append(Point(self.o[i][0],self.o[i][1]))
                circle.append(center[int(i/2)].buffer(self.o[i+1]).boundary)
        
        coordinates_2 =self._calculate_coordinates(new_position) 
        for i in range(nbr_of_lines):
            #constructing of 1 arm with 1 node at origin  with length l
            
            if i > 1:
                line.append(LineString([(coordinates_2[i-1][0], coordinates_2[i-1][1]), (coordinates_2[i][0], coordinates_2[i][1])]))
            else:
                line.append(LineString([(0,0), (coordinates_2[i][0], coordinates_2[i][1])]))

        #checking arms with arms
        for i in range(nbr_of_lines):

            #make sure adjacent arms cant be on top on eahcother
            if (i>0):
                if (new_position[i] <= 181 and new_position[i] >= 179):
                    
                    return [True,0,i,i-1]


            # check intersection between arms
            for j in range(i,nbr_of_lines):  
                if (nbr_of_lines-j>2):
                    if(line[i].intersects(line[j+2])):
                        arm_collided_with = i
                        colliding_arm = j+2
                        return [True,0,arm_collided_with,colliding_arm]


        #checking arms with obstacles
        for i in range(nbr_of_obstacles):           
            for j in range(nbr_of_lines):
                if  (circle[i].intersects(line[j])):
                    obsatcle_hit = j
                    arm_hitting = i
                    return[True,1,obsatcle_hit,arm_hitting]
            


        
        return [False,0, 0, 0]
            

    # Public methods
    def get_sensory_data(self):
        #get inputs from existing sensor
        #Function with no input. The output is given by get_S().

        joints_in_home_position = 0
        coordinates = self._calculate_coordinates( self.p)
        for i  in range(self.n):
            if coordinates[i] == self.feedback[i]:      
                joints_in_home_position = joints_in_home_position + 1
        
        if joints_in_home_position == self.n:
            return 1
        else:
            return 0

    def get_position(self):
        # This function returns p and also the actual geometry of the arm, i.e. the coordinates of the joints. 
        # This can be computed using p and L, assuming that the first joint is in the origin (0, 0).
        coordinates_3=[]
        
        coordinates_3 = self._calculate_coordinates(self.p)   
        self.plot(coordinates_3)
        return coordinates_3


    def update(self, a):
        new_position=[]
        for i in range(self.n):
            new_position.append(self.p[i])
        # This function takes as an input an action a from internal library.
        # The action a is an integer such that 0 ≤ a < 2n. If a = 2k for some k, then the k:th joint moves counterclockwise, 
        # and if a = 2k + 1 for some k, then the k:th joint moves clockwise.

        if a % 2 == 0: #move clockwise
            k = int(a/2) 
            while (new_position[k] - self.d <0):
                new_position[k]= new_position[k]+360
            new_position[k] = (new_position[k] + self.d) % 360
        else: #move counterclockwise
            k = int((a-1)/2)
            while (new_position[k]- self.d <0):
                new_position[k]= new_position[k]+360
            new_position[k] = (new_position[k] - self.d) % 360
        
        coordinates_after_move = self._calculate_coordinates(new_position)
        results=self.__hit_obstacle(new_position)

        if not results[0] :
            self.p[k] = new_position[k] # move joint to new position
        elif results[1] == 1:
            print('Position of joint '+ str(results[2]) +' (' + str(coordinates_after_move[k]) + ') is unreachable due to object '+str(results[3])+'! \n')
        else:
            print('line '+ str(results[2]) +' intersects with line '+str(results[3])+'! \n')


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

        