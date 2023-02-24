from turtle import Screen
from scoreboard import ScoreBoard
from players import Players
from ball import Ball
import time

SCREEN_LENGTH = 1540
SCREEN_WIDTH = 780
SCREEN_COLOR = "black"

screen = Screen()
screen.setup(SCREEN_LENGTH, SCREEN_WIDTH)
screen.bgcolor(SCREEN_COLOR)
screen.title("Pong")
screen.tracer(0)

scoreboard = ScoreBoard(SCREEN_LENGTH, SCREEN_WIDTH)
player1 = Players((730, 0))
player2 = Players((-730, 0))
ball = Ball()


screen.listen()
screen.onkey(player1.two_up, "Up")
screen.onkey(player1.two_down, "Down")
screen.onkey(player2.one_up, "w")
screen.onkey(player2.one_down, "s")

ball_in_play = True
while ball_in_play:
    screen.update()
    time.sleep(0.05)
    ball.ball_move()
    ball.move()

    if ball.ycor() > 370 or ball.ycor() < -370:
        ball.bounce_y()

    #detech collision with right panel
    if ball.distance(player1) < 50 and ball.xcor() > 690 or ball.distance(player2) < 50 and ball.xcor() < -690:
        ball.bounce_x()

    if ball.xcor() > 750:
        scoreboard.clear()
        scoreboard.player1_score()
        ball.setposition(0, 0)
        ball.point_scored()



    if ball.xcor() < -750:
        scoreboard.clear()
        scoreboard.player2_score()
        ball.setposition(0, 0)
        ball.point_scored()


screen.exitonclick()
