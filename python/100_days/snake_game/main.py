from turtle import Screen
from snake import Snake
from food import Food
import time

window = Screen()
window.title("Snake Game")
window.setup(width=600, height=600)
window.bgcolor("black")
window.tracer(0)

snake = Snake()
food = Food()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.right, "Right")
window.onkey(snake.left, "Left")
window.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    window.update()
    time.sleep(0.1)
    snake.move()



window.exitonclick()