from db import db

class User:
    def __init__(self, _name, _username, _password, _role):
        self.name = _name
        self.username = _username
        self.password = _password
        self.role = _role

    def getUserData(self):
        print(f"{self.name} / {self.username} / {self.password}")

    def toDictionary(self):
        myDict = dict()
        myDict["name"] = self.name
        myDict["username"] = self.username
        myDict["password"] = self.password
        return myDict




