from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
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

generate_button = Button(text="Generate Password")
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()