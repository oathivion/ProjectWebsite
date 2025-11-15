from doctest import debug
from math import sqrt
import tkinter as tk
from token import NUMBER




def calc_add() :
    n1 = float(number1.get())
    n2 = float(number2.get())
    result.set(n1+n2)

def calc_subtract():
    n1 = float(number1.get())
    n2 = float(number2.get())
    result.set(n1-n2)

def calc_multiply() :
    n1 = float(number1.get())
    n2 = float(number2.get())
    result.set(n1*n2)

def calc_devide(): 
    n1 = float(number1.get())
    n2 = float(number2.get())
    if n2 == 0:
        result.set("Please")
    if n2 != 0:
        result.set(n1/n2)
def calc_sqrt():
    n1 = float(number1.get())
    result.set(sqrt(n1))

    
    

window = tk.Tk()
window.title("Simple Calculator")

tk.Label(window, text="Number 1").grid(row=0, column=0, padx=6, pady=6, sticky="e")
number1 = tk.Entry(window, width=15)
number1.grid(row=0, column=1, padx=6, pady=6)

tk.Label(window, text="Number 2").grid(row=1, column=0, padx=6, pady=6, sticky="e")
number2 = tk.Entry(window, width=15)
number2.grid(row=1, column=1, padx=6, pady=6)

tk.Button(window, text="Add",      width=50, command=calc_add).grid(row=2, column=0, padx=6, pady=6)
tk.Button(window, text="Subtract", width=50, command=calc_subtract).grid(row=2, column=1, padx=6, pady=6)
tk.Button(window, text="Multiply", width=50, command=calc_multiply).grid(row=3, column=0, padx=6, pady=6)
tk.Button(window, text="Divide",   width=50, command=calc_devide).grid(row=3, column=1, padx=6, pady=6)
tk.Button(window, text="Square Root", width=50, command=calc_sqrt).grid(row=4, column=0, padx=6, pady=6)

result = tk.StringVar(value="")
tk.Label(window, text="Result").grid(row=6, column=0, padx=6, pady=6, sticky="e")
tk.Label(window, textvariable=result).grid(row=6, column=1, padx=6, pady=6, sticky="w")

window.mainloop()

