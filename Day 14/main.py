from game_data import data
from replit import clear
import random
from art import logo, vs


def random_personality():
    # Choose a personality randomly
    return random.choice(data)


def personality_selection(personality):
    # Format personality informations into printable format
    name = personality['name']
    description = personality['description']
    country = personality['country']
    return f'{name}, a {description}, from {country}'


def compare(user, one_follow, two_follow):
    if one_follow > two_follow:
        return user == 'a'
    else:
        return user == 'b'


# check answer's player against followers, it'll return True if they got it.
end_game = True
score = 0
personality_two = random_personality()
print(logo)

while end_game:
    personality_one = personality_two
    personality_two = random_personality()

    while personality_one == personality_two:
        personality_two = random_personality()

    print(f"Compare A: {personality_selection(personality_one)}.")
    print(vs)
    print(f"Compare B: {personality_selection(personality_two)}.")

    answer = input('Who has more followers? Type "A" or "B": ').lower()

    follower_one = personality_one['follower_count']
    follower_two = personality_two['follower_count']

    correct = compare(answer, follower_one, follower_two)

    clear()
    print(logo)

    if correct:
        score += 1
        print(f'Congrats !! Your current score: {score}')
    else:
        end_game = False
        print(f'So sorry, you got wrong answer. Final score: {score}')