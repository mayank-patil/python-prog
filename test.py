import numpy as np
a=np.array([1,2,3,4,4,4,4,4,6,6,4,6,7,8,9,9])
b=list(a)
c=[]
for i in b:
    if i in b and i not in c:
        c.append(i)
print(np.array(c))
6260775087
