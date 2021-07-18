from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 60, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        # must update color before writing to show
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    # in this class, 2 turtle objects are created
    # but when main calls, it is treated as a class
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 230)
        self.write(f"{self.l_score}", align = ALIGNMENT, font= FONT)
        self.goto(100, 230)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

