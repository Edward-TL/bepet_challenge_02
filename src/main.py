# Resolve the problem!!
import string

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    con1 = input("Digite una contraseña nueva: ")
    con2 = input("Confirmar contraseña: ")
    if con1 != con2:
      print("Las contraseñas no coinciden, intente de nuevo\n\n")
      generate_password()
    if len(con1) < 8 and len(con1) > 16:
      print("La contraseña es muy corta o muy larga, intente de nuevo\n\n")
      generate_password()
    else:
      return con1

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
        print('Insecure Password, Intente de nuevo\n')
        run()


if __name__ == '__main__':
    run()
