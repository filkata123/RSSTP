import math

from shapely.geometry import LineString, Point

#pip install shapely

  # will be used to store which new position to move to
class External:
    decision = (0,0)
    #Constructor of External
    def __init__(self, n,p,l,o):
        self.n = n
        self.p = p
        self.l = l
        self.o = o

    def getSensoryData(self,coordinate):
        #get inputs from existing sensor
        #Function with no input. The output is given by get_S().
         # definition of sensory feedback point on a plane
        feedback = (-0.14,2.0) 
        if (coordinate == feedback):      
            return 1
        else:
            return 0 

        

    def hitObstacle(self, coordinate):
        # this will create 2 circles at (1,2) and (-1,-2) with radii 1
        # idealy when we create instance of class we fill in obstacles 
        # make use of self.o to create obs
        center1 = Point(1.0,2.0)
        center2 = Point(-1.0,-2.0)
        circle1 = center1.buffer(1).boundary
        circle2 = center2.buffer(1).boundary
        
        #constructing of 1 arm with 1 node at origin  with length l
        line = LineString([(0,0), (coordinate[0], coordinate[1])])

        #checks if line and any of the circles intersect
        obstacle1 = circle1.intersects(line)
        obstacle2 = circle2.intersects(line)

        if (obstacle1 or obstacle2):
            self.p = self.decision[0] # reset position to old position
            return True
        else:
            self.p = self.decision[1] # move arm to new position
            return False

    def getPosition(self,p):
        # This function returns p and also the actual geometry of the arm, i.e. the coor-dinates of the joints. 
        # This can be computed using p and L, assuming that the first joint is in the origin (0, 0).

        length = self.l
        position = p

        x = round(length*math.cos(math.radians(position)),2)
        y = round(length*math.sin(math.radians(position)),2)
        coordinate = (x,y)
        return coordinate

    def update(self, a):
        new_position=self.p
        old_position=self.p
        # This function takes as an input an action a from internal library.
        # The action a is an integer such that 0 ≤ a < 2n. If a = 2k for some k, then the k:th joint moves counterclockwise, 
        # and if a = 2k + 1 for some k, then the k:th joint moves clockwise.

         # p array of positions of each joint
        if a%2 == 0: #move clock wiseS
            #k = int(a/2) 
            new_position = (new_position + 1) % 360
        else: #move counterclockwise
           # k = int((a-1)/2)
            new_position = (new_position - 1) % 360

        # list with new and old position, decision to move arm will be made in hit_obstacle()
        self.decision = (old_position,new_position)
        p = new_position

        # return new potential position of arm with which joint to move
        return p
