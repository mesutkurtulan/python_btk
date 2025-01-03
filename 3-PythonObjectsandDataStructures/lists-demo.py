# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ['Bmw','Mercedes','Opel','Mazda']

# 2-  Liste Kaç elemanlıdır ?
print(len(arabalar))    # 4

# 3-  Listenin ilk ve son elemanı nedir ?
print(arabalar[0], arabalar[-1])    # Bmw Mazda

# 4-  Mazda değerini Toyota ile değiştirin.
arabalar[arabalar.index("Mazda")] = "Toyota"
print(arabalar) # ['Bmw', 'Mercedes', 'Opel', 'Toyota']

# 5-  Mercedes listenin bir elemanı mıdır ?
print("Mercedes" in arabalar)       # True
print(arabalar.index("Mercedes"))   # 1

# 6-  Listenin -2 indeksindeki değer nedir ?
print(arabalar[-2])     # Opel

# 7-Functions  Listenin ilk 3 elemanını alın.
print(arabalar[0:3])    # ['Bmw', 'Mercedes', 'Opel']

# 8-  Listenin son 2 elemanı yerine "Totoya" ve "Renault" değerlerini ekleyin.
arabalar[-2] = "Totoya"
arabalar[-1] = "Renault"
#or
#arabalar[-2:0] = ["Totoya", "Renault"]
print(arabalar) # ['Bmw', 'Mercedes', 'Totoya', 'Renault']


# 9-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
arabalar.append("Audi")
arabalar.append("Nissan")
print(arabalar) # ['Bmw', 'Mercedes', 'Totoya', 'Renault', 'Audi', 'Nissan']

# 10- Listenin son elemanını silin.
del arabalar[-1]
print(arabalar) # ['Bmw', 'Mercedes', 'Totoya', 'Renault', 'Audi']

# 11- Liste elemanlarını tersten yazdırınız.
print(arabalar[::-1])   # ['Audi', 'Renault', 'Totoya', 'Mercedes', 'Bmw']

# 12-Nested-Functions Aşağıdaki verileri bir liste içinde saklayınız.

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90)
studentA = ["Yiğit", "Bilgi", 2010, [70, 60, 70]]
studentB = ["Sena", "Turan", 1999, [80, 80, 70]]
studentC = ["Ahmet", "Turan", 1998, [80, 70, 90]]

# 13- Liste elemanlarını ekrana yazdırınız.
print(studentA) # ['Yiğit', 'Bilgi', 2010, [70, 60, 70]]
print(studentB) # ['Sena', 'Turan', 1999, [80, 80, 70]]
print(studentC) # ['Ahmet', 'Turan', 1998, [80, 70, 90]]