def usalma(number):

    def inner(power):
        return number ** power

    return inner

two = usalma(2)
print(two) # <function usalma.<locals>.inner at 0x100267560>
print(two(3)) # 8

def yetki_Sorgula(page):
    def inner(role):
        if role == "Admin":
            return f"{role} yetkiniz var. {page} sayfasini goruntuleyebilirsiniz."
        else:
            return f"{role} yetkiniz yok. {page} sayfasini goruntuleyemezsiniz."
    return inner

user_1 = yetki_Sorgula("Product_Edit")
print(user_1("Admin"))  # Admin yetkiniz var. Product_Edit sayfasini goruntuleyebilirsiniz.

def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam

    def carpma(*args):
        carpim = 1
        for i in args:
            carpim*=i
        return carpim

    if islem_adi == "toplama":
        return toplam
    else:
        return carpma


toplama = islem("toplama")
print(toplama(1,3,5,6,7))   # 22

carpma = islem("carpma")
print(carpma(1,2,3,6,4))    # 144
