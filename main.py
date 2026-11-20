from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height= 600, width = 600)
# so this setup is what gives me the choice of H and W, and if I wanna start of the left corner startx, starty = 0
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
score_board = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.increase_score()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        snake.reset_snake()
        score_board.reset_game()

    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 5:
            score_board.reset_game()
            snake.reset_snake()



screen.exitonclick()
