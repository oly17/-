n=int(input("n="))
import math
Ist=[]
for i in range(1,int(math.sqrt(n))+1):
    if n %i ==0:
        Ist.append(i)
        Ist.append(n//i)
Ist=list(set(Ist))
Ist.sort()
print(Ist)
