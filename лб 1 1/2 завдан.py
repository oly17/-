n=int(input("n= "))
i=2
k=666
while i<n:
    if n%i!=0:
        k=1
    else:
        k=0
        break
    i+=1
if k==1:
    print("Число просте")
else:
    print("Число не просте")
    