import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(1)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    # def start_move(self):
    #     self.x_move = 10
    #     self.y_move = 10
    #
    # def stop_move(self):
    #     self.x_move = 0
    #     self.y_move = 0

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_position(self):
        self.setpos(0, 0)
        self.bounce_x()
