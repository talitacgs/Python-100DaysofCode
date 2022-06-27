from turtle import Turtle

class Score(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(x, y)
        self.write(f'Score = {self.score}', align='center', font=('Arial', 14, 'bold'))

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score = {self.score}', align='center', font=('Arial', 14, 'bold'))

