import math

def prime_checker(number):

    numeros = list(range(2,math.ceil(number**0.5)+1))
    not_prime = []

    if number == 2 or number == 3:
        print("It's a prime number.")


    for algo in range(0,len(numeros)):
      if number % numeros[algo] == 0:
        not_prime.append(numeros[algo])

    values = len(not_prime)

    if values >= 1:
      print("It's not a prime number.")
    else:
      print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
