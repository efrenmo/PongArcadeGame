import time
from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("lawn green")
        self.penup()
        self.bounce_count_r = True
        self.bounce_count_l = True
        self.x_move = 18
        self.y_move = 18
        self.move_speed = 0.16

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_wall(self):
        self.y_move *= -1

    def bounce_r_paddle(self):
        while self.bounce_count_r:
            self.x_move *= -1
            self.bounce_count_r = False
            self.bounce_count_l = True
            self.move_speed *= 0.9

    def bounce_l_paddle(self):
        while self.bounce_count_l:
            self.x_move *= -1
            self.bounce_count_l = False
            self.bounce_count_r = True
            self.move_speed *= 0.9

    def reset_position(self):
        self.setposition(0,0)
        self.move_speed = 0.16
        self.x_move *= -1
        self.move()

