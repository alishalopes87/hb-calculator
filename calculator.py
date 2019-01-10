"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

import arithmetic as ar


# Your code goes here


def consume_input():
    """Get input from user"""

    user_input = input("print >")
    return user_input

def evaluate_input():
    """tokenize input"""

    user_input = consume_input()
    token_input = user_input.split(' ')
    return token_input

def calculator():
    """ Calculator for basic arithmetic functions"""

    while True:
        token_list = evaluate_input()
        token = token_list[0]
        #for token in token_list:
        if token ==  "q":
            break
        elif token == "+":
            print(ar.add(float(token_list[1]), float(token_list[2])))

        elif token == "-":
            print(ar.subtract(float(token_list[1]), float(token_list[2])))

        elif token == "*":
            print(ar.multiply(float(token_list[1]), float(token_list[2])))

        elif token == "/":
            print(ar.divide(float(token_list[1]), float(token_list[2])))

        elif token == "square":
            print(ar.square(float(token_list[1])))

        elif token == "cube":
            print(ar.cube(float(token_list[1])))

        elif token == "pow":
            print(ar.power(float(token_list[1]), float(token_list[2])))

        elif token == "mod":
            print(ar.mod(float(token_list[1]), float(token_list[2])))

        else:
            print("This isn't arithmetic!")


calculator()