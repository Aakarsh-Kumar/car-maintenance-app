from tkinter import *
from tkinter import ttk

#initializing root window
root = Tk()
root.title("Car Maintenance App")

#creating container for widgets
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#widgets
milesLabel = ttk.Label(mainframe, text= "Enter your cars current mileage:")
lastmilesLabel = ttk.Label(mainframe, text= "How many miles was your last oil change at?")

miles_entry = ttk.Entry(mainframe, width=7 )
lastmiles_entry = ttk.Entry(mainframe, width=7)

milesButton = ttk.Button(mainframe, text="Enter")

#positioning
milesLabel.grid(row=1, column=0)
miles_entry.grid(row=1, column=1)
milesButton.grid(row=1, column=2)
lastmilesLabel.grid(row=0, column=0)
lastmiles_entry.grid(row=0, column=1)

root.mainloop()




