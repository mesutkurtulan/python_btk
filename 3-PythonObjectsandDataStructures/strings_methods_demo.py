website = "www.google.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


# 1-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
print(' Hello World '.strip())  # Hello World
print(' Hello World '.lstrip())  # Hello World
print(' Hello World '.rstrip())  # Hello World

# 2- 'www.google.com' içindeki google bilgisi haricindeki her karakteri silin.
print((website.lstrip("www.")).rstrip(".com"))   # google
print(website.strip("www.com"))   # google

# 3-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
print("course".lower()) # course

# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
print("website".count('a')) # 0

# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
print(website.startswith("www"))    # True
print(website.endswith("com"))  # True

# 6-  'website' içinde '.com' ifadesi var mı?
print(website.find('com'))  # 11
print(website.index('com')) # 11

# 7-Functions 'course' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
print(course.isalpha()) # False

# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
print("Content".center(50,"*")) # *********************Content**********************

# 9-  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
print(course.replace(' ','_')) # Python_Kursu:_Baştan_Sona_Python_Programlama_Rehberiniz_(40_saat)

# 10- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
print('Hello World'.replace("World", "There"))  # Hello There

# 11-  'course' karakter dizisini boşluk karakterlerinden ayırın.
print(course.split(" "))    # ['Python', 'Kursu:', 'Baştan', 'Sona', 'Python', 'Programlama', 'Rehberiniz', '(40', 'saat)']