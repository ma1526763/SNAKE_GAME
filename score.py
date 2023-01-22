from turtle import Turtle


def get_highest_score():
    try:
        with open("highest_score.txt") as file:
            return int(file.readline())
    except FileNotFoundError:
        with open("highest_score.txt", "w") as file:
            file.write("0")
            return 0


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.h_score = get_highest_score()
        self.penup()
        self.goto(0, 250)
        self.hideturtle()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}\tHighest Score: {self.h_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!!", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.h_score:
            with open("highest_score.txt", "w") as file:
                file.write(str(self.score))
            self.h_score = self.score
        self.score = 0
        self.goto(0, 250)
        self.write_score()

