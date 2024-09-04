from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
# Game Screen Creation
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
s = 0
snake = Snake()
eat = Food()
sc = Score(s)

# Button inputs
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game = True
while game:
    # Screen Refresh Moments
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Making Scoreboard and Food Update
    if snake.snake[0].distance(eat) < 15:
        snake.extend()
        sc.clear()
        s += 1
        sc = Score(s)
        eat.ht()
        eat = Food()
    # Collision at Wall
    if snake.snake[0].xcor() > 300 or snake.snake[0].xcor() < -300 or snake.snake[0].ycor() > 300 or snake.snake[0].ycor() < -300:
        sc.over()
        game = False

    # Collision on body
    for i in snake.snake[1:]:
        if snake.snake[0].distance(i) < 10:
            sc.over()
            game = False





screen.exitonclick()
