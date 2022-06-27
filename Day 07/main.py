import random
from hangman_words import word_list
from hangman_art import stages, logo

# Variaveis
lifes = 6
end_game = False
display = []
used = []

print(logo)

# Escolha randomica da palavra
chosen_word = random.choice(word_list)

# Interface de posições
for i in chosen_word:
    a = '_'
    display.append(a)

# Escolha do usuario
while end_game == False:

    display_quantity_initial = display.count('_')
    letter = input('What letter do you choose? ').lower()

    if letter in used:
        print('You already used this letter')
    else:
        used.append(letter)
        # Comparar input usuario com letra da palavra escolhida
        for i in range(0, len(chosen_word)):
            if letter == chosen_word[i]:
                display[i] = letter

        display_quantity_final = display.count('_')

        if display_quantity_initial == display_quantity_final:
            lifes -= 1

        print(display)
        print('Lifes:', lifes)
        print('Used words: ', set(used))
        print(stages[lifes])

    # Condição para acabar o jogo
    if '_' not in display:
        print('You won !!!  👑  🏆  🥇 ')
        end_game = True
    elif lifes == 0:
        print('You lose !!! 🚽 💀 ⚰️')
        print('The word was: ', chosen_word)
        end_game = True

