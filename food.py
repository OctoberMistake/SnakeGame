from turtle import Turtle
from random import randint

class Food(Turtle):

    """Esta es la clase que hace la domida del jugo de snake
    this is the class that makes the snake game food"""

    def __init__(self):
        """init food"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        random_x = randint(-280, 280)
        random_y = randint(-280, 280)
        self.goto(random_x, random_y)
        
