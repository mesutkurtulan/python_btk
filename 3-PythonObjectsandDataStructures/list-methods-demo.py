names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)    # ['Ali', 'Yağmur', 'Hakan', 'Deniz', 'Cenk']

# 2-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0, 'Sena')
print(names)    # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Deniz', 'Cenk']

# 3-  "Deniz" ismini listeden siliniz.
names.remove('Deniz')
print(names)    # ['Sena', 'Ali', 'Yağmur', 'Hakan', 'Cenk']

# 4-  "Hakan" isminin indeksi nedir ?
print(names.index("Hakan")) # 3

# 5-  "Ali" listenin bir elemanı mıdır ?
print("Ali" in names) # True

# 6-  Liste elemanlarını ters çevirin.
names.reverse()
print(names)    # ['Cenk', 'Hakan', 'Yağmur', 'Ali', 'Sena']

# 7-Functions  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)    # ['Ali', 'Cenk', 'Hakan', 'Sena', 'Yağmur']

# 8-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort(reverse=True)
print(years)    # [2010, 2000, 1998, 1998, 1987]

# 9-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia"
strList = str.split(",")
print(strList)  # ['Chevrolet', 'Dacia']

# 10- years dizisinin en büyük ve en küçük elemanı nedir ?
print(min(years))   # 1987
print(max(years))   # 2000

# 11- years dizisinde kaç tane 1998 değeri vardır ?
print(years.count(1998))    # 2

# 12-Nested-Functions years dizisinin tüm elemanlarını siliniz.
years.clear()

# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

brands = []

brand = input("Marka: ")
brands.append(brand)

brand = input("Marka: ")
brands.append(brand)

brand = input("Marka: ")
brands.append(brand)

print(brands)
