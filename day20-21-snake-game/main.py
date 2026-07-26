import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    snake.move()
    time.sleep(0.1)

    screen.update()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow_snake()
        scoreboard.increase_score()

    if snake.is_collision_with_wall():
        game_is_on = False
        scoreboard.game_over()

    # Check for collision with tail
    if snake.is_collision_with_tail():
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
