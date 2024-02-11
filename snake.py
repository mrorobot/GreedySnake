POSITION=[(0,0), (-20,0), (-40,0)]

from turtle import Turtle
from scoreboared import Scoreboard
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:

    def __init__(self):
        self.bodies=[]
        self.body()

    def body(self):
        for position in POSITION:
            self.new_segment(position)

    def new_segment(self, position):
        turtle = Turtle("turtle")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        part = turtle
        self.bodies.append(part)

    def extend(self):
        self.new_segment(self.bodies[-1].position())

    def movement(self):
        for body_num in range(len(self.bodies) - 1, 0, -1):
            new_x = self.bodies[body_num - 1].xcor()
            new_y = self.bodies[body_num - 1].ycor()
            self.bodies[body_num].goto(new_x, new_y)
        self.bodies[0].forward(20)

    def reset_snake(self):
        for body in self.bodies:
            body.goto(1000,1000)

        self.bodies.clear()
        self.body()



    def up(self):
        if self.bodies[0].heading()!=DOWN:
            self.bodies[0].setheading(UP)

    def down(self):
        if self.bodies[0].heading() !=UP:
            self.bodies[0].setheading(DOWN)

    def right(self):
        if self.bodies[0].heading() != LEFT:
            self.bodies[0].setheading(RIGHT)

    def left(self):
        if self.bodies[0].heading() != RIGHT:
            self.bodies[0].setheading(LEFT)