# ? Advanced Functions and Arguments

import tkinter as tk


# *args is a tuple of arguments - unlimited arguments
def add(*args):
    return sum(args)


print(add(1, 2, 3, 4, 5))


# **kwargs is a dictionary of arguments - unlimited keyword arguments
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)

window = tk.Tk()
window.title("My GUI App")
window.geometry("300x200")
window.mainloop()


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.model)
print(my_car.color)
print(my_car.seats)
