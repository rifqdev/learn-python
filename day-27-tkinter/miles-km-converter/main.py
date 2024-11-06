from tkinter import *

def miles_to_km():
    miles = float(input_miles.get())
    km = round(miles * 1.609)
    result_label.config(text=km)

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=50, pady=20)

input_miles = Entry(width=10)
input_miles.grid(column=2, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=3, row=0)

equals_label = Label(text="is equal to")
equals_label.grid(column=1, row=1)

result_label = Label(text="0")
result_label.grid(column=2, row=1)

km_label = Label(text="Km")
km_label.grid(column=3, row=1)

button = Button(text="Calculate", command=miles_to_km)
button.grid(column=2, row=2)


window.mainloop()