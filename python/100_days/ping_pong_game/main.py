from turtle import Screen
from paddle import Pad
from ball import Ball
from scoreboard import Scoreboard
import time

window = Screen()
window.setup(width=800, height=600)
window.bgcolor("black")
window.title("Ping Pong Game")
window.tracer(0)

right_pad = Pad((350, 0))
left_pad = Pad((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

window.listen()
window.onkey(right_pad.go_up, "Up")
window.onkey(right_pad.go_down, "Down")
window.onkey(left_pad.go_up, "w")
window.onkey(left_pad.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    window.update()
    ball.ball_move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(right_pad) < 50 and ball.xcor() > 320 or ball.distance(left_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

window.exitonclick()