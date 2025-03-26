from turtle import Turtle

ALIGNMENT = "CENTER"
FONT = ("Courier", 70, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.create_scoreboard()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def create_scoreboard(self):
        self.shape("circle")
        self.hideturtle()
        self.color("white")
        self.penup()

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)
