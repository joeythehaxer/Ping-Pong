import turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard
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
# scoreboard
scoreboard = Scoreboard()
# TODO movement controls
screen.listen()
screen.onkey(paddle.go_up, "Up")
screen.onkey(paddle.go_down, "Down")
screen.onkey(paddle2.go_up, "w")
screen.onkey(paddle2.go_down, "s")


# TODO game loop
game_is_on = True
direction = 1
sleep_time = 0.1

while game_is_on:

    time.sleep(sleep_time)
    screen.update()
    # ball.start_move()
    ball.move()
#     detect ball collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        sleep_time *= 0.9
#     detect paddle collision
    if ball.distance(paddle) < 50 and ball.xcor() > 320 or ball.distance(paddle2) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        sleep_time *= 0.9

    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_score()
        sleep_time = 0.1
        # ball.setpos(0, 0)
        # direction = -1
        # ball.stop_move()
        # time.sleep(3)

    if ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_score()
        sleep_time = 0.1
        # ball.setpos(0, 0)
        # direction = 1
        # ball.stop_move()
        # time.sleep(3)
screen.exitonclick()
