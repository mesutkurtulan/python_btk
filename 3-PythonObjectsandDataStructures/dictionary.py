# key - value
cities = ["Kocaeli", "Istanbul", "Bursa", "İzmir"]
plates = [41, 34, 16, 35]

print(plates[cities.index('Istanbul')]) # 34

platesDictionary = { "Kocaeli": 41, "Istanbul": 34, "Bursa": 16, "Izmir": 35 }
print(platesDictionary["Kocaeli"])  # 41

platesDictionary["Denizli"] = 20
print(platesDictionary)  # {'Kocaeli': 41, 'Istanbul': 34, 'Bursa': 16, 'Izmir': 35, 'Denizli': 20}

users = {
    "John":
        {
            "age": 30,
            "roles": ["admin", "user"],
            "email": "john@mail.com",
            "address": "Newyork",
            "phone": "1234567890"
        },
    "Jane":
        {
            "age": 28,
            "roles": ["user"],
            "email": "jane@mail.com",
            "address": "Newyork",
            "phone": "9876543210"
        }
}
print(users)            # {'John': {'age': 30, 'email': 'john@mail.com', 'address': 'Newyork', 'phone': '1234567890'}, 'Jane': {'age': 28, 'email': 'jane@mail.com', 'address': 'Newyork', 'phone': '9876543210'}}
print(users["John"])    # {'age': 30, 'email': 'john@mail.com', 'address': 'Newyork', 'phone': '1234567890'}
print(users["Jane"]["email"]) # jane@mail.com
print(users["Jane"]["roles"][0]) # user
