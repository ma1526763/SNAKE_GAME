from turtle import Turtle

MOVE_DISTANCE = 20

def snake_common_attributes(seg):
    seg.shape("square")
    seg.penup()
    seg.color("green", "gold")

class Snake:
    def __init__(self):
        self.snake = []
        self.create_sanke_body()
        self.snake_head = self.snake[0]

    def create_sanke_body(self):
        self.snake = [Turtle() for i in range(4)]
        x_cor = 0
        for segment in self.snake[:]:
            snake_common_attributes(segment)
            segment.goto(x_cor, 0)
            x_cor -= 20

    def move_snake_body(self):
        new_position = self.snake[0].xcor(), self.snake[0].ycor()
        self.snake_head.forward(MOVE_DISTANCE)
        for segment in self.snake[1:]:
            segment_position = segment.xcor(), segment.ycor()
            segment.goto(new_position)
            new_position = segment_position

    def create_new_snake_segment(self):
        last_segment = self.snake[-1].xcor(), self.snake[-1].ycor()
        segment = Turtle()
        snake_common_attributes(segment)
        segment.goto(last_segment)
        return segment

    def detect_food_collision(self, food):
        if self.snake_head.distance(food) < 15:
            self.snake.append(self.create_new_snake_segment())
            return True
        else:
            return False

    def detect_wall_collision(self):
        s_x_cor = self.snake_head.xcor()
        s_y_cor = self.snake_head.ycor()
        return True if (abs(s_x_cor) >= 380 or abs(s_y_cor) >= 280) else False

    def detect_tail_collision(self):
        for segment in self.snake[1:]:
            if self.snake_head.distance(segment) < 10:
                return True
        else:
            return False

    def move_left(self):
        if self.snake_head.heading() != 0:
            self.snake_head.setheading(180)

    def move_right(self):
        if self.snake_head.heading() != 180:
            self.snake_head.setheading(0)

    def move_up(self):
        if self.snake_head.heading() != 270:
            self.snake_head.setheading(90)

    def move_down(self):
        if self.snake_head.heading() != 90:
            self.snake_head.setheading(270)

    def out_snake(self):
        for segment in self.snake:
            segment.goto(-1000, 1000)