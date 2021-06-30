# Resolve the problem!!
import string
import random
SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')
NUMB = list('0123456789')
c=[]
k=[]
MAY=[]
MIN=[]
#Con el metodo chr, convierto de valores enteros a su equivalente en la tabla ASCII
for i in range(65,91):
    k=chr(i)
    MAY.append(k)
for i in range(97,123):
    z=chr(i)
    MIN.append(z)
MIN= list ("".join(MIN))
MAY= list ("".join(MAY))

def generate_password():
    password=[]
    m=0
    while m<12:
        a=random.choice(SYMBOLS)
        m+=1
        password.append(a)
        b=random.choice(MAY)
        m+=1
        password.append(b)
        c=random.choice(MIN)
        m+=1
        password.append(c)
        d=random.choice(NUMB)
        m+=1
        password.append(d)

    print(password)
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