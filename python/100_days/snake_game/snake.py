from turtle import Turtle
class Snake:
    """This module describes the behaviour of the snake"""
    turtle_positions = [(0, 0), (-20, 0), (-40, 0)]
    snakes = []
    for position in turtle_positions:
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        snakes.append(segment)
    def __init__(self, ):
        pass

    def move(self):

        for seg_num in range(len(snakes) - 1, 0, -1):
            new_x = snakes[seg_num - 1].xcor()
            new_y = snakes[seg_num - 1].ycor()
            snakes[seg_num].goto(new_x, new_y)
        snakes[0].forward(20)



