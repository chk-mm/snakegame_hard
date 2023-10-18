from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Score: 0", align="center", font=("Courier", 24, "normal"))
        self.score = 0
        self.high_score = 0

    def write_score(self,point):
        if point > 0:
            self.score += 10
            self.clear()
            self.highest_score()
            self.goto(0,260)
            self.write("Score: {}".format(self.score), align="center", font=("Courier", 24, "normal"))
            self.goto(0,250)
            self.write("High Score: {}".format(self.high_score), align="center", font=("Courier", 24, "normal"))
        else:
            self.clear()
            self.write("GAME OVER!!", align="center", font=("Courier", 24, "normal"))

    def clear_score(self):
        self.score = 0

    def highest_score(self):
        if self.score > self.high_score:
            self.high_score = self.score