'''
x = 10

if x > 5:
    raise Exception("x 5 den büyük değer alamaz.") # Exception: x 5 den büyük değer alamaz.
'''

def check_password(password):
    if len(password) < 8:
        raise ValueError("Parola en az 8 karakter uzunluğunda olmalıdır.")
    elif not any(char.isupper() for char in password):
        raise ValueError("Parola en az bir büyük harf içermelidir.")
    elif not any(char.islower() for char in password):
        raise ValueError("Parola en az bir küçük harf içermelidir.")
    elif not any(char.isdigit() for char in password):
        raise ValueError("Parola en az bir rakam içermelidir.")
    elif not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>/?" for char in password):
        raise ValueError("Parola en az bir özel karakter içermelidir.")
    else:
        print("Parola geçelidir")

password1 = "Qwerty!"
password2 = "Qwertyuiop!"
password3 = "qwerty123!"
password4 = "QWERTYUIOP"
password5 = "Qwerty123"
password6 = "Qwerty123!"

try:
    check_password(password1)    # ValueError: Parola en az 8 karakter uzunluğunda olmalıdır.
    check_password(password2)    # ValueError: Parola en az bir rakam içermelidir.
    check_password(password3)    # ValueError: Parola en az bir büyük harf içermelidir.
    check_password(password4)    # ValueError: Parola en az bir küçük harf içermelidir.
    check_password(password5)    # ValueError: Parola en az bir özel karakter içermelidir.
    check_password(password6)    # Parola geçelidir
except ValueError as e:
    print(e)

class Person:
    def __init__(self, name, year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor.")
        else:
            self.name = name

p = Person("Aliiiiiiiiiiii", 1989)