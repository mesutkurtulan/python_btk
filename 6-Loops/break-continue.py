name = "Jone Doe"

for letter in name:
    if letter == " ":
        continue
    print(letter.lower())

x = 0
total = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    total += x
print("total", total)