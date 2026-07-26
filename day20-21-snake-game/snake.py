# Snake body parts
from turtle import Turtle

MOVING_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow_snake(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].position())
        self.segments.append(new_segment)

    def is_collision_with_tail(self):
        for segment in self.segments[1:]:
            if segment == self.head:
                continue
            if self.head.distance(segment) < 10:
                return True
        return False

    def is_collision_with_wall(self):
        return (
            self.head.xcor() > 280
            or self.head.xcor() < -280
            or self.head.ycor() > 280
            or self.head.ycor() < -280
        )


# slicing the list
piano_keys = ["A", "B", "C", "D", "E", "F", "G"]
# print(piano_keys[1:])
# print(piano_keys[1:-1])
# print(piano_keys[:-1])
# print(piano_keys[1:])
# print(piano_keys[1:])
print(piano_keys[::-1])
print(piano_keys[2:5])
