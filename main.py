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
tab_control.pack(expand=1, fill="both")

#functions
miles = IntVar()
last_miles = IntVar()
miles_between_oil_changes = 3000

def check_oil_change():
    miles = miles_entry.get()
    miles = int(miles)
    last_miles = last_miles_entry.get()
    last_miles = int(last_miles)
    miles_till_oilchange = miles_between_oil_changes - (miles - last_miles)
    if miles_till_oilchange == 0:
        output_label.config(text="You are due for an oil change")
    if miles_till_oilchange > 0:
        output_label.config(text="You have {} miles until next oil change.".format(miles_till_oilchange))
    if miles_till_oilchange < 0:
        output_label.config(text="You are over due {} miles for an oil change.".format(abs(miles_till_oilchange)))

#tab1 widgets
maintenance_history_choices = [  #drop down menu options
    "Update Oil Change",
    "Update Tire Rotation",
    "Update Spark Plugs",
]
clicked = StringVar()
clicked.set( "Update" )
maintenance_history_choices_dropdown = OptionMenu(tab1, clicked, *maintenance_history_choices)
last_miles_label = ttk.Label(tab1, text= "How many miles was your last oil change at?")
last_miles_entry = ttk.Entry(tab1, width=7)
history_msg = StringVar()
history_msg.set("Oil change: {} \nTire Rotation: {} \nSpark Plugs: {}".format("?","?","?"))
maintenance_history_message = Message(tab1, textvariable=history_msg, relief=RAISED)
#tab1 positioning
maintenance_history_choices_dropdown.grid(row=0, column=0, sticky="W")
last_miles_label.grid(row=1, column=0)
last_miles_entry.grid(row=1, column=1)
maintenance_history_message.grid(row=2, column=0, sticky="W")
#tab2 widgets
miles_label = ttk.Label(tab2, text= "Enter your cars current mileage:")
miles_entry = ttk.Entry(tab2, width=7)
miles_button = ttk.Button(tab2, text="Enter", command=check_oil_change)
output_label = ttk.Label(tab2, text="")
maintenance_choices = [  #drop down menu options
    "Check Oil Change",
    "Check Tire Rotation",
    "Check Spark Plugs",
]
clicked = StringVar()
clicked.set( "Check" )
maintenance_choices_dropdown = OptionMenu(tab2, clicked, *maintenance_choices)
#tab2 positioning
maintenance_choices_dropdown.grid(row=0, column=0, sticky="W")
miles_label.grid(row=1, column=0)
miles_entry.grid(row=1, column=1)
miles_button.grid(row=1, column=2)
output_label.grid(row=2, column=1)


root.mainloop()




