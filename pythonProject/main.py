import turtle
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
screen = turtle.Screen()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########

for n in range(0, 361, 6):
  tim.pencolor(random_color())
  tim.circle(150)
  tim.setheading(n)

t.exitonclick()