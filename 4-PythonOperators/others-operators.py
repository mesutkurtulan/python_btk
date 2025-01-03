# Identity Operator: is
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)   # True
print(x == z)   # True
print(y == z)   # True

# is checking address
print(x is y)   # True
print(x is z)   # False
print(y is z)   # False


x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)       # True
print(x is y)       # False
print(x is not y)   # True

# Membership Operator: in

x = ['apple','banana']
print('banana' in x)    # True

name = 'Çınar'
print('a' in name)      # True
print('a' not in name)  # False