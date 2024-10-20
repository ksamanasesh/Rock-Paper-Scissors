import tkinter as tk
from tkinter import messagebox

def button_click(value):
    current = input_num.get()
    input_num.delete(0, tk.END)
    input_num.insert(0, current + str(value))

def button_clear():
    input_num.delete(0, tk.END)

def button_equal():
    try:
        result = eval(input_num.get())
        input_num.delete(0, tk.END)
        input_num.insert(0, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

window = tk.Tk()
window.title("Calculator")

window.configure(bg="lightgray")

input_num = tk.Entry(window, width=65, borderwidth=5)
input_num.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

button_color = "lightblue"
text_color = "black"

button_1 = tk.Button(window, text="1", padx=30, pady=30, command=lambda: button_click(1), bg=button_color, fg=text_color)
button_2 = tk.Button(window, text="2", padx=30, pady=30, command=lambda: button_click(2), bg=button_color, fg=text_color)
button_3 = tk.Button(window, text="3", padx=30, pady=30, command=lambda: button_click(3), bg=button_color, fg=text_color)
button_4 = tk.Button(window, text="4", padx=30, pady=30, command=lambda: button_click(4), bg=button_color, fg=text_color)
button_5 = tk.Button(window, text="5", padx=30, pady=30, command=lambda: button_click(5), bg=button_color, fg=text_color)
button_6 = tk.Button(window, text="6", padx=30, pady=30, command=lambda: button_click(6), bg=button_color, fg=text_color)
button_7 = tk.Button(window, text="7", padx=30, pady=30, command=lambda: button_click(7), bg=button_color, fg=text_color)
button_8 = tk.Button(window, text="8", padx=30, pady=30, command=lambda: button_click(8), bg=button_color, fg=text_color)
button_9 = tk.Button(window, text="9", padx=30, pady=30, command=lambda: button_click(9), bg=button_color, fg=text_color)
button_0 = tk.Button(window, text="0", padx=30, pady=30, command=lambda: button_click(0), bg=button_color, fg=text_color)

button_add = tk.Button(window, text="+", padx=30, pady=30, command=lambda: button_click("+"), bg=button_color, fg=text_color)
button_subtract = tk.Button(window, text="-", padx=30, pady=30, command=lambda: button_click("-"), bg=button_color, fg=text_color)
button_multiply = tk.Button(window, text="*", padx=30, pady=30, command=lambda: button_click("*"), bg=button_color, fg=text_color)
button_divide = tk.Button(window, text="/", padx=30, pady=30, command=lambda: button_click("/"), bg=button_color, fg=text_color)

button_equal = tk.Button(window, text="=", padx=70, pady=30, command=button_equal, bg=button_color, fg=text_color)
button_clear = tk.Button(window, text="C", padx=70, pady=30, command=button_clear, bg=button_color, fg=text_color)

button_7.grid(row=1, column=0, padx=5, pady=5)
button_4.grid(row=2, column=0, padx=5, pady=5)
button_1.grid(row=3, column=0, padx=5, pady=5)
button_0.grid(row=4, column=0, padx=5, pady=5)

button_8.grid(row=1, column=1, padx=5, pady=5)
button_5.grid(row=2, column=1, padx=5, pady=5)
button_2.grid(row=3, column=1, padx=5, pady=5)
button_clear.grid(row=4, column=1, padx=5, pady=5)

button_9.grid(row=1, column=2, padx=5, pady=5)
button_6.grid(row=2, column=2, padx=5, pady=5)
button_3.grid(row=3, column=2, padx=5, pady=5)
button_equal.grid(row=4, column=2, padx=5, pady=5)

button_divide.grid(row=1, column=3, padx=5, pady=5)
button_multiply.grid(row=2, column=3, padx=5, pady=5)
button_subtract.grid(row=3, column=3, padx=5, pady=5)
button_add.grid(row=4, column=3, padx=5, pady=5)

window.mainloop()
