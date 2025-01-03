class Person:
    # Class Attributes
    address = "no information"

    # Constructor
    def __init__(self, name, birthday, ):

        # Object Attributes
        self.name = name
        self.birthday = birthday


    # Methods
    def intro(self):
        print("Hello There. I am", self.name)

    def calculateAge(self):
        return 2024- self.birthday

person_1= Person(name="Jane", birthday=1980)
person_1.intro()    # Hello There. I am Jane
person_1_Age = person_1.calculateAge()
print(person_1_Age) # 44

class Circle:

    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def calculatePerimeter(self):
        return self.radius * 2 * self.pi

    def calculateArea(self):
        return self.pi * (self.radius ** 2)

circle1 = Circle()
circle2 = Circle(5)

print(f"circle1; perimeter: {circle1.calculatePerimeter()}, area: {circle1.calculateArea()}")    # circle1; perimeter: 6.28, area: 3.14
print(f"circle1; perimeter: {circle2.calculatePerimeter()}, area: {circle2.calculateArea()}")    # circle1; perimeter: 31.400000000000002, area: 78.5