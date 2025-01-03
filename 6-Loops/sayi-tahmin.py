'''
   1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile
   buldurmaya çalışın. (hak = 5)
   ** "random modülü" için "python random" şeklinde arama yapın.
   ** 100 üzerinden puanlama yapın. Her soru 20 puan.
   ** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
      üzerinden hesaplansın.
'''

import random
randomSayi = random.randint(1, 10)
hak = int(input("İstediğiniz hak sayısını giriniz: "))
i = 0

while i < hak:
    i += 1
    tahmin = int(input("1'den 10'a kadar olan sayıyı tahmin et: "))
    if tahmin == randomSayi:
        print(f"Tebrikler, {i} defada bildiniz. Toplam Puan {100 - ((i-1)*(100/i))}")
        break
    elif tahmin > randomSayi:
        print("Daha küçük bir sayı tahmin edin.")
    elif tahmin < randomSayi:
        print("Daha büyük bir sayı tahmin edin.")

    if i == hak:
        print(f"Kaybettiniz. Doğru sayı: {randomSayi}")

