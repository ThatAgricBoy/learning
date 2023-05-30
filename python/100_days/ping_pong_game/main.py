from turtle import Screen
from paddle import Pad
from ball import Ball
import time

window = Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Ping Pong Game")
window.tracer(0)

right_pad = Pad((350, 0))
left_pad = Pad((-350, 0))
ball = Ball()


window.listen()
window.onkey(right_pad.go_up, "Up")
window.onkey(right_pad.go_down, "Down")
window.onkey(left_pad.go_up, "w")
window.onkey(left_pad.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    window.update()
    ball.ball_move()



window.exitonclick()