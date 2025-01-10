import json
import os


class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}
        # load users from .json file
        self.loadUsers()

    def loadUsers(self):
        if os.path.exists('users.json'):
            with open('users.json', 'r') as file:
                users = json.load(file)
                for user in users:
                    user = json.loads(user)
                    newUser = User(username = user['username'], password = user['password'], email= user['email'])
                    self.users.append(newUser)
            print(self.users)

    def register(self, user: User):
        self.users.append(user)
        self.saveToFile()
        print('Registration Successful.')

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user
                print('Login Successful.')
                break

    def logout(self):
        self.isLoggedIn = False
        self.currentUser = {}
        print('Logout Successful.')

    def identity(self):
        if self.isLoggedIn:
            print(f'Logged in as {self.currentUser.username}')
        else:
            print('Not logged in.')

    def saveToFile(self):
        list = []

        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open('users.json', 'w') as file:
            json.dump(list, file)


repository = UserRepository()

while True:
    print('Menü'.center(50,'_'))
    selection = input('1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nYour Selection: ')
    if selection == '5':
        break
    else:
        if selection == '1':
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")
            user = User(username = username, password=password, email=email)
            repository.register(user)
            #print(repository.users)

        elif selection == '2':
            username = input("username: ")
            password = input("password: ")

            repository.login(username, password)

        elif selection == '3':
            repository.logout()

        elif selection == '4':
            repository.identity()

        else:
            print('Invalid selection. Please try again.')