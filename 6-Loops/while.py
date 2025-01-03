x = 0
while x <= 100:
    if x % 2 == 0:
        print(x)
    x += 1

name = ""
while not name.strip():
    name = input("Enter your name: ")

print(f"Hello {name.strip()}")
