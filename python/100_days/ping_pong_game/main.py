from turtle import Screen, Turtle
# from paddle import pad

window = Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Ping Pong Game")

pad = Turtle()
pad.shape("square")
pad.color("white")
pad.shapesize(stretch_wid=5, stretch_len=1)
pad.penup()
pad.goto(350, 0)

def go_up():
    new_y = pad.ycor() + 20
    pad.goto(pad.xcor(), new_y)

def go_down():
    new_y = pad.ycor() - 20
    pad.goto(pad.xcor(), new_y)

window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")

window.exitonclick()