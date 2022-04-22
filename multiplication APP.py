from ast import Delete
from email import message
from tkinter import *
from tkinter import messagebox

from setuptools import Command



win=Tk()
win.geometry("900x500")
win.title("Multiplication")
#win label
Label(win,text="Multiplication",bd=5,font=("",28,"bold")).pack()



#frame
#********************************************************start frame***************************************************************************

#left frame
left_frame=Frame(win,bd=5,background="blue")
left_frame.place(x=0,y=50,width=450,height=400)


#right frame
right_frame=Frame(win,bd=5,background="white")
right_frame.place(x=450,y=50,width=450,height=400)

#************************************************************end frame***************************************************************************





#***************************************************************************frame Ceate*********************************************************************

Label(right_frame,text="Display TABLE",width=30,font=("",22,"bold"),bd=8).pack()


result_text=Text(right_frame,bd=5,width=28,height=19,bg="white")
result_text.place(x=100,y=80)

Label(left_frame,text="Enter the number",width=30,font=("",22,"bold"),bd=8).pack()


                #variable define*****************************************************variable**************************

var=StringVar()


#enetry box
e=Entry(left_frame,bd=10,textvariable=var)
e.place(x=100,y=100,width=200,height=40)

#fuction define

def mul ():
    print("hello")
    result_text.delete(1.0,END)
    m=var.get()
    print(m)
    if m.isdigit():
        m=int(m)
        for i in range (1,11):  
            result_text.insert(END,m,'\t',"x",'\t',i,'\t',"=",'\t',(m*i))
            result_text.insert(END,"\n")
            result_text.insert(END,"\n")
def reset():
    if messagebox.askyesno('multiplication','Are you want to Resert '):
        result_text.delete(1.0,END)
        var=set("")
def exit():
    if messagebox.askyesno('multiplication','Are you want to Exit '):
        win.destroy()
    else:
        result_text.delete(1.0,END)
        var=set("")
        


# button
b1=Button(left_frame,text="Multiplication", fg="black",command=mul)
b1.place(x=120,y=200,width=150,height=40)

b2=Button(left_frame,text="Resert",command=reset)
b2.place(x=120,y=250,width=150,height=40)

b3=Button(left_frame,text="Exit",command=exit)
b3.place(x=120,y=300,width=150,height=40)

#***************************************************************************ENd frame******************************************************************

























win.mainloop()