from turtle import Turtle

ALIGMENT = 'center'
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", False, align=ALIGMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=("Arial", 24, "normal"))


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align=ALIGMENT, font=FONT)