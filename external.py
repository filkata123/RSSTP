class External:
    
    #Constructor of External
    def_init_(self, n,p,l,o):
        self.n = n
        self.p = p
        self.l = l
        self.o = o

    def getSensoryData():
        #get inputs from existing sensor
        #Function with no input. The output is given by get_S().
        #import the sensory library and get the binary input,
        input = str(0b11100101)
        # Extracting inputs we want 
        return input[:, 4];

    def hitObstacle(p_input):
        #get inputs from existing sensor

    def getPoistion(l,p):
        #This function returns p and also the actual geometry of the arm, i.e. the coor-dinates of the joints. 
        #This can be computed using p and L, assuming that the first joint is in the origin (0, 0).

    def update(a):
        #This function takes as an input an action a.
        #The action a is an integer such that 0 ≤ a < 2n. If a = 2k for some k, then the k:th joint moves counterclockwise, 
        # and if a = 2k + 1 for some k, then the k:th joint moves clockwise.

    