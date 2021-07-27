from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Verdana", 16, "normal")

class States(Turtle):
    def __init__(self):
        super().__init__()
        self.correct_guess = []
        self.penup()
        self.hideturtle()

    def add_states(self, x, y, answer):
        self.goto(x, y)
        self.write(answer, align=ALIGNMENT, font=FONT)

    def increase_score(self, answer):
        if answer not in self.correct_guess:
            self.correct_guess.append(answer)
        return len(self.correct_guess)
