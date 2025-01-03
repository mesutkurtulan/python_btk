# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme
#    durumunu kontrol ediniz. Ehliyet alma koşulu en az 18 ve eğitim durumu
#    lise ya da üniversite olmalıdır.
import datetime

name = input('Name: ').lower().strip()
age = int(input('Age: '))
education = input('Education: ').lower().strip()

if age >= 18 and (education == 'lise' or education == 'üniversite'):
    print(f'{name}, you are eligible for driver license.')
elif age < 18:
    print(f'{name}, you are not eligible for driver license because of your age {age}')
elif education != "lise" and education != "Üniversite":
    print(f'{name}, you are not eligible for driver license because of your education {education}')

# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
#    not aralığına karşılık gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5

first_note = float(input('First note: '))
second_note = float(input('Second note: '))
third_note = float(input('Third note: '))

average_note = (first_note + second_note + third_note) / 3

if 0 <= average_note <= 24:
    print('Range: 0')
elif 25 <= average_note <= 44:
    print('Range: 1')
elif 45 <= average_note <= 54:
    print('Range: 2')
elif 55 <= average_note <= 69:
    print('Range: 3')
elif 70 <= average_note <= 84:
    print('Range: 4')
elif 85 <= average_note <= 100:
    print('Range: 4')
else:
    print('invalid notes')

# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
#    göre hesaplayınız.
#    1. Bakım => 1. yıl
#    2. Bakım => 2. yıl
#    3. Bakım => 3. yıl
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.
#    (simdi) - (2018/8/1) => gün

date = input("On what date did your vehicle enter traffic? (2019/8/9) -> (year/month/day)")
date_format = date.split("/")
enterTime = datetime.datetime(int(date_format[0]),int(date_format[1]),int(date_format[2]))
now = datetime.datetime.now()
difference = now - enterTime

if difference.days < 365:
    print("Go to the service for 1st time")
elif 365 < difference.days < 365*2:
    print("Go to the service for 2nd time")
elif 365*2 < difference.days < 365*3:
    print("Go to the service for 3rd time")
else:
    print("You should not go to the service")
