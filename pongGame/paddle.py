from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.create_self()

    def create_self(self):
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(self.position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.position[0], new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.position[0], new_y)
