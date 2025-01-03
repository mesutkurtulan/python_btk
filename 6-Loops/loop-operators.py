# range

numbers = [1,2,3,4,5,6,7,8,9]

for i in numbers:
    print(i)

for i in range(1,10,2):
    print(i)

print(list(range(0,10,2)))  # [0, 2, 4, 6, 8]

# enumerate

index = 0
greetings = "Hello"

for letter in greetings:
    print(f"Index: {index}, Letter: {letter}")
    index += 1
'''
Index: 0, Letter: H
Index: 1, Letter: e
Index: 2, Letter: l
Index: 3, Letter: l
Index: 4, Letter: o
'''

greeting = "Hello"
for index, letter in enumerate(greeting):
    print(f"Index: {index}, Letter: {letter}")

'''
Index: 0, Letter: H
Index: 1, Letter: e
Index: 2, Letter: l
Index: 3, Letter: l
Index: 4, Letter: o
'''

greet = "Hello"
for item in enumerate(greet):
    print(item)

'''
(0, 'H')
(1, 'e')
(2, 'l')
(3, 'l')
(4, 'o')
'''

# zip

list1= [1,2,3,4,5]
list2=["a","b","c","d","e"]
list3= [True,False,True,False,True]
zip_list= zip(list1, list2, list3)
print(list(zip_list))   # [(1, 'a', True), (2, 'b', False), (3, 'c', True), (4, 'd', False), (5, 'e', True)]

for item in list(zip(list1, list2, list3)):
    print(item)
'''
(1, 'a', True)
(2, 'b', False)
(3, 'c', True)
(4, 'd', False)
(5, 'e', True)
'''

for a,b,c in list(zip(list1, list2, list3)):
    print(a,b,c)
'''
1 a True
2 b False
3 c True
4 d False
5 e True
'''