from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate():
    entry_password.delete(0, END)

    password_letters = [random.choice(letters) for i in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for i in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for i in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    entry_password.insert(END, string=f'{password}')
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Ooops...', message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \n'
                                                        f'Email: {email} \nPassword: {password}\n Is it ok to save?')
        if is_ok:
            with open('passwords.txt', 'a') as password_data:
                password_data.write(f'{website} | {email} | {password}\n')
                entry_website.delete(0, END)
                entry_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=0, row=0, columnspan=3)

# Label
website_label = Label(text="Website", font=('Arial', 8, 'normal'))
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username", font=('Arial', 8, 'normal'))
email_label.grid(column=0, row=2)
password_label = Label(text="Password", font=('Arial', 8, 'normal'))
password_label.grid(column=0, row=3)

# Entry
entry_website = Entry(width=51)
entry_website.grid(column=1, row=1, columnspan=2)
entry_website.focus()
entry_email = Entry(width=51)
entry_email.grid(column=1, row=2, columnspan=2)
entry_email.insert(0, "youremail@gmail.com")
entry_password = Entry(width=32)
entry_password.grid(column=1, row=3, columnspan=1)

# Button
password_button = Button(text="Generate Password", command=generate)
password_button.grid(column=2, row=3, columnspan=1)
add_button = Button(text="Add", command=add, width=43)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
