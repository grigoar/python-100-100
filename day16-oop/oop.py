class Turtle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving")

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

    def shape(self, shape):
        self._shape = shape
        print(f"{self.name} shape set to {shape}")

    def color(self, color):
        self._color = color
        print(f"{self.name} color set to {color}")

    def forward(self, distance):
        print(f"{self.name} moves forward {distance}")

    def right(self, angle):
        print(f"{self.name} turns right {angle} degrees")

    def left(self, angle):
        print(f"{self.name} turns left {angle} degrees")

    def backward(self, distance):
        print(f"{self.name} moves backward {distance}")

    def penup(self):
        print(f"{self.name} pen up")

    def pendown(self):
        print(f"{self.name} pen down")

    def goto(self, x, y):
        print(f"{self.name} goes to ({x}, {y})")

    def setheading(self, heading):
        print(f"{self.name} heading set to {heading}")

    def __str__(self):
        return f"Turtle(name={self.name})"
