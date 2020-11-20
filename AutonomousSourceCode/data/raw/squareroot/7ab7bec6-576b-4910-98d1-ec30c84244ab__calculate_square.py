#	calculate_square.py

from Tkinter import *
import ttk

def calculate_square(*args):
	value_in = float(number_in.get())
	number_out.set(value_in * value_in)

root = Tk()
root.title('Calculate square')

mainframe = ttk.Frame(root)
mainframe.grid(column=1, row=1, sticky=(N, E, S, W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

number_in = StringVar()
number_out = StringVar()

square_of_string_label = ttk.Label(mainframe, text='The square of')
square_of_string_label.grid(column=1, row=1, sticky=E)

number_in_entry = ttk.Entry(mainframe, width=5, textvariable=number_in)
number_in_entry.grid(column=2, row=1, sticky=(E, W))

is_string_label = ttk.Label(mainframe, text='is')
is_string_label.grid(column=1, row=2, sticky=E)

number_out_label = ttk.Label(mainframe, textvariable=number_out)
number_out_label.grid(column=2, row=2, sticky=W)

go_button = ttk.Button(mainframe, text='Go!', command=calculate_square)
go_button.grid(column=2, row=3, sticky=W)

for child in mainframe.winfo_children():
	child.grid_configure(padx=2, pady=2)

number_in_entry.focus()
root.bind('<Return>', calculate_square)

root.mainloop()
