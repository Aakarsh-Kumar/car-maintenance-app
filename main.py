from tkinter import *
from tkinter import ttk




#initializing root window
root = Tk()
root.title("Car Maintenance App")
root.resizable(False, False)
tab_control = ttk.Notebook(root)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text="History")
tab_control.add(tab2, text="Check maintenance")
tab_control.grid(row=0, column=6)

#functions
miles = IntVar()
last_miles = IntVar()
miles_between_changes = 3000

def check_oil_change():
    miles = miles_entry.get()
    miles = int(miles)
    last_miles = last_miles_entry.get()
    last_miles = int(last_miles)
    miles_till_oilchange = miles_between_changes - (miles - last_miles)
    if miles_till_oilchange == 0:
        output_label.config(text="You are due for an oil change")
    if miles_till_oilchange > 0:
        output_label.config(text="You have {} miles until next oil change.".format(miles_till_oilchange))
    if miles_till_oilchange < 0:
        output_label.config(text="You are over due {} miles for an oil change.".format(abs(miles_till_oilchange)))

#tab1 widgets
last_miles_label = ttk.Label(tab1, text= "How many miles was your last oil change at?")
last_miles_entry = ttk.Entry(tab1, width=7)
#tab1 positioning
last_miles_label.grid(row=0, column=0)
last_miles_entry.grid(row=0, column=1)

#tab2 widgets
miles_label = ttk.Label(tab2, text= "Enter your cars current mileage:")
miles_entry = ttk.Entry(tab2, width=7)
miles_button = ttk.Button(tab2, text="Enter", command=check_oil_change)
output_label = ttk.Label(tab2, text="")
#tab2 positioning
miles_label.grid(row=1, column=0)
miles_entry.grid(row=1, column=1)
miles_button.grid(row=1, column=2)
output_label.grid(row=2, column=1)

root.mainloop()




