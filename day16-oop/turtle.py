# turtle.py

from oop import Turtle
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Pokemon Name", "Type"]
table.add_row(["Pikachu", "Electric"])
table.add_row(["Charmander", "Fire"])
table.add_row(["Squirtle", "Water"])
table.add_column("HP", [100, 100, 100])
table.add_column("Speed", [100, 100, 100])
table.add_column("Attack", [100, 100, 100])
table.add_column("Defense", [100, 100, 100])
table.add_column("Special Attack", [100, 100, 100])
table.add_column("Special Defense", [100, 100, 100])
table.add_column("Total", [100, 100, 100])
print(table)


turtle = Turtle("turtle")
turtle.move()
turtle.eat()
turtle.sleep()
turtle.shape("turtle")
turtle.color("red")
turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.left(90)
turtle.backward(100)

print(turtle)
