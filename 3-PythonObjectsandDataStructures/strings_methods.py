message = 'Hello There. My name is John Doe'
print(message)                  #Hello There. My name is John Doe

messages = message.split()
print(messages)                 # ['Hello', 'There.', 'My', 'name', 'is', 'John', 'Doe']
messages = message.split()
print(messages)                 # ['Hello', 'There.', 'My', 'name', 'is', 'John', 'Doe']
print(' '.join(messages))       # Hello There. My name is John Doe

print("------")

print(message.upper())      # HELLO THERE. MY NAME IS JOHN DOE
print(message.lower())      # hello there. my name is john doe
print(message.title())      # Hello There. My Name Is John Doe
print(message.capitalize()) # Hello there. my name is john doe
print(message.swapcase())   # hELLO tHERE. mY NAME IS jOHN dOE

print("------")

print(" Hello World ".strip())  #Hello World

print("------")

print(message.find("John")) # 24
print(message.find("Jane")) # -1

print("------")

print(message.startswith("Hello"))  # True
print(message.endswith("Doe "))     # False

print("------")

print(message.replace("John", "Jane"))  # Hello There. My name is Jane Doe

print("------")

print(message.center(50,'_'))   # _________Hello There. My name is John Doe_________
