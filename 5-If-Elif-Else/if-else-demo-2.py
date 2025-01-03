# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
number = int(input('Number: '))
if 0 <= number <= 100:
    print(f'{number} is between 0 and 100.')
else:
    print(f'{number} is not between 0 and 100.')

# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
number = int(input('Number: '))
if number % 2 == 0 and number > 0:
    print(f'{number} is a positive even number.')
else:
    print(f'{number} is not a positive even number.')

# 3- Email ve parola bilgileri ile giriş kontrolü yapınız.
name = int(input('Name: '))
password = int(input('Password: '))

if name.lower().strip() == "jane" and password == "Qwerty123":
    print("Welcome, Jane!")
elif name.lower().strip() == "jane":
    print("Wrong User name!")
elif password != "Qwerty123":
    print("Wrong Password!")
else:
    print("Wrong User name and Password!")

# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
number_1 = input("Enter number 1: ")
number_2 = input("Enter number 2: ")
number_3 = input("Enter number 3: ")

if int(number_1) > int(number_2) and int(number_1) > int(number_3):
    print(f"{number_1} is the biggest number.")
elif int(number_2) > int(number_1) and int(number_2) > int(number_3):
    print(f"{number_2} is the biggest number.")
elif int(number_3) > int(number_1) and int(number_3) > int(number_2):
    print(f"{number_3} is the biggest number.")
else:
    print("Some or All numbers are equal.")

'''
5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
   Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
   a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
   b-) Finalden 70 alındığında ortalamanın önemi olmasın.
'''
vize1 = float(input("Vize 1 notu: "))
vize2 = float(input("Vize 2 notu: "))
final = float(input("Final notu: "))
ortalama = ((((vize1 + vize2)/2)*0.6) + (final*0.4))

if ortalama >= 50 and final >= 50:
    print("Geçtiniz!")
elif final >= 70:
    print("Geçtiniz!")
else:
    print("Kaldınız!")

'''
6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
   Formül: (Kilo / boy uzunluğunun karesi)
   Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
   0-18.4    => Zayıf 
   18.5-24.9 => Normal  
   25.0-29.9 => Fazla Kilolu
   30.0-34.9 => Şişman (Obez)
'''
name = input("Name: ")
weight = float(input("Weight: "))
height = float(input("Height: "))

indeks = weight / ((height/100) ** 2)

if 0 <= indeks <= 18.4:
    print(f"{name}, Your BMI: {indeks} and you are underweight.")
elif 18.5 <= indeks <= 24.9:
    print(f"{name}, Your BMI: {indeks} and you are normal.")
elif 25.0 <= indeks <= 29.9:
    print(f"{name}, Your BMI: {indeks} and you are overweight.")
elif 30.0 <= indeks <= 34.9:
    print(f"{name}, Your BMI: {indeks} and you are obese.")
else:
    print(f"{name}, Your BMI: {indeks} and you are severely obese.")