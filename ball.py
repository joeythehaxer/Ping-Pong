import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(1)

    def move(self):
        x = self.xcor() + 10
        y = self.ycor() + 10
        self.goto(x, y)
