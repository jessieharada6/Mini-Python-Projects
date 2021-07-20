from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        # score_file.txt is manually created
        with open("score_file.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        # must update color before writing to show
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align = ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        # get highest score: but once game is closed, everything restarts
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score_file.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        # reset
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game over", align=ALIGNMENT, font=FONT)

