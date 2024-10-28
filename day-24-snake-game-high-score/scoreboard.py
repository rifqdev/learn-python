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
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.score = 0
        self.update_score()            

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, align=ALIGMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.update_score()


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(str(self.score))
        self.score = 0
        self.update_score()
