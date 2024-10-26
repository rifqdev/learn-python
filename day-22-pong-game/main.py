from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()
screen.tracer(0)

r_paddle = Paddle(x_post= 370, y_post= 0)
l_paddle = Paddle(x_post= -380, y_post= 0)


screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")


ball = Ball()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -350:
        ball.bounce_x()

    # r missed
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # l missed
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()