from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('PONG')
screen.tracer(0)    # control the animation, if 0 then animation is turned off.
'''Now you have to manually update the screen & refresh it everytime'''

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, key='Up')
screen.onkey(r_paddle.go_down, key='Down')
screen.onkey(l_paddle.go_up, key='w')
screen.onkey(l_paddle.go_down, key='s')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)     # screen sleep for 0.1 sec after every update
    screen.update()
    ball.move()

    # check ball collision with top & bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # check ball collision with paddles
    if ball.xcor() > 320 and ball.distance(r_paddle) < 40 or ball.xcor() < -320 and ball.distance(l_paddle) < 40:
        ball.bounce_x()

    # check right paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # check left paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
