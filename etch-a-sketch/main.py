from turtle import Turtle, Screen

screen = Screen()
screen.setup(500, 400)

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.back(10)

def clock_wise():
    tim.setheading(5)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=clock_wise)
screen.onkey(key="d", fun=move_forwards)
screen.onkey(key="c", fun=move_forwards)

screen.exitonclick()