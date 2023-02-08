from turtle import Screen, Turtle
from scoreboard import ScoreBoard
from players import Players
from ball import Ball

SCREEN_LENGTH = 1536
SCREEN_WIDTH = 768
SCREEN_COLOR = "black"

screen = Screen()
screen.setup(SCREEN_LENGTH, SCREEN_WIDTH)
screen.bgcolor(SCREEN_COLOR)


scoreboard = ScoreBoard(SCREEN_LENGTH, SCREEN_WIDTH)
players = Players()
ball = Ball()

screen.listen()
screen.onkey(players.two_up, "Up")
screen.onkey(players.two_down, "Down")
screen.onkey(players.one_up, "w")
screen.onkey(players.one_down, "s")

ball_in_play = True
while ball_in_play:
    ball.forward(1)
    print(ball.heading())
    if int(ball.xcor()) == 748:
        print("POINT")
        ball_in_play == False
        break

    if int(ball.xcor()) == -748:
        print("POINT")
        ball_in_play == False
        break


    if int(ball.ycor()) == 364:
        new_heading = ball.heading() + 90
        ball.setheading(new_heading)

    if int(ball.ycor()) == -364:
        new_heading = ball.heading() + 90
        ball.setheading(new_heading)


screen.exitonclick()