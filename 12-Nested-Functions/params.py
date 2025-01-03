def toplama(a,b):
    return a + b

def cikarma(a,b):
    return a - b

def carpma(a,b):
    return a * b

def bolme(a,b):
    if b == 0:
        raise ValueError("Bölünen sayı 0 olamaz!")
    return a / b

def islem(f1,f2,f3,f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(2, 3))
    elif islem_adi == "cikarma":
        print(f2(5, 3))
    elif islem_adi == "carpma":
        print(f3(4, 2))
    elif islem_adi == "bolme":
        print(f4(10, 2))
    else:
        raise ValueError("Geçersiz islem_adi!")

islem(toplama, cikarma, carpma, bolme, "toplama")   # 5
islem(toplama, cikarma, carpma, bolme, "cikarma")   # 2
islem(toplama, cikarma, carpma, bolme, "carpma")    # 8
islem(toplama, cikarma, carpma, bolme, "bolme")     # 5
