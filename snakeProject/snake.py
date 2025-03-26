from turtle import Turtle
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        """Creates the snake"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in starting_positions:
            self.create_segment(positions)

    def create_segment(self,positions):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(positions)
        self.segments.append(new_segment)

    def extend(self):
        self.create_segment(self.segments[-1].position())

    def move(self):
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor()
            new_y = self.segments[segment_number - 1].ycor()
            self.segments[segment_number].goto(new_x, new_y)
        self.head.forward(move_distance)

    def snake_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
