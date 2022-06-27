from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.goto(0, 280)
        self.color('white')
        self.hideturtle()
        self.write(f'Score: {self.score}  High Score = {self.high_score}', align='center', font=('arial', 14, 'bold'))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Score: {self.score}  High Score = {self.high_score}', align='center', font=('arial', 14, 'bold'))

    def refresh(self):
        self.score += 1
        self.clear()
        self.write(f'Score: {self.score}  High Score = {self.high_score}', align='center', font=('arial', 14, 'bold'))

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.score = 0
        self.clear()
        self.write(f'Score: {self.score}  High Score = {self.high_score}', align='center', font=('arial', 14, 'bold'))


