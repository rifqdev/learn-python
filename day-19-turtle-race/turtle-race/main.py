from turtle import Turtle, Screen
import random

screen = Screen()
continue_play = 'yes'


def turtle_race():
    screen.clear()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? red, orange, yellow, green, blue, purple: enter a color")
    screen.title(f"Your turtle color is {user_bet}")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    all_turtles = []

    is_race_on = False

    if user_bet:
        is_race_on = True
    gap = -100

    for color in colors:
        new_turtle = Turtle(shape='turtle')
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(x=-230, y=gap)
        gap += 40
        all_turtles.append(new_turtle)

    global continue_play
    while is_race_on:

        for turtle in all_turtles:
            if turtle.xcor() > 220:
                is_race_on = False
                winning_color = turtle.pencolor()
                if user_bet.lower() == winning_color:
                    result = f"You win! The {winning_color} turtle is the winner!"
                else:
                    result = f"You lose! The {winning_color} turtle is the winner!"

                continue_play = screen.textinput(title=f"Race Results", prompt=f"{result} type yes to play again")
                return

            turtle.forward(random.randint(0, 10))


while continue_play.lower() == 'yes':
    turtle_race()


screen.exitonclick()
