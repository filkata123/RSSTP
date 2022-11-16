import External
n = 1
p = 90
l = 2
o = [[1,2],1,[-1,-2],1]
obj = External.External(n,p,l,o)

decision = (0,0)

print(obj.update(0))
print(obj.getPosition())