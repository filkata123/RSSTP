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

        if self.__hit_obstacle(self._calculate_coordinates(self.l, self.p)):
            raise Exception("Initial position must not intersect with objects")

    # Private methods 
    def _calculate_coordinates(self, length, position):
        x = round(length*math.cos(math.radians(position)),2)
        y = round(length*math.sin(math.radians(position)),2)

        return (x,y)

    def __hit_obstacle(self, coordinates):
        # this will create 2 circles at (1,2) and (-1,-2) with radii 1
        # idealy when we create instance of class we fill in obstacles 
        # make use of self.o to create obs

        #TODO: list of obstacles and less hard-coding
        #TODO(2): What if no objects?

        center1 = Point(self.o[0][0],self.o[0][1])
        circle1 = center1.buffer(self.o[1]).boundary

        center2 = Point(self.o[2][0],self.o[2][1])
        circle2 = center2.buffer(self.o[3]).boundary
        
        #constructing of 1 arm with 1 node at origin  with length l
        line = LineString([(0,0), (coordinates[0], coordinates[1])])

        #checks if line and any of the circles intersect
        obstacle1 = circle1.intersects(line)
        obstacle2 = circle2.intersects(line)

        if obstacle1 or obstacle2:
            return True
        else:
            return False

    # Public methods
    def get_sensory_data(self):
        #get inputs from existing sensor
        #Function with no input. The output is given by get_S().
        if self._calculate_coordinates(self.l, self.p) == self.feedback:      
            return 1
        else:
            return 0 

    def get_position(self):
        # This function returns p and also the actual geometry of the arm, i.e. the coordinates of the joints. 
        # This can be computed using p and L, assuming that the first joint is in the origin (0, 0).
        
        #TODO: coordinates for multiple joints
        coordinates = self._calculate_coordinates(self.l, self.p)
        return (self.p, coordinates)


    def update(self, a):
        new_position=self.p
        # This function takes as an input an action a from internal library.
        # The action a is an integer such that 0 ≤ a < 2n. If a = 2k for some k, then the k:th joint moves counterclockwise, 
        # and if a = 2k + 1 for some k, then the k:th joint moves clockwise.

        #TODO: multiple joints
        if a % 2 == 0: #move clockwise
            #k = int(a/2) 
            new_position = (new_position + 1) % 360
        else: #move counterclockwise
           # k = int((a-1)/2)
            new_position = (new_position - 1) % 360

        coordinates_after_move = self._calculate_coordinates(self.l, new_position)

        if not self.__hit_obstacle(coordinates_after_move):
            self.p = new_position # move arm to new position
        else:
            print('Position (' + str(coordinates_after_move) + ') unreachable due to object! \n')
