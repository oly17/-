import random
n=int(input("n="))
mas=random.sample(range(-100,100),n)
print(mas)

print("Мінімальний від'ємний елемент",min(mas))

S=0
for i in mas:
    if i<0:
        S=S+i
print("Сума від'ємних елементів масиву=",S)


k=0
for i in mas:
    if i>0:
        k=k+1
print("Кількість додатніх елементів масиву= ",k)

for i in range (len(mas)):
    if mas[i]>0:
     print("Додатній елемент масиву =  ",mas[i])
     











    


    







