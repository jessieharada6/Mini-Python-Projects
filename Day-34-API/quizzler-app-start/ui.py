from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    # TODO: quiz_brain: QuizBrain -> variable: type
    # 1. ensure the correct data type when passing into object
    # 2. when using the variable, the methods/properties show
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        # must provide the x and y positions - if not -> IndexError: tuple index out of range
        self.quiz_question = self.canvas.create_text(
            150,
            125,
            # set the width less than the canvas width,
            # so the texts are wrapped
            width=280,
            text="Question texts",
            fill= THEME_COLOR,
            font=("Arial", 20, "italic"))
        # pady provides further padding on top of window padding for up and down
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, bd=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=0)
        correct_img = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_img, highlightthickness=0, bd=0, command=self.true_pressed)
        self.correct_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text =  self.quiz.next_question()
            self.canvas.itemconfig(self.quiz_question, text=q_text)
        else:
            self.canvas.itemconfig(self.quiz_question, text="You've reached the end of the quiz")
            # disable the buttons to be pressed again
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_false = self.quiz.check_answer("False")
        self.give_feedback(is_false)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

