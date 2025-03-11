# import tkinter as tk

# app = tk.Tk()
# app.title("My App")
# app.geometry("400x400")

# result = tk.Label(app, text="Result")
# result.pack()

# def say_hello():
#     result.config(text="Welcome to my GUI app")


# button = tk.Button(app, text="Click me", command=say_hello)
# button.pack()
# app.mainloop()


import tkinter as tk
app = tk.Tk()
app.title("My App")
app.geometry("400x400")
flable = tk.Label(app,text="Enter first number")
flable.pack()
num1 = tk.Entry()
num1.pack()

result = tk.Label(app, text="Result")
result.pack()
def add():
    n1 = int(num1.get())
    
    result.config(text=f"{n1}")
button = tk.Button(app, text="Show", command=add)
button.pack()
app.mainloop()