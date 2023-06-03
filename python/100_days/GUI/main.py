from tkinter import Tk, Button, Label, Entry



# Using Buttons
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


# Using the Entry Class
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

# Using labels
my_label = Label(text="I am a label", font=("Arial,", 24, "bold"))
my_label.config(text="New One")
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

button = Button(text="Click ME Now", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=30, pady=30)

New_button = Button(text="Click ME")
New_button.grid(column=2, row=0)
New_button.config(padx=10, pady=10)

# Using the Entry Class
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()
