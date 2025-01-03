website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
print(len(course))  # 65

# 2- 'website' içinden www karakterlerini alın.
print(website[7:10])    # www

# 3- 'website' içinden com karakterlerini alın.
print(website[22:]) # com

# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
print(course[:15], course[-15:])    # Python Kursu: B riniz (40 saat)

# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
print(course[::-1]) # )taas 04( zinirebheR amalmargorP nohtyP anoS natşaB :usruK nohtyP

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
#    'Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis.'
name = "Bora"
lastname = "Yılmaz"
age = 32
occupation = "mühendis"

print('Benim adım', name, lastname, 'Yaşım', age, 've mesleğim', occupation)    # Benim adım Bora Yılmaz Yaşım 32 ve mesleğim mühendis
print('Benim adım {} {}, Yaşım {} ve mesleğim {}'.format(name, lastname, age, occupation))    # Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis
print(f'Benim adım {name} {lastname}, Yaşım {age} ve mesleğim {occupation}')    # Benim adım Bora Yılmaz, Yaşım 32 ve mesleğim mühendis


# 7-Functions 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
text = 'Hello world'
print(f'{text[:6]}W{text[-4:]}')    # Hello World
print(text.replace('w', 'W')) # Hello World

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
print('abc ' * 3) # abc abc abc