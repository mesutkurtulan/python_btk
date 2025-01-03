#Value Types => string, integer, float
a = 5
b = 15

a = b

b = 25
print(a)    # 15
print(b)    # 25

# Reference Types => list, dictionary, set
c = [1, 2, 3, 4, 5]
d = [6, 7, 8, 9, 10]

c = d

d[0] = 11

print(c)    # [11, 7, 8, 9, 10]
print(d)    # [11, 7, 8, 9, 10]
