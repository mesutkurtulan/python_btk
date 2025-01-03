# Globan Scope
x = "global"

def function():
    # Local Scope
    x = "local"
    print(x)

function()  # local
print(x)    # global

x = 50

def test():
    global x # use global scope and change inside the function
    print(f"x: {x}")    # x: 50
    x = 100
    print(f"x: {x}")    # x: 100

test()
print(x)    # 100