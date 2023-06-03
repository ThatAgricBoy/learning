from tkinter import Tk, Button, Label, Entry
window = Tk()
window.title("First GUI")
window.minsize(width=500, height=300)

# Using labels
my_label = Label(text="I am a label", font=("Arial,", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New One")

# Using Buttons
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click ME Now", command=button_clicked)
button.pack()

# Using the Entry Class
input = Entry()
input.pack()



window.mainloop()