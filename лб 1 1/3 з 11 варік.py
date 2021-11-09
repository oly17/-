import random
n=int(input("n="))
mas=random.sample(range(-100,100),n)
print(mas)

d=10**2
for i in mas:
    if 0<i<d:
        d=i
print("Мінімальний додатній елемент= ",d)

S=0
for i in mas:
    if i%2==0:
        S=S+i
print("Сума парних елементів масиву=",S)

list.reverse(mas)
print("Масив у зворотньому порядку= ", mas)

