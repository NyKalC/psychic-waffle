from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, screenlength, screenwidth):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.length = screenlength
        self.width = screenwidth
        self.font = ('Bauhaus 93', 50, 'bold')
        self.align = "center"
        self.player_1_score = 0
        self.player_2_score = 0
        self.player_1_scoreboard()
        self.player_2_scoreboard()
        self.draw_net()

    def player_1_scoreboard(self):
        self.goto(-50, (self.width/2 - 80))
        self.write(self.player_1_score, False, self.align, font=self.font)

    def player_2_scoreboard(self):
        self.goto(50, (self.width/2 - 80))
        self.write(self.player_2_score, False, self.align, font=self.font)

    def draw_net(self):
        self.goto(0, (self.width/2))
        self.setheading(270)
        self.pensize(10)
        self.pendown()
        self.forward(self.width)