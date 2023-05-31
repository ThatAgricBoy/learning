from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")

game_is_on = True
move_delay = 0.2

while game_is_on:
    window.update()
    time.sleep(move_delay)
    snake.move()

    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

        # Increase speed when score reaches certain thresholds
        if scoreboard.score % 5 == 0:
            move_delay *= 0.9

    #Detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()

    #Detect collision with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

window.exitonclick()
