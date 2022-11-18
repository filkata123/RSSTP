import numpy as np

from internal import Internal

print('-'*15 + "demo matrix" +'-'*15)
demo = Internal(np.array([[(0,1),(1,2,4,3)],
                                   [(1,3,4),(0,2)]], dtype = object),0)
print(demo.transition_matrix)

print('-'*15 + "split(n) demonstration" +'-'*15)
print(demo.split(0))

print('-'*15 + "demo matrix" +'-'*15)
demo.transition_matrix = np.array([[(1,),(2,4),(2,)],
                                   [(),(),(1,)],
                                   [(0,),(),()]], dtype = object)
print(demo.transition_matrix)
print('-'*15 + "merge(n,m) demonstration" +'-'*15)
print(demo.merge(0,1))

print('-'*15 + "add(n,m,k) demonstration" +'-'*15)
print(demo.add(0,0,3))
print("\n")
print(demo.add(0,1,3) )
print("\n")
print(demo.add(1,0,3))
print("\n")
print(demo.add(1,1,3))

print('-'*15 + "delete(n,m,k) demonstration" +'-'*15)
print(demo.delete(0,0,3))
print("\n")
print(demo.delete(0,1,3) )
print("\n")
print(demo.delete(1,0,3))
print("\n")
print(demo.delete(1,1,3))
print("\n")

print('-'*15 + "transition(k) demonstration" +'-'*15)
for i in range(5):
    demo.current_state = 0
    print(demo.transition(2))
print("\n")

demo.current_state = 1
print(demo.transition(3))
print("\n")

demo.current_state = 1
print(demo.transition(0))
