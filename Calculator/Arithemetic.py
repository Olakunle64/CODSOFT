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


operands = {'+': add, '-': sub, 'X': mul, '%': modulo, '**': power, '/': div}


def calc(userInput):
    import re
    match_float_input = re.compile(r'''(\d+\.\d+)\s # first operand
                                ([\+\-%\/X]?)\s # operand (-,+,**,*,/,%)
                                (\d+\.\d+) # second operand''', re.VERBOSE)
    
    match_int_input = re.compile(r'''\b(\d+)\s #first operand
                                ([\+\-%\/X]?) #operand(-,+,**,*,/,%)
                                \s(\d+)\b #second integer value''', re.VERBOSE)
    validate_input_float = match_float_input.search(userInput)
    validate_input_integer = match_int_input.search(userInput)
    if validate_input_float or validate_input_integer:
        rm_newline = str(userInput.strip("\n "))
        a = eval(rm_newline.split()[0].strip())
        b = eval(rm_newline.split()[2].strip())
        result = operands[rm_newline.split()[1]](a, b)
        return result
    