# Methods
# bir sınıf içerisinde oluşturulan bir function'dır
list = [1,2,3]
list.append(4) # this is a method

# Functions

def sayHello(name = "User"):
    return f"Hello {name}"

print(sayHello("Şakir"))  # Hello Şakir

print(sayHello())  # Hello User

def total(num1, num2):
    return num1 + num2

print(total(5,7))   # 12

def ageCalculator(birthYear):
    '''
    DOCSTRING: Calculate your age based on 2025
    INPUT: Birth Year
    OUTPUT: Age
    '''
    return 2025 - birthYear

print(ageCalculator(2017))  # 8
print(help(ageCalculator))
'''
    DOCSTRING: Calculate your age based on 2025
    INPUT: Birth Year
    OUTPUT: Age
'''