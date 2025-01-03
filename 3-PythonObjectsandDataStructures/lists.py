my_list = [1,2,3]
my_list = [4, "A", True]

print(my_list)  # [4, 'A', True]

list_1 = ["one", "two", "three"]
list_2 = ["four", "five", "six"]
num_list = list_1 + list_2
print(num_list)         # ['one', 'two', 'three', 'four', 'five', 'six']
print(num_list[2])      # three
print(len(num_list))    # 6

userA = ['John', 40]
userB = ['Jane', 30]
users = userA + userB
print(users)            #  ['John', 40, 'Jane', 30]
users_list = [userA, userB]
print(users_list)       # [['John', 40], ['Jane', 30]]
print(users_list[0])    # ['John', 40]
print(users_list[0][0]) # John