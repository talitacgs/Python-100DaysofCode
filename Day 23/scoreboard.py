from turtle import Turtle

FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(-200, 250)
        self.write(f'Level: {self.score}', align='center', font=FONT)

    def add_score(self):
        self.score += 1
        self.clear()
        self.write(f'Level: {self.score}', align='center', font=FONT)

    def lost(self):
        self.goto(0, 0)
        self.write(f'You lost! :( ', align='center', font=FONT)
