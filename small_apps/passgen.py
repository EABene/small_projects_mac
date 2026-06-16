"""
TODO:
Change: Use secrets instead of random
Sauberere Logik
Jedes Zeichen mit gleicher Wahrscheinlichkeit, gepicked zu werden, und jeweils Fix UPPER, LOWER und DIGIT
Am besten eine V2 schreiben
"""

import secrets
import random
import string

# Note: lowercase_letters = string.ascii_lowercase
# Note: uppercase_letters = string.ascii_uppercase
upper_and_lowercase_letters = string.ascii_letters
digits = string.digits
extra_signs = string.punctuation

all_signs = upper_and_lowercase_letters + digits # optional: add extra_signs

eligible_signs = []
for sign in all_signs:
    eligible_signs.append(sign)

eligible_signs = list(all_signs)
secrets.SystemRandom().shuffle(eligible_signs) # kind of unecessary... More like superstition.


def passgen_part():
    password_part = []
    for sign in eligible_signs:
        checker = [1, 2, 3, 4, 5]
        check = secrets.choice(checker)
        if check == 1:
            password_part.append(sign)
            if len(password_part) == 6:
                break
    password_part.append("-")
    password_part_string = "".join(password_part)

    return password_part_string

def passgen():
    password = ""
    for loop in range(5):
        password = password + passgen_part()
    password = password[:-1]
    return password

# App Runtime

user_choice = input("Do you want to generate a safe password? Type: Go! >> ")
if user_choice == "Go!":
    user_choice = "y"
    while True:
        if user_choice == "y":
            print(passgen())
        else:
            print("Program exit.")
            break
        user_choice = input("Generate another? (y/n) >> ")
else: print("No password generated.")

