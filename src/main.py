# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
passw=[]

def generate_password(password):
    for i in range (3):
        password=random.choice(string.ascii_uppercase )
        passw.append(password)
        password=random.choice(string.ascii_lowercase)
        passw.append(password)
        password=random.choice(string.digits)
        passw.append(password)
        password=random.choice(SYMBOLS)
        passw.append(password)
    return passw


def validate(password):
    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password(passw)
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()