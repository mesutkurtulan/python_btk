x, y, z = 2, 5, 10

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir ?
a = int(input("Enter an integer: "))
b = int(input("Enter an integer: "))
print((a*b)-(x+y+z))

# 2- y' nin  x' e kalansız bölümünü hesaplayınız.
print(y//x) # 2

# 3- (x,y,z) toplamının mod 3' ü nedir ?
print((x+y+z)%3)    # 2

# 4- y' nin x. kuvvetini hesaplayınız.
print(y**x) # 25

# 5- x, *y, z = numbers işlemine göre z' nin küpü kaçtır ?
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
print(z**3) # 216

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır ?
x, *y, z = numbers
print(y[0]+y[1]+y[2])   # 22