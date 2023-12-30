#!/usr/bin/python3

"""This module contains a program that generate a strong
    random password.

    Note: the length of the password depends on the user input
    """

import random


def paswdGen(arg):
    """generate a random password of length arg"""
    symbols = ["/", "!", "#", "$", "%", "^", "&", "*"]
    symbols.extend(["(", ")", "-", "_", "{", "}", ":", ";"])
    numbers = list(range(0, 9))
    upper_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    small_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    mixture = []
    for letter in upper_letters:
        if symbols:
            mixture.append(symbols.pop())
        mixture.append(letter)
        if numbers:
            mixture.append(numbers.pop())
        if small_letters:
            mixture.append(small_letters.pop())
    i = 0
    password = ""
    while (i < arg):
        password += str(random.choice(mixture))
        i += 1
    return password


if __name__ == "__main__":
    """ validate the user argument and call the paswdGen function """
    while True:
        print("Type <quit> to exit the program")
        userInput = input("Enter password length: ")
        if userInput == 'quit':
            break
        if not userInput.isdigit():
            print("*** password length must be an integer ***")
            continue
        print(f'\nYour password is: {paswdGen(int(userInput))}\n')
