from turtle import Turtle
import random


class food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        x_cor = random.randint(-260, 260)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)

    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)