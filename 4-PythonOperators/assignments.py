x = 5
y = 10
z = 15

x, y, z = 5, 10, 15

z, y, x = x, y, z

x = x + 5
x -= 5
print(x, y, z)  # 15 10 5

values = 1,2,3 # tuples
print(values)   # (1, 2, 3)
print(type(values)) # <class 'tuple'>

x, y, z = values
print(x, y, z) # 1 2 3

values = 1,2,3,4,5 # tuples
print(values)   # (1, 2, 3, 4, 5)
print(type(values)) # <class 'tuple'>

x, y, *z = values
print(x, y, z) # 1 2 [3, 4, 5]