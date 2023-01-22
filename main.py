from turtle import Screen
from snake import Snake
from food import Food
from screen import ScreenFunctions
from score import Score
import time
def start_game():
    sc = ScreenFunctions(screen)  # setup_screen
    screen.tracer(0)  # wait till update
    s = Snake()
    f = Food()
    sc.key_listen(s)  # screen key_listen
    f.create_random_food()

    while True:
        screen.update()
        s.move_snake_body()
        # if wall or tail collide game will end
        if s.detect_wall_collision() or s.detect_tail_collision():
            screen.tracer(0)
            my_score.game_over()
            screen.update()
            time.sleep(1)
            break
        # if snake gets the food update the snake and update it.
        if s.detect_food_collision(f):
            f.create_random_food()
            my_score.increase_score()
            my_score.write_score()
        time.sleep(0.1)
    my_score.reset()
    s.out_snake()
    f.out_food()
    start_game()

screen = Screen()
screen.tracer(0)
my_score = Score()
screen.update()
start_game()
screen.exitonclick()
