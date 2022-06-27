import random
from art import logo

number = random.randint(1, 100)
end_game = True
life = 0


def check_number(player_number):
    # Check number, if it is correct return 0
    if player_number < number:
        print('Too low 🥶')
    elif player_number > number:
        print('Too high 🥵')
    else:
        return 0


print(logo)

user_level = input('Do you want to play easy mode or hard mode? Type "easy" or "hard"\n').lower()

if user_level == 'easy':
    life = 10
else:
    life = 6

while end_game == True:
    user_guess = int(input('Choose a number: '))
    check_number(user_guess)
    if user_guess != number:
        life -= 1
    print(f'Lifes: {life}')

    if life == 0:
        print(f'You died ☠️, the number was: {number}')
        end_game = False
    elif check_number(user_guess) == 0:
        print('Congrats, you guessed 👑')
        end_game = False
