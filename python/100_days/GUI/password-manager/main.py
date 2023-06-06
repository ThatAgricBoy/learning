from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip3
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbol = [choice(symbols) for _ in range(randint(2, 5))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 5))]

    password_list = password_letters + password_numbers + password_symbol
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip3.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="You can't leave any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                      f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:

            entry = f"Website: {website}\nEmail: {email}\nPassword: {password}\n\n"
            with open("data.txt", "a") as f:
                f.write(entry)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", fg="black")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_label = Label(text="Email/Username:", fg="black")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.insert(0, "samueljohn3999@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:", fg="black")
password_label.grid(column=0, row=3)
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()