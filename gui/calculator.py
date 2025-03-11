import tkinter as tk 
app = tk.Tk()
app.title("Calculator")
app.geometry("290x300")
input = tk.Entry(app, font=("Arial", 16))
input.grid(row=0, column=0, columnspan=4, padx=30, pady=5)
def get_input(value):
    input.insert("end", value)
def equal_value():
    previous_value = input.get()
    result = eval(previous_value)
    input.delete(0, "end")
    input.insert("end", result)
zero = tk.Button(app,text="0", font=("Arial", 16), width=3, height=1,command=lambda: get_input(0))
one = tk.Button(app,text="1", font=("Arial", 16), width=3, height=1,command=lambda: get_input(1))
two = tk.Button(app,text="2", font=("Arial", 16), width=3, height=1,command=lambda: get_input(2))
three = tk.Button(app,text="3", font=("Arial", 16), width=3, height=1,command=lambda: get_input(3))
four = tk.Button(app,text="4", font=("Arial", 16), width=3, height=1,command=lambda: get_input(4))
five = tk.Button(app,text="5", font=("Arial", 16), width=3, height=1,command=lambda: get_input(5))
six = tk.Button(app,text="6", font=("Arial", 16), width=3, height=1,command=lambda: get_input(6))
seven = tk.Button(app,text="7", font=("Arial", 16), width=3, height=1,command=lambda: get_input(7))
eight = tk.Button(app,text="8", font=("Arial", 16), width=3, height=1,command=lambda: get_input(8))
nine = tk.Button(app,text="9", font=("Arial", 16), width=3, height=1,command=lambda: get_input(9))
plus = tk.Button(app,text="+", font=("Arial", 16), width=3, height=1,command=lambda: get_input("+"))
minus = tk.Button(app,text="-", font=("Arial", 16), width=3, height=1,command=lambda: get_input("-"))
multiply = tk.Button(app,text="*", font=("Arial", 16), width=3, height=1,command=lambda: get_input("*"))
divide = tk.Button(app,text="/", font=("Arial", 16), width=3, height=1,command=lambda: get_input("/"))
equal = tk.Button(app,text="=", font=("Arial", 16), width=3, height=1,command=equal_value)
clear = tk.Button(app,text="C", font=("Arial", 16), width=3, height=1)

seven.grid(row=1, column=0, padx=5, pady=5)
eight.grid(row=1, column=1, padx=5, pady=5)
nine.grid(row=1, column=2, padx=5, pady=5)
divide.grid(row=1, column=3, padx=5, pady=5)
four.grid(row=2, column=0, padx=5, pady=5)
five.grid(row=2, column=1, padx=5, pady=5)
six.grid(row=2, column=2, padx=5, pady=5)
multiply.grid(row=2, column=3, padx=5, pady=5)
one.grid(row=3, column=0, padx=5, pady=5)
two.grid(row=3, column=1, padx=5, pady=5)
three.grid(row=3, column=2, padx=5, pady=5)
minus.grid(row=3, column=3, padx=5, pady=5)
zero.grid(row=4, column=0, padx=5, pady=5)
clear.grid(row=4, column=1, padx=5, pady=5)
equal.grid(row=4, column=2, padx=5, pady=5)
plus.grid(row=4, column=3, padx=5, pady=5)

app.mainloop()


# list =[
#     [45,67,87],
#     [870,62,14]
# ]