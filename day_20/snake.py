# # snake class

from turtle import Turtle, Screen


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):

        self.segments = []
        self.color = "white"
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle()
            segment.shape("square")
            segment.color(self.color)
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for index in range(len(self.segments)-1, 0, -1):
            self.segments[index].goto(self.segments[index-1].xcor(),
                                      self.segments[index-1].ycor())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 90 and self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 270 and self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 180 and self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 0 and self.head.heading() != 180:
            self.head.setheading(0)

    def reset(self):
        for segment in self.segments:
            segment.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend_snake(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)
