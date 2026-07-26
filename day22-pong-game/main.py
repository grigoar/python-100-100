import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle = Paddle((350, 0))
paddle2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()


def go_up():
    paddle.go_up()


def go_down():
    paddle.go_down()


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Bounce only when moving toward the paddle, so one hit can't flip repeatedly.
    if ball.distance(paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0:
        ball.bounce_x()

    if ball.distance(paddle2) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_x()

    # Reset the ball when it goes past the paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.r_point()

    # Reset the ball when it goes past the paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.l_point()


screen.exitonclick()
