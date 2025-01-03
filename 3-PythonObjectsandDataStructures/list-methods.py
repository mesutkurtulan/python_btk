numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ['a', 'g', 's', 'b', 'y', 'a', 's']

print(min(numbers)) # 1
print(max(numbers)) # 16

print(min(letters)) # a
print(max(letters)) # y

numbers.append(49)
print(numbers)  # [1, 10, 5, 16, 4, 9, 10, 49]
numbers.insert(3,78)
print(numbers)  # [1, 10, 5, 78, 16, 4, 9, 10, 49]

numbers.pop()
print(numbers)  # [1, 10, 5, 78, 16, 4, 9, 10]

numbers.pop(3)
print(numbers)  # [1, 10, 5, 16, 4, 9, 10]

numbers.remove(9)
print(numbers)  # [1, 10, 5, 16, 4, 10]

numbers.sort()
print(numbers)  # [1, 4, 5, 10, 10, 16]

print(letters)  # ['a', 'g', 's', 'b', 'y', 'a', 's']
letters.reverse()
print(letters)  # ['s', 'a', 'y', 'b', 's', 'g', 'a']
letters.sort()
print(letters)  # ['a', 'a', 'b', 'g', 's', 's', 'y']

print(numbers.count(10))    # 2
print(letters.count("s"))   # 2

numbers.clear()
print(numbers)  # []