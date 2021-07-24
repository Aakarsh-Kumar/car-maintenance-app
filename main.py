from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Car Maintenance App")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

miles = StringVar()
miles_entry = ttk.Entry(mainframe, width=7, textvariable=miles)
miles_entry.grid(column=2, row=1, sticky=(W, E))

miles_entry.configure()

root.mainloop()