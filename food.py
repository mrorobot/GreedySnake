from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(0.7,0.7)
        self.color("green")
        self.speed("fastest")
        self.refresh()
    def refresh(self):
        x = random.randint(0, 280)
        y = random.randint(0, 280)
        self.goto(x, y)