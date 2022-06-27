print('''
*******************************************************************************
            .-""""-.       .-""""-.
           /        \     /        \
          /_        _\   /_        _\
         // \      / \\ // \      / \\
         |\__\    /__/| |\__\    /__/|
          \    ||    /   \    ||    /
           \        /     \        /
            \  __  /       \  __  /
    .-""""-. '.__.'.-""""-. '.__.'.-""""-.
   /        \ |  |/        \ |  |/        \
  /_        _\|  /_        _\|  /_        _\
 // \      / \\ // \      / \\ // \      / \\
 |\__\    /__/| |\__\    /__/| |\__\    /__/|
  \    ||    /   \    ||    /   \    ||    /
   \        /     \        /     \        /
    \  __  /       \  __  /       \  __  /
     '.__.'         '.__.'         '.__.'
 jgs  |  |           |  |           |  |
      |  |           |  |           |  |

*******************************************************************************
''')

print('Hi, Rick. Welcome to Space\n Your mission is to find fucking Morty')

direction = input('You are out solar system. Where do you want to go? Type "left" or "right": ')
direction = direction.lower()

if direction == 'left':
    print(
        'Peace Among universe. You found a strange criature telling it knows Morty, but you have to pay for the information. Type "pay" or "fuck off"')
    payment = input('Do you wanna pay ? ')
    payment.lower()

    if payment == 'fuck off':
        print('Yeah. You hit the creature, he is telling you to travel to Boobs Planet')

        for i in range(3):
            print('Traveling to Planet Boobs\n')

        print('Nice Rick, so many hoes. Do yoy wanna a cameleon girl or a clown girl? Type "Cameleon" or "Clown"')

        girl = input('Which one do you choose? ')
        girl = girl.lower()

        if girl == 'cameleon':
            print('Congratulations Rick, Cameleon girl is opening a door to Sistine Chapel where fucking Morty is in')
        else:
            print(
                'Clown girl is killing you right now and eating your ass, because only stupid people has clown as tattoo. Are you a morty? You know nothing, shit. Game Over')

    else:
        print('PAY ??? DO YOU WANNA PAY ??? I am so glad that the creature hit you. You are dead')
else:
    print('Right? To the right ??? You are a fucking bolsomion, rick? You are dead')
