import json
# dataB=[]
# open("newDB.json",'w').write("[]")
with open("newDB.json") as tofig:  # jsondan goturur
    dataB = json.load(tofig)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def turnToDict(self):
        myDict = dict()  # dict yaradiriq
        myDict["username"] = self.username
        myDict["password"] = self.password
        return myDict


user1 = User("Ali", "1234")
user2 = User("Taruerish", "155555")
user3 = User("rubilyo", "AAAA4")

dataB.append(user1.turnToDict())
dataB.append(user2.turnToDict())
dataB.append(user3.turnToDict())


for i,x in dataB.items():


with open("newDB.json", 'w') as tofig:
    json.dump(dataB, tofig)                    # json.dump(a, b) -> json'a faylina yazmaq  a -> pythondaki versiyasi  b -> fayli ifade elediyimiz variable (json versiyasi)


