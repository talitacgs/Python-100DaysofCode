from art import logo


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def subtract(n1, n2):
    return n1 - n2


# Multiply
def multiply(n1, n2):
    return n1 * n2


# Divide
def divide(n1, n2):
    return n1 / n2


operator = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    print(logo)
    n1 = float(input('Put the first number: '))
    for symbol in operator:
        print(symbol)

    continuation = True

    while continuation:
        operation = input('Which operator do you choose? +, - , *  or / : ')
        n2 = float(input('Put the other number: '))
        function = operator[operation]
        answer = function(n1, n2)

        print(f'{n1} {operation} {n2} = {answer}')

        if input('Do you wanna continue doing an operation with that number ? Type yes or no: ').lower() == 'yes':
            n1 = answer
        else:
            print('bye')
            continuation = False
            calculator()


calculator()
