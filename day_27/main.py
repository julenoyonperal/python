from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("WidgMile to Km Converter")
window.minsize(width=200, height=100)

#Buttons
def action():
    miles = float(miles_input.get())
    km = int(miles)/1.6
    km_result.config(text=str(km))
    return(km)


miles_input = Entry(width=30)
miles_input.grid(column=1,row=0)

miles_label = Label(text="miles")
miles_label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

km_result = Label(text="0")
km_result.grid(column=3,row=0)

button = Button(text="Calculate", command=action)
button.grid(column=3,row=2)


window.mainloop()