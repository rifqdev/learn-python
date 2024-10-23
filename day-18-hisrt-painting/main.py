import turtle
from turtle import Turtle, Screen
from random import choice, randint

my_turtle = Turtle()
my_turtle.shape('turtle')
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    color_tuple = (r, g, b)
    return color_tuple


# def draw_dashed():
#     for _ in range(15):
#         move_forward(10)
#         my_turtle.penup()
#         move_forward(10)
#         my_turtle.pendown()
#
#
# draw_dashed()

# def draw_different_shape(num_side):
#     angle = 360 / num_side
#     for _ in range(num_side):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
#
#
# for num_side in range(3, 10):
#     my_turtle.color(choice(turtle_color))
#     draw_different_shape(num_side)


# RANDOM WALK
# direction = [0, 90, 180, 270]
# my_turtle.pensize(15)
#
# for _ in range(200):
#     my_turtle.color(random_color())
#     my_turtle.forward(30)
#     my_turtle.right(choice(direction))


# SPIROGRAPH
my_turtle.speed('fastest')
def draw_spirograph(num_of_gap):
    for _ in range(int(360/num_of_gap)):
        my_turtle.color(random_color())
        my_turtle.circle(100)
        my_turtle.setheading(my_turtle.heading() + num_of_gap)


draw_spirograph(5)














screen = Screen()
screen.exitonclick()
