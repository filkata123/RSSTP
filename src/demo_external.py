from external import External

# n = 2
# p = [95,80]
# l = [2,3]
# o = [[1,2],1,[-1,-2],1]
# feedback = (0.38, 4.95)
# obj = External(n, p, l, o, feedback)

# n = 2
# p = [26.56, 45.00]
# l = [4.47,5.65]
# o = [[5,4],1,[-2,-2],1]
# feedback = (0.38, 4.95)
# obj = External(n, p, l, o, feedback)

n = 3
p = [120, 108.43, 180]
l = [2.82, 9.48,4.00]
o = [[3,3],1,[-8,9],1, [-5,-3], 1]
feedback = (0.38, 4.95)
obj = External(n, p, l, o, feedback)

for x in range (11):
    if x <= 7:
        print("------------------move right------------------")
        obj.update(1)
    else:
        print("------------------move left------------------")
        obj.update(0)
    print("Moved to position: ")
    print(obj.get_position())
    print("Reached destination: ")
    print(obj.get_sensory_data())
