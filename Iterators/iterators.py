liste1 = [1,2,3,4,5]

iterator = iter(liste1)

print(next(iterator))   # 1
print(next(iterator))   # 2
print(next(iterator))   # 3
print(next(iterator))   # 4
print(next(iterator))   # 5

iterator = iter(liste1)

'''
for i in liste1:
    print(i)

'''

while True:
    try:
        print(next(iterator))
    except StopIteration:
        break

class MyNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= self.end:
            x = self.start
            self.start += 1
            return x
        else:
            raise StopIteration

liste2 = MyNumbers(10,20)

for x in liste2:
    print(x)
    
myiter = iter(liste2)
print(next(myiter))
    