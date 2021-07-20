# render itself as a small circle on the screen
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
      super().__init__()
      # self now refers to Turtle class
      self.shape("circle")
      self.penup()
      # 20 * 0.5
      self.shapesize(stretch_len=0.5, stretch_wid=0.5)
      self.color("blue")
      self.speed("fastest")
      self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
