from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

EMAIL = "email@gmail.com"


def save():
    websites = w_entry.get()
    mail = em_entry.get()
    passwords = pass_entry.get()

    details = {
        websites: {
            "Email/Username": mail,
            "Password": passwords,
        }
    }
    if len(websites) == 0 or len(mail) == 0 or len(passwords) == 0:
        messagebox.showinfo(title="OOPS", message="Please don't leave any part.")

    else:
        is_ok = messagebox.askokcancel(title=websites,
                                       message=f"These are the details:\nEmail / Username: {mail}\n"
                                               f"Password : {passwords}\n\nDo you want to save?")
        if is_ok:
            try:
                with open("password.json", "r") as data_file:
                    data = json.load(data_file)
            except JSONDecodeError:
                with open("password.json", "w") as data_file:
                    json.dump(details, data_file, indent=4)
            else:
                data.update(details)
                with open("password.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                w_entry.delete(0, END)
                pass_entry.delete(0, END)


def find_password():
    search_site = w_entry.get()

    try:
        with open("password.json", "r") as query_file:
            queries = json.load(query_file)
            print(queries)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="Nothing can be found")

    else:
        for websites in queries.keys():
            if search_site != websites:
                messagebox.showinfo(title="ERROR", message=f"{search_site} cannot be found!")
                break
            elif search_site == websites:
                queried = queries[search_site]
                q_mail = queried["Email/Username"]
                q_password = queried["Password"]
                messagebox.showinfo(title=search_site, message=f"EMAIL: {q_mail}\nPASSWORD: {q_password}")
                break

    finally:
        w_entry.delete(0, END)


def password_generator():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password1 = "".join(password_list)

    pass_entry.insert(0, password1)
    pyperclip.copy(password1)


screen = Tk()
screen.title("Password Manager")
screen.config(pady=40, padx=40)

canvas = Canvas(width=200, height=224, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo)
canvas.grid(column=1, row=0)

website = Label(text="Website :")
website.config(pady=15)
website.grid(column=0, row=1)

w_entry = Entry(width=35)
w_entry.focus()
w_entry.grid(column=1, row=1)

search_entry = Button(text="Search", width=18, command=find_password)
search_entry.grid(column=2, row=1, columnspan=2)

mail_user = Label(text="Email / Username :")
mail_user.config(pady=15)
mail_user.grid(column=0, row=2)

password = Label(text="Password :")
password.config(pady=15)
password.grid(column=0, row=3)

em_entry = Entry(width=58)
em_entry.insert(0, EMAIL)
em_entry.grid(column=1, row=2, columnspan=2)

pass_entry = Entry(width=34)
pass_entry.grid(column=1, row=3)

gen_pass = Button(text="Generate Password", highlightthickness=0, width=19, command=password_generator)
gen_pass.grid(column=2, row=3)

add_button = Button(text="Add", width=49, command=save)
add_button.config(pady=5)
add_button.grid(column=1, row=4, columnspan=2)

screen.mainloop()
