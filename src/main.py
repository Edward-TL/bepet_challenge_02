# Resolve the problem!!
from random import randrange as rr
import string


SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here

    chars = [string.ascii_uppercase, string.ascii_lowercase, string.digits, SYMBOLS]
    chars2 = chars.copy()

    password = ""

    for i in range(rr(8, 17)):
        if len(chars2)!= 0:
            pass
        else:
            chars2 = chars.copy()

        ind = rr(len(chars2))
        password += chars2[ind][rr(len(chars2[ind]))] # Since it's a nested list, I need two random indexes
        chars2.pop(ind)

    return password


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
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
