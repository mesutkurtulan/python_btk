mylist = [1,2,3]

print(len(mylist))  # 3

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration

    def __str__(self):
        return f"{self.title} - Directed by {self.director}, {self.duration} minutes long."

    def __len__(self):
        return self.duration

    def __del__(self):
        print(f"Deleted movie: {self.title}")

m = Movie("Movie Name", "Film Director",120)
print(type(m))  # <class '__main__.Movie'>
print(str(m))   # Movie Name - Directed by Film Director, Film Duration minutes long.
print(len(m))   # 120

del m
print(m)    # Deleted movie: Movie Name
