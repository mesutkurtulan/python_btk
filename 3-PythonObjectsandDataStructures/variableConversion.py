'''
x = input("1. sayi gir: ")
y = input("2. sayi gir: ")

print(int(float(x) + float(y)))
'''
import math

x = 1               # integer
y = 2.3             # float
name = "Paul"       # string
isStudent = False   # boolean

x = float(x)    # float
print(x)        # 1.1
print(type(x))  # <class 'float'>

y = int(y)
print(y)        # 2
print(type(y))  # <class 'int'>

"""
isStudent = str(isStudent)
print(isStudent)
print(type(isStudent))
"""

isStudent = int(isStudent)
print(isStudent)
print(type(isStudent))

r = input("Çemberin yarıçapını giriniz: ")

print("Çemberin Çevresi", int(float(r))*2*(math.pi))
print("Çemberin Alanı", (int(float(r))*int(float(r)))*(math.pi))
