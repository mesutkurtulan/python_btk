def greeting(name):
    print("Hello", name)

greeting("Ali") # Hello Ali
print(greeting) # <function greeting at 0x10f9972e0>

# Encapsulation
def outer(num1):
    print("outher")
    def inner(num1):
        print("inner")
        return num1 + 1
    num2 = inner(num1)
    print(num1, num2)

outer(10)
'''
outher
inner
10 11
'''

def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Number must be an integer")

    if not number >= 0:
        raise ValueError("Number must be non-negative")
    
    def inner_factorial(number):
        if number <= 0:
            return 1

        return number * inner_factorial(number - 1)

    return inner_factorial(number)

print(factorial(5)) # 120