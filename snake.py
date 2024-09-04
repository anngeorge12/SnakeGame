from turtle import Turtle
import random
POSITION = [(0, -20), (0, -40), (0, -60)]
color = ["green yellow", "darkolivegreen", "green"]


class Snake:
    def __init__(self):
        self.snake = []
        self.create()

    def create(self):
        for i in POSITION:
            self.add(i)

    def add(self, i):
        tim = Turtle("square")
        tim.penup()
        tim.goto(i)
        tim.color(random.choice(color))
        self.snake.append(tim)

    def extend(self):
        self.add(self.snake[-1].position())

    def move(self):
        for j in range(len(self.snake) - 1, 0, -1):
            x = self.snake[j - 1].xcor()
            y = self.snake[j - 1].ycor()
            self.snake[j].goto(x, y)
        self.snake[0].forward(20)

    def up(self):
        h = self.snake[0].heading()
        if h == 0:
            self.snake[0].left(90)
            self.move()
        elif h == 180:
            self.snake[0].right(90)
            self.move()

    def down(self):
        h = self.snake[0].heading()
        if h == 0:
            self.snake[0].right(90)
            self.move()
        elif h == 180:
            self.snake[0].left(90)
            self.move()

    def left(self):
        h = self.snake[0].heading()
        if h == 90:
            self.snake[0].left(90)
            self.move()
        elif h == 270:
            self.snake[0].right(90)
            self.move()

    def right(self):
        h = self.snake[0].heading()
        if h == 90:
            self.snake[0].right(90)
            self.move()
        elif h == 270:
            self.snake[0].left(90)
            self.move()

    def startover(self):
        self.snake.clear()
        self.create()

