from turtle import Turtle
import time

ALIGNMENT="center"


LOGO = r"""

                      .
                      |\
       \_ O     _     |X\
         /\_==(#)      XX\          _    O_/
       \/\              XX\    o   (#)==_/\                                               
          \              XX\              /\/                                            
                          XX\            /                                                
88888b. 88888888b.  .d88b. 88888b.  .d88b. 88888b.  .d88b.  
888 "88b888888 "88bd88P"88b888 "88bd88""88b888 "88bd88P"88b 
888  888888888  888888  888888  888888  888888  888888  888 
888 d88P888888  888Y88b 888888 d88PY88..88P888  888Y88b 888 
88888P" 888888  888 "Y8888888888P"  "Y88P" 888  888 "Y88888 
888                     888888                          888 
888                Y8b d88P888                     Y8b d88P 
888                 "Y88P" 888                      "Y88P"  


"""


class Art(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(117, -100)
        self.color("white")
        self.intro()

    def intro(self):
        self.write(LOGO, align=ALIGNMENT, font=("courier", 10, "bold") )

    def clear_intro(self):
        time.sleep(4)
        self.clear()