import turtle
from paddle import Paddle
from ball import Ball
import time
# TODO initialise screen as 1000 by 100 black background
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")
screen.tracer(0)
# TODO initialise paddle from paddle class

paddle = Paddle(350, 0)
paddle2 = Paddle(-350, 0)

# TODO initialise ball

ball = Ball()

# TODO movement controls
screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")


# TODO game loop
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()
