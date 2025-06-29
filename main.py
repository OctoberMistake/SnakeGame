from turtle import Screen
from food import Food
from snake import Snake
import time
from score_board import Score_board


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = Screen()
screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score_board()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.update_score()
        score.clear()
        score.print_score()
        snake.extend()

    #hit the wall
    if abs(snake.head.pos()[0])>screen.screensize()[0] or abs(snake.head.pos()[1])>screen.screensize()[1]:
        game_is_on = False
        score.game_over()

    #hit their own tail
    for segment in snake.segments[2:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()