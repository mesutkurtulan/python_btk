liste = ["1","2","5a","10b","abc","10","50"]

# 1: Liste elemanları içindeki sayısal değerleri bulunuz.
numbers = []
for list in liste:
    if list.isdigit():
        numbers.append(int(list))

print(numbers)  # [1, 2, 10, 50]

numbers = []
for list in liste:
    try:
        numbers.append(int(list))
    except ValueError:
        continue

print(numbers)  # [1, 2, 10, 50]

# 2: Kullanıcı 'q' değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz aksi halde hata mesajı yazın.

while True:
    text = input("Please enter any number or type 'q' for exit: ")
    if text.lower().strip() == "q":
        print("Goodbye")
        break

    try:
        number = float(text)
        print(f"Number: {number}")
    except ValueError as ex:
        print('Your text is not including number, please try again', ex)
        continue

# 3: Girilen parola içinde türkçe karakter hatası veriniz.

def checkPassword(password):
    turkish_chars = "ŞşçÇğĞüÜöÖıİ"
    for char in turkish_chars:
        if char in password:
            raise TypeError("Password cannot include Turkish characters")
        else:
            pass

    print("Your password is valid")

password = input("please enter password with english character: ")
checkPassword(password)

# 4: Faktöriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajları verin.

def factorial(number):
    if not isinstance(number, int) or number < 0:
        raise ValueError("The input must be a non-negative integer")
    elif number == 0:
        return 1
    else:
        return number * factorial(number - 1)

number = input("Please enter a number:")
fact = factorial(number)
print(fact)