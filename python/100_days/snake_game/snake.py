from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    """This module describes the behaviour of the snake"""
    def __init__(self):
        self.snakes = []
        self.create_snakes()
        self.head = self.snakes[0]

    def create_snakes(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.snakes.append(segment)

    def move(self):
        for seg_num in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[seg_num - 1].xcor()
            new_y = self.snakes[seg_num - 1].ycor()
            self.snakes[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.setheading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.setheading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.setheading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.setheading() != LEFT:
            self.head.setheading(RIGHT)


