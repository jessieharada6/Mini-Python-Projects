from turtle import Screen, Turtle

# constant - outside of class
STARTING_POSITION = [(0.00,0.00), (-20.00,0.00), (-40.00,0.00)]
MOVING_DISTANCE = 20
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270
RIGHT_WALL_SIZE = 300
LEFT_WALL_SIZE = -300

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segments = Turtle("square")
        new_segments.penup()
        new_segments.color("white")
        new_segments.goto(position)
        self.segments.append(new_segments)

    def extend(self):
        # add a new segment to the snake
        tail_position = self.segments[-1].position()
        self.add_segment(tail_position)

    def move(self):
        for position in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[position - 1].xcor()
            new_ycor = self.segments[position - 1].ycor()
            self.segments[position].setposition(new_xcor, new_ycor)
        self.head.forward(MOVING_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
