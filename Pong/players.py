from turtle import Turtle

POSITION = [(-728, 0), (728, 0)]
MOVEMENT_SPEED = 25
MAX_LIMIT = 325

class Players(Turtle):

    def __init__(self):
        super().__init__()
        self.player = []
        self.create_players()
        self.player1 = self.player[0]
        self.player2 = self.player[1]

    def create_players(self):
        for position in POSITION:
            self.draw_player(position)

    def draw_player(self, position):
        new_player = Turtle("square")
        new_player.color("white")
        new_player.penup()
        new_player.speed("fastest")
        new_player.resizemode("user")
        new_player.shapesize(stretch_wid=1, stretch_len=5, outline=1)
        new_player.setheading(90)
        new_player.goto(position)
        self.player.append(new_player)

    def two_up(self):
        print(self.player2.ycor())
        if self.player2.ycor() != MAX_LIMIT:
            self.player2.setheading(90)
            self.player2.forward(MOVEMENT_SPEED)

    def two_down(self):
        print(self.player2.ycor())
        if self.player2.ycor() != -MAX_LIMIT:
            self.player2.setheading(270)
            self.player2.forward(MOVEMENT_SPEED)

    def one_up(self):
        print(self.player1.ycor())
        if self.player1.ycor() != MAX_LIMIT:
            self.player1.setheading(90)
            self.player1.forward(MOVEMENT_SPEED)

    def one_down(self):
        print(self.player1.ycor())
        if self.player1.ycor() != -MAX_LIMIT:
            self.player1.setheading(270)
            self.player1.forward(MOVEMENT_SPEED)