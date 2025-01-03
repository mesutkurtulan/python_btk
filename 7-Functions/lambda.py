def square_1(num):
    return num ** 2

def square_2(num): return num ** 2
result = square_2(2)
print(result)   # 4

numbers = [1,2,3,4,5,6,7,8,9]

result = list(map(square_2, numbers))   # [1, 4, 9, 16, 25, 36, 49, 64, 81]
print(result)

for number in map(square_2, numbers):
    print(number)   # 1, 4, 9, 16, 25, 36, 49, 64, 81

result = list(map(lambda num: num ** 2, numbers))
print(result)   # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# Lambda functions
square_3 = lambda num: num ** 2
result = list(map(square_3, numbers))
print(result)   # [1, 4, 9, 16, 25, 36, 49, 64, 81]

#filter functions

def check_even(num): return num % 2 == 0
result = list(map(check_even, numbers))
print(result)   # [False, True, False, True, False, True, False, True, False]
result = list(filter(check_even, numbers))
print(result)   # [2, 4, 6, 8]

result = list(filter(lambda num: num%2==0, numbers))
print(result)   # [2, 4, 6, 8]

check_even_lambda= lambda num: num%2==0
result = list(filter(check_even_lambda, numbers))
print(result)   # [2, 4, 6, 8]