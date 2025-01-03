def changeName(n):
    n = "ada"

name = "efe"
changeName(name)
print(name) # efe

def change(n):
    n[0] = "adana"

cities = ["ankara", "izmir", "hatay"]

change(cities[:]) # this slicing method creates new cities and don't touch the original cities list
print(cities)   # ['ankara', 'izmir', 'hatay']

change(cities)  # this method uses the address of the cities list and change the original cities list
print(cities)   # ['adana', 'izmir', 'hatay']

def add_1(a, b, c = 0):
    return sum((a, b, c))

print(add_1(2,5))         # 7
print(add_1(2,5,7))    # 14

def add_2(*params):
    return sum((params))

print(add_2(2,5))      # 7
print(add_2(2,5,7))    # 14

def add_3(*params): # params is tuple
    sum = 0

    for n in params:
        sum += n

    return sum

print(add_3(2,5))      # 7
print(add_3(2,5,7))    # 14

def displayUser(**args):    # args is dictionary
    for key, value in args.items():
        print(f"{key} is: {value}")


displayUser(name = "John", age = 39, city = "Ankara")
'''
name is: John
age is: 39
city is: Ankara
'''

displayUser(name = "Jane", age = 29, city = "Adana", phone = "12345")
'''
name is: Jane
age is: 29
city is: Adana
phone is: 12345
'''

displayUser(name = "Cane", age = 19, city = "Afyon", phone = "67890", email = "test@mail.com")
'''
name is: Cane
age is: 19
city is: Afyon
phone is: 67890
email is: test@mail.com
'''

def myFunctions(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunctions(1, 2, 3, 4, 5, name = "John", age = 39, city = "Ankara")
'''
1
2
(3, 4, 5)
{'name': 'John', 'age': 39, 'city': 'Ankara'}
'''