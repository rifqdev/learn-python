import turtle
import pandas as pd
import time

screen = turtle.Screen()
screen.setup(width=800)
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")

count_answer = 0
state_answered = []

while count_answer != len(data):
    time.sleep(1)

    user_answer = screen.textinput(title=f"{count_answer}/{len(data)} States Correct", prompt="What's another state name").title()

    if user_answer == "Exit":
        break

    city = data[data.state == user_answer]
    if not city.empty:
        cor_x = city.x.values[0]
        cor_y = city.y.values[0]

        new_turtle = turtle.Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(cor_x, cor_y)
        new_turtle.write(user_answer, font=("Arial", 16, "normal"))
        if user_answer not in state_answered:
            count_answer += 1
            state_answered.append(user_answer)



# states to learn.csv
all_state = data['state'].to_list()
missing_states = [item for item in all_state if item not in state_answered]
# for state in all_state:
#     if state not in state_answered:
#         missing_states.append(state)

data_dict = {
    "states": missing_states
}

df = pd.DataFrame(data_dict)
df.to_csv("states_to_learn.csv")
