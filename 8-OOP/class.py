# class

class Person:
    pass # placeholder

    # Class Attributes
    address = "no information"

    def __init__(self, name, birthday, ): # Constructor
        # Object Attributes
        self.name = name
        self.birthday = birthday

    # Methods



# object (instance)
person_1 = Person("Jane", 1990)

# updating
person_1.name = 'John'
person_1.address = 'NY'

# accessing object attributes
print(f'p1: name: {person_1.name} year: {person_1.birthday} address: {person_1.address}')   # p1: name: Jane year: 1990 address: no information

print(person_1)         # <__main__.Person object at 0x102021010>
print(type(person_1))   # <class '__main__.Person'>