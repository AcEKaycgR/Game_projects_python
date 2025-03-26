from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.create_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.goto(-220,250)
        self.write(f"LEVEL {self.level}" , align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)
