from replit import clear
import random
from art import logo


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

# Chose card
def deal_card(cards_used):
    card = random.choice(cards_used)
    return card


# takes a List of cards as input and returns the score
def calculate_score(list_player):
    score_player = sum(list_player)

    # check blackjack
    if list_player == [10, 11] or list_player == [11, 10]:
        return 0

    # check over 21
    if score_player > 21:
        if 11 in list_player:
            list_player.remove(11)
            list_player.append(1)

    return score_player


# comprare score
def compare(score_user, score_computer):
    if score_user == score_computer:
        print('It is a drawn')
    elif score_computer == 0:
        print('Wow, computer has a black jack. You lose :( ')
    elif score_user == 0:
        print('Wow, you had a blackjack. You won !!')
    elif score_user > 21:
        print('You went over. You lose :( ')
    elif score_computer > 21:
        print('Opponet went over. You won !!')
    elif score_user > score_computer:
        print('You won !!')
    else:
        print('You lose :( ')


def play_game():
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []
    end_game = False

    # Deal the user and computer 2 cards each
    for i in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))

    while end_game == False:
        print(f'Your cards: {user_cards}, your current score: ', calculate_score(user_cards))
        print("Computer's first card: ", computer_cards[0])

        # Check Blackjack
        if calculate_score(user_cards) == 0:
            end_game = True
        elif calculate_score(computer_cards) == 0:
            end_game = True
        elif calculate_score(user_cards) > 21:
            end_game = True
        else:
            answer = input("Do you want to take other card? Type 'y' or 'n': ").lower()
            if answer == 'y':
                user_cards.append(deal_card(cards))
            else:
                end_game = True

    # Computer play
    while calculate_score(computer_cards) < 17 and calculate_score(computer_cards) != 0:
        computer_cards.append(deal_card(cards))

    print(f'Your final hand: {user_cards}, your final score: ', calculate_score(user_cards))
    print(f"Computer's final hand: {computer_cards}, computer score: ", calculate_score(computer_cards))
    compare(calculate_score(user_cards), calculate_score(computer_cards))


while input('Do you want to play a game of BlackJack? Type y or n: ').lower() == 'y':
    clear()
    play_game()
