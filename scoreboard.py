from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, l_player, r_player):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-200, 250)
        self.update_score(l_player, r_player)

    def update_score(self, l_player, r_player):
        self.clear()
        self.write(f"{l_player}: {self.l_score}", align="center", font=("Courier", 30, "normal"))
        self.goto(200, 250)
        self.write(f"{r_player}: {self.r_score}", align="center", font=("Courier", 30, "normal"))
        self.goto(-200, 250)

    def l_point(self):
        self.l_score += 1

    def r_point(self):
        self.r_score += 1

    def winner(self, winner):
        self.goto(0, 0)
        self.write(f"{winner} is the winner!!!", align="center", font=("Courier", 40, "bold"))
