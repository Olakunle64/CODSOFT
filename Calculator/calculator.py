#!/usr/bin/python3

"""A calculator for arithemetic operation

    The following are the availabe operations on this
    calculator:
        addition, subtraction, multiplication, modulo, division
        and power.
"""


def add(a, b):
    """return the addition a and b"""
    return a + b


def sub(a, b):
    """return the difference between a and b"""
    return a - b


def mul(a, b):
    """return the multiplication of a and b"""
    return a * b


def modulo(a, b):
    """return the modulo of a and b"""
    return a % b


def power(a, b):
    """return a raise to power of b"""
    return a ** b


def div(a, b):
    """return the division of a and b"""
    return a // b


operands = {'+': add, '-': sub, '*': mul, '%': modulo, '**': power, '/': div}


if __name__ == "__main__":
    import re

    userInput_regex = re.compile(r'''(\d+)\s #first operand
                                ([\+\-%\/\*]\*?) #operand(-,+,**,*,/,%)
                                \s(\d+) #second integer value''', re.VERBOSE)
    print("type <help> to see the details of the program or\
            <quit> to exit the program")
    while(True):
        userInput = input("CALCULATOR->$ ")
        if userInput == 'quit':
            break
        if userInput == 'help':
            print("type <help> to see how the program works or\
                    <quit> to exit the program")
            print("Usage: <integer> <operand> <integer> e.g, <2 + 2>")
            print("\tAvailable operands: +, -, /, %, *, **")
            continue

        validate_input = userInput_regex.search(userInput)
        if validate_input:
            a = int(validate_input.group(1))
            b = int(validate_input.group(3))
            result = operands[validate_input.group(2)](a, b)
            print(result)
        else:
            print("*** invalid input ***")
