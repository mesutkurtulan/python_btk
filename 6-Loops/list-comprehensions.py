from selectors import SelectSelector

for x in range(10):
    print(x)

numbers = [x for x in range(10)]
print(numbers)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = [x*x for x in range(10) if x % 3 == 0]
print(numbers) # [0, 9, 36, 81]

myString = "Hello"
myList =  []

for letter in myString:
    myList.append(letter)

print(myList)   # ['H', 'e', 'l', 'l', 'o']

myList = [letter for letter in myString]
print(myList)   # ['H', 'e', 'l', 'l', 'o']

years = [1983, 1999, 2008, 1956, 1986]
ages = [2024-year for year in years]
print(ages) # [41, 25, 16, 68, 38]

results = [x if x % 2 == 0 else '*' for x in range(1,10)]
print(results)  # ['*', 2, '*', 4, '*', 6, '*', 8, '*']

results = []

for x in range(3):
    for y in range(3):
        results.append((x,y))

print(results)  # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

results = [(x,y) for x in range(3) for y in range(3)]
print(results) # [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]