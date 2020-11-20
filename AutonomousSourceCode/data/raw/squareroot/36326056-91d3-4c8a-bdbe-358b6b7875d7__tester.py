import tkinter as Tk

from functools import partial

def square(x):
    return x*x

def compute():
    value = var.get()
    result = square(value)
    list_of_results.append(result)

root = Tk.Tk()
var = Tk.IntVar(root, value=0) #the variable the gets passed to the class call
menu = Tk.OptionMenu(root, var, *[0,1,2,3,4,5]) #a drop-down list to choose a value for the variable
menu.pack()
list_of_results=[]
button = Tk.Button(root, text='click', command = compute) #a button that calls the class
button.pack()
root.mainloop()