# Inheritance (Kalıtım): Miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

class Person:
    def __init__(self, fName, lName):
        self.firstName = fName
        self.lastName = lName
        print("Person created")     # Person created

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fName, lName, number):
        Person.__init__(self, fName, lName)       # Person created
        self.studentNumber = number
        print("Student created")    # Student created

    # Overriding
    def who_am_i(self):
        print("I am a student")

class Teacher(Person):
    def __init__(self, fName, lName, branch):
        # Person.__init__(self, fName, lName)       # Person created
        super().__init__(fName, lName)              # Person created
        self.branch = branch
        print("Teacher created")    # Teacher created

    # Overriding
    def who_am_i(self):
        print(f"I am a {self.branch} teacher")

p1 = Person("John", "Doe")
print(p1.firstName, p1.lastName)        # John Doe
p1.who_am_i()                           # I am a person

s1 = Student("Jane", "Doe", 1001)
print(s1.firstName, s1.lastName, s1.studentNumber)          # Jane Doe 1001
s1.who_am_i()                                               # I am a student

t1 = Teacher("Richard", "Roe", "Math")
print(t1.firstName, t1.lastName, t1.branch)         # Richard Roe Math
t1.who_am_i()                                       # I am a Math teacher