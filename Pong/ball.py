import random
from turtle import Turtle

START_HEADINGS = [30, 60, 120, 150, 210, 240, 300, 330]

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed("fastest")
        self.penup()
        self.ball_move()
        self.x_move = 10
        self.y_move = 10


    def ball_move(self):
        self.setheading(random.choice(START_HEADINGS))

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.x_move += 5
        self.y_move += 5

    def point_scored(self):
        self.setposition(0,0)
        self.bounce_x()