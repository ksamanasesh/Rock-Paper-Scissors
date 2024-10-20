import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    
    try:
        length = int(length_entry.get()) 
    except Exception as e:
        messagebox.showwarning("Input Error", "Please enter the numeric value.")
    
    char_types = character_type_var.get()
    
    characters = ""
    
    if char_types == "Lowercase + Uppercase":
        characters = string.ascii_lowercase + string.ascii_uppercase
    elif char_types == "Lowercase + Uppercase + Numbers":
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif char_types == "Lowercase + Uppercase + Numbers + Symbols":
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

    if not characters:
        messagebox.showwarning("Selection Error", "Please select valid character types.")
        return
    
    password = ''.join(random.choice(characters) for _ in range(length))

    password_entry.config(state=tk.NORMAL)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#d3e4f2")  

length_label = tk.Label(root, text="Password Length:", bg="#d3e4f2")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

character_type_label = tk.Label(root, text="Character Types:", bg="#d3e4f2")
character_type_label.grid(row=1, column=0, padx=10, pady=10)

character_type_var = tk.StringVar()
character_type_var.set("Lowercase + Uppercase")  # Default selection

character_type_menu = tk.OptionMenu(root, character_type_var,
                                    "Lowercase + Uppercase",
                                    "Lowercase + Uppercase + Numbers",
                                    "Lowercase + Uppercase + Numbers + Symbols")
character_type_menu.grid(row=1, column=1, padx=10, pady=10)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="#85c1e9", fg="black")
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

password_label = tk.Label(root, text="Generated Password:", bg="#d3e4f2")
password_label.grid(row=3, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, state=tk.DISABLED, width=35)
password_entry.grid(row=3, column=1, padx=10, pady=10)

root.mainloop()
