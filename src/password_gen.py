import random

NUMBERS = "0123456789"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SYMBOLS = "!@#$%^&*()-_=+~[]/;[]|}{>?<"
CHARS = NUMBERS + LOWERCASE + UPPERCASE + SYMBOLS


def gen_pwd(length=64, characters=CHARS):
    pwd = []
    for count in range(length):
        choice = random.choice(characters)
        pwd.append(choice)
        del choice
    return ''.join(str(item) for item in pwd)
