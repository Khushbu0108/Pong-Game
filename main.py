from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(height= 600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) #control the animation , turn off the animation put 0

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.increase_speed)
    screen.update()
    ball.move()

    #detect the collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()


    #detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #if right paddle misses ball
    if ball.xcor() > 380:
        ball.restart()
        scoreboard.l_point()

    #if left paddle misses ball
    if ball.xcor() < -380:
        ball.restart()
        scoreboard.r_point()

screen.exitonclick()
