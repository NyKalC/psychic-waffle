import random
from turtle import Turtle

START_HEADINGS = [30, 60, 120, 150, 210, 240, 300, 330]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("square")
        self.speed("fastest")
        self.penup()
        self.ball_move()


    def ball_move(self):
        self.setheading(random.choice(START_HEADINGS))
