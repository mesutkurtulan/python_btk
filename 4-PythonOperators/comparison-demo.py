# 1- Girilen 2 sayıdan hangisi büyüktür ?

a = int(input("Number 1: "))
b = int(input("Number 2: "))

print(f"a: {a} b: {b} den büyük müdür?: {a>b}")

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

a = float(input("1. vize notu: "))
b = float(input("1. vize notu: "))
c = float(input("1. vize notu: "))
result = (((a+b)/2) * 0.6) + (c * 0.4)
print(f"Not ortalamanız: {result} ve dersten geçtiniz mi? {result>=50}")

# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

a = int(input("Sayı giriniz: "))
print(f"Girilen sayı {a} çift mi? {(a%2)==0}")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.

a = int(input("Sayı giriniz: "))
print(f"Girilen sayı {a} pozitif mi? {a>=0}")

# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
#    (email: email@sadikturan.com parola:abc123)

email = "email@sadikturan.com"
parola = "abc123"

a = input("Enter Email: ")
b = input("Enter Password: ")

isEmailCorrect = email == a.lower().strip()
isPasswordCorrect = email == b.lower().strip()

print(f"Email doğru mu: {isEmailCorrect}, Password doğru mu: {isPasswordCorrect}")