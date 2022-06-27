rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

escolha = int(input('Escolha 0 para 🗿, 1 para 📄, 2 para ✂️: '))

if escolha == 0:
  print(rock)
elif escolha == 1:
  print(paper)
else:
  print (scissors)

escolha_pc = random.randint(0,2)

if escolha_pc == 0:
  print(rock)
elif escolha_pc == 1:
  print(paper)
else:
  print(scissors)

if escolha == escolha_pc:
  print('Empate, jogue novamente')
elif escolha == 0 and escolha_pc == 1:
  print('O computador venceu')
elif escolha == 0 and escolha_pc == 2:
  print('Você venceu')
elif escolha == 1 and escolha_pc == 0:
  print('Você venceu')
elif escolha == 1 and escolha_pc == 2:
  print('O computador venceu')
elif escolha == 2 and escolha_pc == 0:
  print('O computador venceu')
else:
  print('Você venceu')
