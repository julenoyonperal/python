from turtle import Turtle
import random
print("Loading package: scoreboard")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(-200, 270)
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Te amo del uno al diez: {self.score}", align="left",
                   font=("Arial", 24, "normal"))

    def count(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.write("Game Over", align="left")


print("Loaded  package: scoreboard")
