import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue", "cyan")
        self.penup()
        self.shapesize(.7)
        self.speed("fastest")

    def create_random_food(self):
        self.goto(random.randint(-360, 360), random.randint(-270, 270))

    def food_position(self):
        return self.xcor(), self.ycor()

    def out_food(self):
        self.goto(-1000, 1000)
