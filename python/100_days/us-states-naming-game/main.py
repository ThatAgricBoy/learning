from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
screen.bgcolor("black")
turtle.shape(image)
# def get_mouse_click_cord(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_cord())
#screen.mainloop()

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_answer = screen.textinput(title=f"{len(guessed_states)}/50 states Correct",
                                   prompt="What is another State name").title()
    if user_answer == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states to learn.csv")
        break
    if user_answer in all_states:
        guessed_states.append(user_answer)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == user_answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_answer)

screen.exitonclick()