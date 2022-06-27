from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.listen()
screen.setup(width=800, height=500)
screen.colormode(255)
user_bet = screen.textinput(title="Make your bet:",prompt='Which turtle will win the race? Enter a color: ')

bob = Turtle(shape='turtle')
bob.color('black', 'purple')
bob.penup()
bob.goto(-230, -100)
bob.write('Bob')

guri = Turtle(shape='turtle')
guri.color('black', 'turquoise')
guri.penup()
guri.goto(-230, 50)
guri.write('Guri')

brenda = Turtle(shape='turtle')
brenda.color('black', 'orange')
brenda.penup()
brenda.goto(-230, 0)
brenda.write('Brenda')

tali = Turtle(shape='turtle')
tali.color('black', 'black')
tali.penup()
tali.goto(-230, -50)
tali.write('Talita')

tata = Turtle(shape='turtle')
tata.color('black', 'red')
tata.penup()
tata.goto(-230, 150)
tata.write('Renata')

mary = Turtle(shape='turtle')
mary.color('black', 'blue')
mary.penup()
mary.goto(-230, 100)
mary.write('Maryna')

marc = Turtle(shape='turtle')
marc.color('black', 'green')
marc.penup()
marc.goto(-230, -150)
marc.write('Marcola')

mari = Turtle(shape='turtle')
mari.color('black', 'yellow')
mari.penup()
mari.goto(-230, 200)
mari.write('MariDias')

all_turtles = [bob, brenda, guri, marc, mari, mary, tali, tata]
if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            if turtle.fillcolor() == user_bet:
                print("You Won!")
            else:
                print(f'You lose, the {turtle.fillcolor()} won!')
            is_race_on=False
        turtle.pendown()
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




print(screen.canvheight)
screen.exitonclick()

