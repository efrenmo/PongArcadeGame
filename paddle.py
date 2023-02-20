from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.setposition(position)
        self.setheading(90)
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()


    def go_up(self):
        self.forward(32)
    # def go_up():
    #     new_y =  paddle1.ycor() + 20
    #     paddle1.goto(paddle1.xcor(), new_y)
    def go_down(self):
        self.backward(32)

