import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("Naija States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
screen.bgcolor("black")
turtle.shape(image)
turtle = Turtle()


def get_mouse_click_cord(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_cord())

screen.mainloop()
