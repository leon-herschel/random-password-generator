import random
from tkinter import *
from tkinter import messagebox
import clipboard


def shuffle(string):
    temp_list = list(string)
    random.shuffle(temp_list)
    return ''.join(temp_list)


def random_char(start, end):
    return chr(random.randint(start, end))


def generate_password():
    uppercase = [random_char(65, 90) for i in range(2)]
    lowercase = [random_char(97, 122) for i in range(2)]
    digits = [random_char(48, 57) for i in range(2)]
    punctuation = [random_char(33, 38) for i in range(2)]

    password = ''.join(uppercase + lowercase + digits + punctuation)
    output.set(shuffle(password))


def copy():
    text = output.get()
    if text:
        clipboard.copy(text)
        messagebox.showinfo("Success", "Password copied to clipboard.")
    else:
        messagebox.showerror("Error", "No password to copy.")


root = Tk()
root.geometry("250x200")
root.resizable(0, 0)
root.title("Random Password Generator")

output = StringVar()
output.set("")

Label(root, textvariable=output, font='arial 20').place(x=60, y=30)

Button(root, text="GENERATE", font='arial 15', command=generate_password).place(x=60, y=80)
Button(root, text="COPY", font='arial 15', command=copy).place(x=80, y=125)

root.mainloop()
