'''
    This program will create for you how many passwords you want
    and you can also decide how many characters goes in your passwords.
    Enjoy it!
'''

# To choose a random character, we'll need to import the random module.

import random

# This variable has got all characters that the program will use to make your password.
chars = "abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ1234567890!?,.-"

# These inputs is where you dicede the length of the password and how many of them you want.   
length = int(input("Password length: "))
how_many = int(input("How many passwords do you want: "))


for p in range(how_many):
    password = ''

    for c in range(length):
        password += random.choice(chars)

    print(password)