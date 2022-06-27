print('Hi drunkies')
bill = float(input('Quanto custou essa brincadeira? '))
person = int(input('Quantas pessoas na divisão? '))
taxa = int(input('Quantos % pro garçom? '))

payment = (bill/person) * (1+taxa/100)
print('O valor individual é ', round(payment,2),' dinheiros')