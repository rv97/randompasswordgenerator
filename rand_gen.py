import random
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import pyperclip
import string


WEAK = string.ascii_lowercase
MED = string.ascii_letters+string.digits
STRONG = MED+string.punctuation

def generate_password(len, type):
    password = ""
    if type == 0:
        for i in range(len):
            password = password + random.choice(WEAK)
        return password

    elif type == 1:
        for i in range(len):
            password = password + random.choice(MED)
        return password
    
    else:
        for i in range(len):
            password = password + random.choice(STRONG)
        return password

def onGeneratePress():
    generated_password = generate_password(combo_var.get(), radio_var.get())
    pyperclip.copy(generated_password)
    messagebox.showinfo("Generated Password", "Your secret key is "+generated_password+" It has been copied to clipboard.")

window = Tk()
window.title("Random Password Generator")

radio_var = IntVar()
combo_var = IntVar()

#Creating the top frame

length_label = Label(window, text="Length")
length_label.grid(row=0, column=0)

length_combo = Combobox(window, textvariable=combo_var)
length_combo['values'] = (8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32)
length_combo.current(0)
length_combo.grid(row=0, column=1)

radio_low = Radiobutton(window, variable=radio_var, text="Weak", value=0)
radio_low.grid(row=0, column=2)
radio_med = Radiobutton(window, variable=radio_var, text="Medium", value=1)
radio_med.grid(row=0, column=3)
radio_strong = Radiobutton(window, variable=radio_var, text="Strong", value=2)
radio_strong.grid(row=0, column=4)

#Creating the generate button

generate_button = Button(window, text="Generate", command=onGeneratePress)
generate_button.grid(row=1, column=1, columnspan=2)
window.mainloop()