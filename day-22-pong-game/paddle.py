from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_post, y_post):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.x_post = x_post
        self.y_post = y_post
        self.goto(self.x_post,self.y_post)

    def move_up(self):
        self.y_post += 20
        self.goto(self.x_post, self.y_post)

    def move_down(self):
        self.y_post -= 20
        self.goto(self.x_post, self.y_post)
