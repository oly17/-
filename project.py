from tkinter import *

from table import opentabble
from grafic import showplot
from table_1 import opentabble_1
from table_txt import opentabble_2
from to_json import convertInJSON, convertToJSON

root=Tk()
root.title('Довідник')
root.geometry('200*200')
root.resizable(False,False)
root.configure(bg='grey22')


def openPlot():
    showplot()

def openTable():
    opentabble()
    root_2=Tk()
    root_2.geometry('200*100')
    root_2.title('Таблиця')
    lbl = Label(root_2)
    lbl.configure(front=(7),text="таблиця в консолі")
    lbl.place(x = 0, y = 0)
    root_2.mainloop()
    
def creataJSON():
    convertToJSON()
    root_3=Tk()
    root_3.geometry('360*70')
    root_3.resizable(False,False)
    root_3.title('файл')
    lbl=Label(root_3)
    lbl.configure(font=(8),text='Файл у форматі JSON сформовано')
    lbl.place(x = 4, y = 2)
    root_3.mainloop()
    
def create_JSON():
    convertInJSON()
    root_4=Tk()
    root_4.geometry('356*50')
    root_4.resizable(False,False)
    root_4.title('повідомлення')
    lbl=Label(root_4)
    lbl.configure(font=(10),text='Файл у форматі JSON сформовано')
    lbl.place(x = 4, y = 2)
    root_4.mainloop()

def openTable_1():
    opentabble_1()
    root_5=Tk()
    root_5.geometry('356*50')
    root_5.resizable(False,False)
    root_5.title('повідомлення')
    lbl=Label(root_5)
    lbl.configure(front=(10),text='Таблиця сформована в .exel')
    lbl.place(x = 4, y = 2)
    root_5.mainloop()

def openTable_2():
    opentabble_2()
    root_6=Tk()
    root_6.geometry('356*50')
    root_6.resizable(False,False)
    root_6.title('повідомлення')
    lbl=Label(root_6)
    lbl.configure(front=(10),text='Таблиця сформована в .txt')
    lbl.place(x = 4, y = 2)
    root_6.mainloop()

btn1=Button(root)
btn1.configure(bg='grey',fg='white',text='відкрити графік',command=openPlot)
btn1.place(x=15,y=20,width=180,height=25)
root.mainloop()

btn2=Button(root)
btn2.configure(bg='grey',fg='white',text='відкрити таблицю',command=openTable)
btn2.place(x=15,y=50,width=180,height=25)

btn3=Button(root)
btn3.configure(bg='grey',fg='white',text='відкрити одиниці виміру(JSON)',command=creataJSON)
btn3.place(x=15,y=80,width=180,height=25)

btn4=Button(root)
btn4.configure(bg='grey',fg='white',text='відкрити показники (JSON)',command=create_JSON)
btn4.place(x=15,y=110,width=180,height=25)

btn5=Button(root)
btn5.configure(bg='grey',fg='white',text='створити таблицю в .exel',command=openTable_1)
btn5.place(x=15,y=140,width=180,height=25)

btn6=Button(root)
btn6.configure(bg='grey',fg='white',text='створити таблицю в .txt',command=openTable_2)
btn6.place(x=15,y=170,width=180,height=25)


root.mainloop()


