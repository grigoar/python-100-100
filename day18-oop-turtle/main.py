# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("blue")
# timmy_the_turtle.forward(1000)
# tim = Turtle()
# screen = Screen()
# screen.exitonclick()
# import heroes
# print(heroes.gen())

# tim = Turtle()


# color_list = [
#     "red",
#     "green",
#     "blue",
#     "yellow",
#     "purple",
#     "orange",
#     "pink",
#     "brown",
#     "gray",
#     "black",
# ]


# # ? draw different shapes
# def draw_shape(num_sides):
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(360 / num_sides)


# for shape_side_n in range(3, 10):
#     tim.color(random.choice(color_list))
#     draw_shape(shape_side_n)

# screen = Screen()
# screen.exitonclick()

# ? random walk
# import random
# from turtle import Screen, Turtle

# tim = Turtle()
# color_list = [
#     "red",
#     "green",
#     "blue",
#     "yellow",
#     "purple",
#     "orange",
#     "pink",
#     "brown",
#     "gray",
#     "black",
# ]
# direction_list = [0, 90, 180, 270]

# tim.pensize(10)
# tim.speed("fastest")

# for _ in range(200):
#     tim.forward(20)
#     tim.right(random.choice(direction_list))
#     tim.color(random.choice(color_list))

# screen = Screen()
# screen.exitonclick()

# ? draw dots
import random
from turtle import Screen, Turtle

tim = Turtle()
color_list = [
    "red",
    "green",
    "blue",
    "yellow",
    "purple",
    "orange",
    "pink",
    "brown",
    "gray",
    "black",
]
# tim.pensize(20)
tim.speed("fastest")
tim.penup()
tim.hideturtle()
# tim.dot(20, random.choice(color_list))
# tim.dot(0, random.choice(color_list))
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()
