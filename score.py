from turtle import Turtle


class Score(Turtle):
    def __init__(self, score):
        super().__init__()
        self.goto(0, 280)
        self.penup()
        self.color("white")
        self.ht()
        self.point = score
        self.write(f"Score: {self.point}", move=False, align='center', font=('Arial', 15, 'normal'))

    def over(self):
        self.goto(0, 0)
        self.color("white")
        self.ht()
        self.penup()
        self.write("Game Over", move=False, align='center', font=('Arial', 15, 'normal'))








