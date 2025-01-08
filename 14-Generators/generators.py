def cube():
    result = []

    for i in range(5):
        result.append(i**3)
    return result

print(cube())  # [0, 1, 8, 27, 64]

######

def cube():
    for i in range(5):
        yield i**3

for i in cube():
    print(i)    # 0 1 8 27 64

liste = [i**3 for i in range(5)]
print(liste) # [0, 1, 8, 27, 64]

liste = (i**3 for i in range(5))
print(liste) # <generator object <genexpr> at 0x10c946a80>

for i in liste:
    print(i)    # 0 1 8 27 64