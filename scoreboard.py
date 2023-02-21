from turtle import Turtle

ALIGNMENT= "center"
ALIGNMENT2= "left"
FONT = ("Courier", 25, "bold")
FONT_2 = ("Courier", 11, "bold")
L_SCORE_LOCATION = (-100, 250)
R_SCORE_LOCATION = (100, 250)
SPEED_LVL_LOC =  (320, 258)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        #self.goto()
        self.l_score = 0
        self.r_score = 0
        self.velocity_level = 0
        self.record_velocity_lvl = 0
        self.color("White")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(L_SCORE_LOCATION)
        self.clear()
        self.write(f"{self.l_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(R_SCORE_LOCATION)
        self.write(f"{self.r_score}", move=False, align=ALIGNMENT, font=FONT)
        self.goto(SPEED_LVL_LOC)
        self.write(f"Speed Lvl: {self.velocity_level}", move=False, align=ALIGNMENT, font=FONT_2)

    def l_point(self):
        self.l_score +=1
        self.update_scoreboard()
        self.velocity_level = 0

    def r_point(self):
        self.r_score +=1
        self.update_scoreboard()
        self.velocity_level = 0

    def speed_level(self):
        self.velocity_level +=1
        self.update_scoreboard()