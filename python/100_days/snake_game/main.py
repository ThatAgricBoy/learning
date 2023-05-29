from turtle import Turtle, Screen
screen = Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")

turtle_positions = [(0, 0), (-20, 0), (-40, 0)]
for position in turtle_positions:
    maxi = Turtle("square")
    maxi.color("white")
    maxi.goto(position)

# def draw_snake():
#     for _ in range(4):
#         maxi.forward(50)
#         maxi.right(90)
# draw_snake()







screen.exitonclick()