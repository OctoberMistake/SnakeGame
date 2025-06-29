from turtle import Turtle
from game_art import GAME_OVER_TEXT

INIT_POS = (0, 270)
FONT = ("courier", 16, "normal")
ALIGMENT = "center"

class Score_board(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(INIT_POS)
        self.color("white")
        self.hideturtle()
        self.print_score()

    def update_score(self):
        self.score += 1

    def print_score(self):
        mess = f"Score: {self.score}"
        self.write(mess, align = ALIGMENT, font= FONT)

    def game_over(self):
        self.clear()
        self.home()
        self.write(f"{GAME_OVER_TEXT}\nYour score is: {self.score}", align = ALIGMENT, font= FONT)