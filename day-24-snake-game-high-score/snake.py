from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)


    def up(self):
        current_head = self.segments[0].heading()
        if current_head == 0.0:
            self.segments[0].setheading(current_head + 90)
        elif current_head == 180.0:
            self.segments[0].setheading(current_head - 90)

    def down(self):
        current_head = self.segments[0].heading()
        if current_head == 0.0:
            self.segments[0].setheading(current_head - 90)
        elif current_head == 180.0:
            self.segments[0].setheading(current_head + 90)

    def left(self):
        current_head = self.segments[0].heading()
        if current_head == 270.0:
            self.segments[0].setheading(current_head - 90)
        elif current_head == 90.0:
            self.segments[0].setheading(current_head + 90)

    def right(self):
        current_head = self.segments[0].heading()
        if current_head == 90.0:
            self.segments[0].setheading(current_head - 90)
        elif current_head == 270:
            self.segments[0].setheading(current_head + 90)

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000,1000)
        self.segments.clear()
        self.create_snake()