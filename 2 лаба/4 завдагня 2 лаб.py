a=[]
for x in range(0,6):
    a.append(int(input("Введите элемент массива")))
print(a)

srt=a[:]
srt.sort(reverse=True)

if srt[4]==srt[3]:
    num1=a.index(srt[4])
    num2=a.index(srt[3],num1+1)
    num3=a.index(srt[2],num2+1)
    num4=a.index(srt[1],num3+1)
    num5=a.index(srt[0],num4+1)
else:
    num1=a.index(srt[4])
    num2=a.index(srt[3])
    num3=a.index(srt[2])
    num4=a.index(srt[1])
    num5=a.index(srt[0])
print("Перший мінімум = ", srt[4],"его номер ", num1)
print("Другий мінімум = ", srt[3],"его номер ", num2)
print("Третій мінімум = ", srt[2],"его номер ", num3)
print("Четвертий мінімум = ", srt[1],"его номер ", num4)
print("Пятий мінімум = ", srt[0],"его номер ", num5)