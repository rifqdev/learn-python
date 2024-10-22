import colorgram

# Extract 6 colors from an image.
# colors = colorgram.extract('color-dot.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
t.hideturtle()
t.penup()
colors = [(185, 160, 30), (123, 192, 232), (211, 36, 77), (240, 246, 251), (107, 96, 151), (219, 150, 46), (247, 196, 2), (110, 99, 160), (238, 201, 53), (70, 146, 131), (220, 40, 83), (72, 138, 124), (123, 172, 163), (209, 131, 151), (149, 204, 226), (235, 166, 184), (191, 113, 39), (187, 185, 208), (166, 29, 64), (170, 203, 196)]
t.setheading(210)
t.forward(230)
t.setheading(0)
number_of_dots = 100


for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(colors))
    t.forward(40)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(40)
        t.setheading(180)
        t.forward(400)
        t.setheading(0)



























screen = t.Screen()
screen.exitonclick()

