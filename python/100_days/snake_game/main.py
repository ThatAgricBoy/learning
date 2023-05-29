from turtle import Turtle, Screen
import time
window = Screen()
window.title("Snake Game")
window.setup(width=600, height=600)
window.bgcolor("black")
window.tracer(0)


game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)






window.exitonclick()