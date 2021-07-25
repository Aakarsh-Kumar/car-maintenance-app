from tkinter import *
from tkinter import ttk




#initializing root window
root = Tk()
root.title("Car Maintenance App")

#functions
miles = IntVar()
last_miles = IntVar()
miles_between_changes = 3000

def check_oil_change():
    miles = miles_entry.get()
    miles = int(miles)
    last_miles = lastmiles_entry.get()
    last_miles = int(last_miles)
    miles_till_oilchange = miles_between_changes - (miles - last_miles)
    if miles_till_oilchange == 0:
        outputLabel.config(text="You are due for an oil change")
    if miles_till_oilchange > 0:
        outputLabel.config(text="You have {} miles until next oil change.".format(miles_till_oilchange))
    if miles_till_oilchange < 0:
        outputLabel.config(text="You are over due {} miles for an oil change.".format(abs(miles_till_oilchange)))



#creating container for widgets
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#widgets
milesLabel = ttk.Label(mainframe, text= "Enter your cars current mileage:")
lastmilesLabel = ttk.Label(mainframe, text= "How many miles was your last oil change at?")

miles_entry = ttk.Entry(mainframe, width=7)
lastmiles_entry = ttk.Entry(mainframe, width=7)

milesButton = ttk.Button(mainframe, text="Enter", command=check_oil_change)

outputLabel = ttk.Label(mainframe, text="")


#positioning
milesLabel.grid(row=1, column=0)
miles_entry.grid(row=1, column=1)
milesButton.grid(row=1, column=2)
lastmilesLabel.grid(row=0, column=0)
lastmiles_entry.grid(row=0, column=1)
outputLabel.grid(row=2, column=1)



root.mainloop()




