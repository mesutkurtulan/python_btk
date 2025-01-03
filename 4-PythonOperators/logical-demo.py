# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
from operator import index

number = int(input('Enter Number: '))
print(f"Girilen sayı {number} 0-100 arasında mı: {0 <= number <= 100}")

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
number = int(input('Enter Number: '))
print(f"Girilen sayı {number} pozitif çift sayı mı: {0 < number and number % 2 == 0}")

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
email = 'email@sadikturan.com'
password = 'abc123'

newEmail = input('Email: ')
newPassword = input('Password: ')

print(f"Email {newEmail} is correct: {email == newEmail.lower().strip()} and Password {newPassword}is correct: {password == newPassword.lower().strip()}")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
number1 = int(input('Number 1: '))
number2 = int(input('Number 2: '))
number3 = int(input('Number 3: '))

print(f"Number 1 is bigger: {number1 > number2 and number1 > number3}")
print(f"Number 2 is bigger: {number2 > number1 and number2 > number3}")
print(f"Number 3 is bigger: {number3 > number2 and number3 > number1}")

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vise1 = float(input("Vize 1 notu: "))
vise2 = float(input("Vize 2 notu: "))
final = float(input("final notu: "))
ortalama = ((((vise1 + vise2)/2)*0.6) + (final*0.4))
print(f"Geçti mi: {ortalama>=50 and final>=50}")
print(f"Geçti mi: {ortalama>=50 or final>=70}")

# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf
#    18.5-24.9 => Normal
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)

name = input("Name: ")
weight = float(input("Weight: "))
height = float(input("Height: "))

index = weight / ((height/100) ** 2)
low = (0 <= index <= 18.4)
mid = (18.5 <= index <= 24.9)
high = (25.0 <= index <= 29.9)
veryHigh = (30.0 <= index <= 34.9)

print(f"{name} weight index: {index} and weight index is Low: {low}")
print(f"{name} weight index: {index} and weight index is Medium: {mid}")
print(f"{name} weight index: {index} and weight index is High: {high}")
print(f"{name} weight index: {index} and weight index is Very High: {veryHigh}")

