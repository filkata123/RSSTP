import math

from shapely.geometry import LineString, Point

#pip install shapely

class External:
    #Constructor of External
    def __init__(self, n, p, l, o, feedback):
        # n = number of joints : int : > 0
        # l = arm lenghts : List<float> with size n
        # o = list of obstacles
        # p = initial position of arm
        # feedback = point which will give feedback to algorithms

        self.n = n
        self.l = l
        self.o = o
        self.p = p
        self.feedback = feedback
        results= self.__hit_obstacle(self.p)
        if results[0]:
            raise Exception("Initial position must not intersect with obstacles")

    # Private methods
    
    def _calculate_coordinates(self, new_position,joint_nbr):
        x=0
        y=0
        lengths=[]

        for i in range(joint_nbr+1):
                lengths.append(self.l[i])
        for i in range(joint_nbr+1):
                temp_x = round(lengths[i]*math.cos(math.radians(new_position[i])),2)
                temp_y = round(lengths[i]*math.sin(math.radians(new_position[i])),2)
                x = round((x + temp_x),2)
                y = round((y + temp_y),2)

        return (x,y)  # this will always return x,y for joint i
    

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
        for i in range(nbr_of_lines):
            #constructing of 1 arm with 1 node at origin  with length l
            
            coordinates_2.append(self._calculate_coordinates(new_position,i))
            if i > 1:
                line.append(LineString([(coordinates_2[i-1][0], coordinates_2[i-1][1]), (coordinates_2[i][0], coordinates_2[i][1])]))
            else:
                line.append(LineString([(0,0), (coordinates_2[i][0], coordinates_2[i][1])]))

        for i in range(nbr_of_lines):

            #make sure adjacent arms cant be on top on eahcother
            if (nbr_of_lines-i>1):
                if (abs(new_position[i]-new_position[i+1]) <= 181 and abs(new_position[i]-new_position[i+1]) >= 179):
                    
                    return [True,0,i+1,i]


            # check intersection between arms
            for j in range(i,nbr_of_lines):  
                if (nbr_of_lines-j>2):
                    if(line[i].intersects(line[j+2])):
                        arm_collided_with = i
                        colliding_arm = j+2
                        return [True,0,arm_collided_with,colliding_arm]
        
        for i in range(nbr_of_obstacles):           
            for j in range(nbr_of_lines):
                if  (circle[i].intersects(line[j])):
                    obsatcle_hit = j
                    arm_hitting = i
                    return[True,1,obsatcle_hit,arm_hitting]
            #checks if line and any of the circles intersect


        
        return [False,0, 0, 0]
            

    # Public methods
    def get_sensory_data(self):
        #get inputs from existing sensor
        #Function with no input. The output is given by get_S().

        joints_in_home_position = 0
        for i  in range(self.n):
            if self._calculate_coordinates( self.p,i) == self.feedback[i]:      
                joints_in_home_position = joints_in_home_position + 1
        
        if joints_in_home_position == self.n:
            return 1
        else:
            return 0

    def get_position(self):
        # This function returns p and also the actual geometry of the arm, i.e. the coordinates of the joints. 
        # This can be computed using p and L, assuming that the first joint is in the origin (0, 0).
        coordinates=[]

        for i in range(self.n):
            
            coordinates.append(self._calculate_coordinates( self.p,i))
            
        return (coordinates)


    def update(self, a):
        new_position=[]
        for i in range(self.n):
            new_position.append(self.p[i])
        # This function takes as an input an action a from internal library.
        # The action a is an integer such that 0 ≤ a < 2n. If a = 2k for some k, then the k:th joint moves counterclockwise, 
        # and if a = 2k + 1 for some k, then the k:th joint moves clockwise.

        if a % 2 == 0: #move clockwise
            k = int(a/2) 
            while (new_position[k] <0):
                new_position[k]= new_position[k]+360
            new_position[k] = (new_position[k] + 1) % 360
        else: #move counterclockwise
            k = int((a-1)/2)
            while (new_position[k] <0):
                new_position[k]= new_position[k]+360
            new_position[k] = (new_position[k] - 1) % 360
        coordinates_after_move = self._calculate_coordinates(new_position,k)
        results=self.__hit_obstacle(new_position)

        if not results[0] :
            self.p[k] = new_position[k] # move joint to new position
        elif results[1] == 1:
            print('Position of joint '+ str(results[2]) +' (' + str(coordinates_after_move) + ') is unreachable due to object '+str(results[3])+'! \n')
        else:
            print('line '+ str(results[2]) +' intersects with line '+str(results[3])+'! \n')

        
