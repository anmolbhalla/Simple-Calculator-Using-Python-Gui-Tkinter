from tkinter import *
import tkinter.messagebox
root=Tk()
var=IntVar()
var1=IntVar()
var2=IntVar()
var3=IntVar()
first=Label(root,text='Enter number')
second=Label(root,text='Second')
first.grid(row=0,sticky=E)
second.grid(row=1,sticky=E)
number1=Entry(root)
number2=Entry(root)
number1.grid(row=0,column=1)
number2.grid(row=1,column=1)
add=Checkbutton(text='ADD',variable=var, onvalue=1, offvalue=0)
sub=Checkbutton(text='Subtract',variable=var1, onvalue=1, offvalue=0)
mul=Checkbutton(text='Multiply',variable=var2, onvalue=1, offvalue=0)
div=Checkbutton(text='Divide', variable=var3,onvalue=1, offvalue=0)
add.grid(row=3,column=0,sticky=W)
sub.grid(row=3,column=1,sticky=W)
mul.grid(row=4,column=0,sticky=W)
div.grid(row=4,column=1,sticky=W)
result=Button(root,text='Result')
result.grid(row=5,columnspan=2)
def quit():
    root.quit()
def reset():
    global new, new1
    number1.delete(0,END)
    number2.delete(0,END)
    new.destroy()
    new1.grid_remove()
    var.set(0)
    var1.set(0)
    var2.set(0)
    var3.set(0)
def addbox(event):
    global new,new1
    new = Label(root, text='New')
    new.grid(row=2)
    new1 = Entry(root)
    new1.grid(row=2, column=1)
    c = number1.get()
    d = number2.get()
    if ((c == '' or d == '') or (var.get() == 1 and var1.get() == 1) or (var.get() == 1 and var2.get() == 1) or (
            var.get() == 1 and var3.get() == 1) or (var1.get() == 1 and var2.get() == 1) or (
            var1.get() == 1 and var3.get() == 1) or (var2.get() == 1 and var3.get() == 1)):
        tkinter.messagebox.showerror('Result', 'Error')
    else:
        a = int(c)
        b = int(d)
        if (var.get() == 1):
            new1.insert(0, str(a + b))
        elif (var1.get() == 1):
            new1.insert(0, str(a - b))
        elif (var2.get() == 1):
            new1.insert(0, str(a * b))
        elif (var3.get() == 1):
            new1.insert(0, str(a / b))
        counter=1
result.bind('<ButtonRelease-1>',addbox)
menu=Menu(root)
root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label='Options',menu=submenu)
submenu.add_command(label='Reset', command=reset)
submenu.add_command(label='Quit',command=quit)
root.mainloop()
