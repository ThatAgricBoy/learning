import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
leo = Turtle()

# for i in range(10):
#     my_turtle.forward(10)
#     my_turtle.penup()
#     my_turtle.forward(10)
#     my_turtle.pendown()

# num_size = 5
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors
#
# directions = [0, 90, 180, 270]
# my_turtle.pensize(15)
leo.speed("fastest")
#
# for move in range(250):
#     my_turtle.color(random_color())
#     my_turtle.forward(25)
#     my_turtle.setheading(random.choice(directions))

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         my_turtle.forward(100)
#         my_turtle.right(angle)
# for shape_side_n in range(3, 11):
#     my_turtle.color(random.choice(colors))
#  draw_shape(shape_side_n)
def draw_spiral(gap_btw_circles):
    for circs in range(int(360 / gap_btw_circles)):
        leo.color(random_color())
        leo.circle(100)
        current_heading = leo.heading()
        leo.setheading(current_heading + gap_btw_circles)

draw_spiral(10)

my_screen = Screen()
my_screen.exitonclick()
