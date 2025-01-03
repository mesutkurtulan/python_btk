name = "Jane"
password = "Qwerty123"

if name.lower().strip() == "jane" and password == "Qwerty123":
    print("Welcome, Jane!")
elif name.lower().strip() == "jane":
    print("Wrong User name!")
elif password != "Qwerty123":
    print("Wrong Password!")
else:
    print("Wrong User name and Password!")
