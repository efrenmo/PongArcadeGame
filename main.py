from turtle import Screen
from turtle import Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
from art import Art


screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong Arcade Game")
screen.bgcolor("black")


# Displays the Intro Art
art = Art()

screen.tracer(0)

# Initializing the paddles
r_paddle = Paddle((350, 0), "crimson")
l_paddle = Paddle((-350, 0), "RoyalBlue1")

court = Turtle()
court.hideturtle()
court.goto(0, -300)
court.color("white")
court.setheading(90)
court.forward(600)
court.penup()

court.goto(0, -55)
court.pendown()
court.color("gray10")
court.write("Pong", align="center", font=('Bradley Hand ITC', 70, "normal"))

scoreboard = Scoreboard()

ball = Ball()

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")


def button_click(x, y):
    if -150 < x < 150 and -100 < y < 0:
        exit()

button = Turtle()
button.color("white")
button.speed(0)
button.pensize(4)
button.penup()
button.hideturtle()

button_text = Turtle()
button_text.color("BLACK")
button_text.speed(0)
button_text.penup()
button_text.hideturtle()

button.begin_fill()

for _ in range(2):
    button.forward(300)
    button.left(90)
    button.forward(100)
    button.left(90)

button.end_fill()

LARGE_FONT_SIZE = 30
LARGE_FONT = ('Arial', LARGE_FONT_SIZE, 'normal')
button_text.write("Exit", align='center', font=LARGE_FONT)

screen.onscreenclick(button_click)




art.clear_intro()

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Detect collision with right paddle
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 318:
        ball.bounce_r_paddle()
        scoreboard.speed_level()

    # Detect collision with left paddle
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -318:
        ball.bounce_l_paddle()
        scoreboard.speed_level()

    # If R paddle misses
    elif ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
    # If L paddle misses
    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()

screen.exitonclick()
