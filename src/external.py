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

        if self.__hit_obstacle(self.p):
            raise Exception("Initial position must not intersect with obstacles")

    # Private methods

    def _calculate_coordinates(self, new_position,joint_nbr):
        x=0
        y=0
        lengths=[]
        for i in range(joint_nbr):
            lengths.append(self.l[i])
        for i in range(joint_nbr):
            print(type(new_position))
            print(new_position)
            temp_x = round(lengths[i]*math.cos(math.radians(new_position[i])),2)
            temp_y = round(lengths[i]*math.sin(math.radians(new_position[i])),2)
            x+= temp_x
            y+= temp_y

        return (x,y)  # this will always return x,y for joint i

    def __hit_obstacle(self, new_position):
        # this will create 2 circles at (1,2) and (-1,-2) with radii 1
        # idealy when we create instance of class we fill in obstacles 
        # make use of self.o to create obs
        coordinates_2=[]
        line=[]
        obstacle=[]
        center=[]
        circle=[]
        lines = []
        i=0
        for i in range(self.n):
            lines.append(self.l[i])
        nbr_of_obstacles = len(self.o)/2
        nbr_of_lines = self.n
        size_of_bool = nbr_of_lines * nbr_of_obstacles
        #TODO: list of obstacles and less hard-coding #Done
        #TODO(2): What if no objects? #Done
        if len(self.o) == 0:
            print ("No obstacles in environment")
            return False
        else:    
            for i in range(len(self.o),2):

                center.append(Point(self.o[i][0],self.o[i][1]))
                circle.append(center[i].buffer(self.o[i+1]).boundary)


        for i in range(self.n):
            #constructing of 1 arm with 1 node at origin  with length l
            coordinates_2.append(self._calculate_coordinates(new_position[i],i))
            if i > 1:
                line.append(LineString([(coordinates_2[i-1][0], coordinates_2[i-1][1]), (coordinates_2[i][0], coordinates_2[i][1])]))
            else:
                line.append(LineString([(0,0), (coordinates_2[i][0], coordinates_2[i][1])]))

        for i in range(nbr_of_obstacles):
            for j in range(nbr_of_lines):
                obstacle.append(circle[i].intersects(line[j]) )  
            #checks if line and any of the circles intersect

        for i in range(size_of_bool): #nbr of obstacles * nbr of lines/arms
            if obstacle[i]:
                return True
            else:
                return False

    # Public methods
    def get_sensory_data(self):
        #get inputs from existing sensor
        #Function with no input. The output is given by get_S().
        #TODO: Figure out what is feedback for n joints
        if self._calculate_coordinates( self.p,self.n) == self.feedback:      
            return 1
        else:
            return 0 

    def get_position(self):
        # This function returns p and also the actual geometry of the arm, i.e. the coordinates of the joints. 
        # This can be computed using p and L, assuming that the first joint is in the origin (0, 0).
        coordinates=()
        #TODO: coordinates for multiple joints #Done
        for i in range(self.n):
            coordinates.append(self._calculate_coordinates( self.p,i))
            return (self.p, coordinates)


    def update(self, a):
        new_position=[]
        for i in range(self.n):
            new_position.append(self.p[i])
        # This function takes as an input an action a from internal library.
        # The action a is an integer such that 0 ≤ a < 2n. If a = 2k for some k, then the k:th joint moves counterclockwise, 
        # and if a = 2k + 1 for some k, then the k:th joint moves clockwise.

        #TODO: multiple joints #Done
        if a % 2 == 0: #move clockwise
            k = int(a/2) 
            new_position[k] = (new_position[k] + 1) % 360
        else: #move counterclockwise
            k = int((a-1)/2)
            new_position[k] = (new_position[k] - 1) % 360

        coordinates_after_move = self._calculate_coordinates(new_position,k)

        if not self.__hit_obstacle(new_position):
            self.p[k] = new_position[k] # move joint to new position
        else:
            print('Position of joint '+ k +' is (' + str(coordinates_after_move) + ') unreachable due to object! \n')

        
