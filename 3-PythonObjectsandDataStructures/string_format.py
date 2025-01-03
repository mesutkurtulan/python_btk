name = "John"
lastname = "Doe"
age = 40

print("My name is " + name + " " + lastname + ", and I am " + str(age) + " years old.")  # My name is John Doe, and I am 40 years old.

print("My name is", name, lastname, "and I am", age, "years old.")                       # My name is John Doe, and I am 40 years old.

print("My name is {} {}, and I am {} years old.".format(name, lastname, age))       # My name is John Doe, and I am 40 years old.
print("My name is {0} {1}, and I am {2} years old.".format(name, lastname, age))       # My name is John Doe, and I am 40 years old.
print("My name is {n} {s}, and I am {a} years old.".format(n=name, s=lastname, a=age))      # My name is John Doe, and I am 40 years old.

print(f"My name is {name} {lastname}, and I am {age} years old.")                       # My name is John Doe, and I am 40 years old.

result = 200/700
print("the result is {}".format(result))            # the result is 0.2857142857142857
print("the result is {r:1.3}".format(r=result))     # the result is 0.286
print("the result is {}")