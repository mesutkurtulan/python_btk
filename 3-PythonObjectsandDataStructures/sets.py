fruits = {"orange", "apple", "banana"}
print(fruits)   # {'orange', 'apple', 'banana'}

# print(fruits[0]) # 'set' object is not subscriptable

for fruit in fruits:
    print(fruit)    # banana orange apple

fruits.add("cherry")
fruits.update(["mango", "grape"])
print(fruits) # {'banana', 'orange', 'apple', 'mango', 'cherry', 'grape'}
fruits.remove("cherry")
print(fruits) # {'grape', 'banana', 'apple', 'orange', 'mango'}
fruits.discard('mango')
print(fruits) # {'orange', 'apple', 'banana', 'grape'}
fruits.pop()
print(fruits) # {'orange', 'grape', 'apple'}
fruits.clear()
print(fruits) # set()

print("--------------------------------")

my_list = [1, 2, 5, 4, 4, 3, 2]
print(my_list)      # [1, 2, 5, 4, 4, 3, 2]
print(set(my_list)) # {1, 2, 3, 4, 5}