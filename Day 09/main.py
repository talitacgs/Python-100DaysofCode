from replit import clear
from art import logo

print(logo)
answer = 'yes'
players = {}


def storage(name_inputed, bid_inputed):
    players[name_inputed] = bid_inputed


while answer == 'yes':
    name = input('What is your name: ')
    bid = int(input('What is your bid price: '))

    storage(name, bid)

    answer = input('Is there another player? Type yes or no: '.lower())
    clear()

max_key = max(players, key=players.get)
print(f'The winner is {max_key} with total of {players[max_key]}')