import math
import time


def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

def sayHello():
    print("Hello")

def sayGreeting():
    print("Greeting")

sayHello = my_decorator(sayHello)
sayHello()
'''
Before calling the function
Hello
After calling the function
'''

sayGreeting = my_decorator(sayGreeting)
sayGreeting()
'''
Before calling the function
Greeting
After calling the function
'''

@my_decorator
def sayGoodbye():
    print("Goodbye")

sayGoodbye()
'''
Before calling the function
Goodbye
After calling the function
'''

def calcalateTime(func):
    def inner(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        finish = time.time()
        print(f"Total time: {finish-start} seconds")
    return inner


def usAlma(a,b):
    start = time.time()
    print(math.pow(a,b))
    finish = time.time()
    print(f"total: {finish-start} seconds")

@calcalateTime
def factorial(a):
    print(math.factorial(a))

usAlma(2,3)
'''
8.0
total: 4.601478576660156e-05seconds
'''

factorial(4)
'''
24
total: 0.0003809928894042969seconds
'''