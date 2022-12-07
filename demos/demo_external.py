from external import External


print("------------------ONE ARM------------------")
n = 1
p = [95]
l = [2]
o = []
d = 1
feedback = [(-0.14,2.0)]
one_arm = External(n, p, l, o, d, feedback)

for x in range (11):
    if x <= 7:
        print("------------------move right------------------")
        one_arm.update(1)
    else:
        print("------------------move left------------------")
        one_arm.update(0)
    #one_arm.visualise_arm()
    print("Moved to position: ")
    print(one_arm.get_position())
    print("Reached destination: ")
    print(one_arm.get_sensory_data())


print("------------------THREE ARMS------------------")
n = 3
p = [0,178,182]
l = [3,2,1]
o = [[1.5,1],0.5,[1.5,-1.5],0.5]
d = 5
feedback = [(3.0, 0.0),(1.0,0.07),(2.0,0.07)]
obj = External(n, p, l, o, d, feedback)

print("Moved to position: ")
print(obj.get_position())
print("Reached destination: ")
print(obj.get_sensory_data())


obj.visualise_arm()
print( "moving up until about to hit obstacle 0")
for x in range (3):

    if x%3 == 0:
        print("------------------move joint 0 Left------------------")
        obj.update(0)
    elif x%3 ==1:
        print("------------------move joint 1 Right------------------")
        obj.update(3)
    elif x%3==2:
        print("------------------move joint 2 left------------------")
        obj.update(4)
    
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
print(obj.p)
obj.visualise_arm()
print( "moving down until about to hit obstacle 0")
for x in range (3):

    if x%3 == 2:
        print("------------------move joint 0 right------------------")
        obj.update(1)
    elif x%3 ==1:
        print("------------------move joint 1 left------------------")
        obj.update(2)
    elif x%3==0:
        print("------------------move joint 2 right------------------")
        obj.update(5)
    
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
print(obj.p)
obj.visualise_arm()
for x in range(9):
    print("------------------move joint 0 Right------------------")
    obj.update(1)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
obj.visualise_arm()    

print( "straightening th arm")
for x in range (70):
    
 
    if x%2 == 0:
        print("------------------move joint 1 Right------------------")
        obj.update(3)
    elif x%2 == 1:
        print("------------------move joint 2 left------------------")
        obj.update(4)
    
    
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
obj.visualise_arm()
print(obj.p)   

print("crooking the arm")

for x in range (24):

    print("------------------move joint 2 right------------------")
    obj.update(5)
    
    
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
obj.visualise_arm()
print(obj.p)   

print("going up until collide with obj 0")

for x in range(13):
    
    print("------------------move joint 0 Left------------------")
    obj.update(0)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
obj.visualise_arm()
print(obj.p)

print("put the arm together")

for x in range (35):

    print("------------------move joint 1 Right------------------")
    obj.update(3)
    
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
obj.visualise_arm()
print(obj.p) 

print("flattening the arm")


print("------------------move joint 1 Right------------------")
obj.update(2)

print("Moved to position: ")
print(obj.get_position())
print("Reached destination: ")
print(obj.get_sensory_data())
obj.visualise_arm()
print(obj.p)

print("flattening the arm")
for x in range (24):

    print("------------------move joint 2 right------------------")
    obj.update(5)
    
    
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
obj.visualise_arm()
print(obj.p)

for x in range (24):

    print("------------------move joint 1 right------------------")
    obj.update(3)
    
    
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
obj.visualise_arm()
print(obj.p)

'''
print( "moving down about to hit obstacle 0")
for x in range (24):

    if x%3 == 0:
        print("------------------move joint 0 Left------------------")
        obj.update(0)
    elif x%3 ==1:
        print("------------------move joint 1 Right------------------")
        obj.update(3)
    elif x%3==2:
        print("------------------move joint 2 left------------------")
        obj.update(4)
    
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
print(obj.p)'''
'''
 print("going back down until collide with self")
for x in range(13):
    if x%3 == 0:
        print("------------------move joint 0 Right------------------")
        obj.update(1)
    elif x%3 ==1:
        print("------------------move joint 1 Left------------------")
        obj.update(2)
    elif x%3==2:
        print("------------------move joint 2 Right------------------")
        obj.update(5)
    
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())

print("moving up until about to hit obstacle 0")
for x in range (13):

    if x%3 == 0:
        print("------------------move joint 0 Left------------------")
        obj.update(0)
    elif x%3 ==1:
        print("------------------move joint 1 Right------------------")
        obj.update(3)
    elif x%3==2:
        print("------------------move joint 2 Left------------------")
        obj.update(4)
    
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())

print("move first joint 0 down until arm collid with self")

for x in range(9):
    print("------------------move joint 0 Right------------------")
    obj.update(1)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
    


print("move joint 1 up until about to hit obs 0")
for x in range(17):
    print("------------------move joint 1 Right------------------")
    obj.update(3)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())


print("move first joint 0 down until hit obs 1")

for x in range(16):
    print("------------------move joint 0 Right------------------")
    obj.update(1)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())

print("move joint 1 up until about to hit obs 0")
for x in range(27):
    print("------------------move joint 1 Right------------------")
    obj.update(3)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())

print("move first joint 0 down until hit obs 1")

for x in range(16):
    print("------------------move joint 0 Right------------------")
    obj.update(1)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())

print("move joint 1 up until about to hit obs 0")
for x in range(65):
    print("------------------move joint 1 Right------------------")
    obj.update(3)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())

print("move joint 1 up until about to hit obs 0")
for x in range(200):
    print("------------------move joint 2 Left------------------")
    obj.update(4)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())

print("move joint 1 up until about to hit obs 0")
for x in range(53):
    print("------------------move joint 1 Left------------------")
    obj.update(2)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
'''