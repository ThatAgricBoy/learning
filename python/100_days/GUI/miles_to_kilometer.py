from tkinter import *


def miles_to_kilometer():
    miles = float(input.get())
    km = miles * 1.6
    label3.config(text=km)

window = Tk()
window.title("Miles to Kilometer")
window.minsize(width=300, height=100)
window.config(padx=60, pady=30)

input = Entry(width=15)
print(input.get())
input.grid(column=1, row=0)

#Labels
label1 = Label(text="Miles", font=("Arial,", 24))
label1.grid(column=2, row=0)
label1.config(padx=20, pady=20)

label2 = Label(text="is equal to", font=("Arial,", 24))
label2.grid(column=0, row=1)

label3= Label(text="0", font=("Arial,", 24))
label3.grid(column=1, row=1)
label3.config(padx=20, pady=20)

my_label = Label(font=("Arial,", 24, "bold"))
my_label.config(text="km")
my_label.grid(column=2, row=1)

button = Button(text="Calculate", command=miles_to_kilometer)
button.grid(column=1, row=2)
button.config(padx=20, pady=20)


window.mainloop()
