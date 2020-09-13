from db import db
from lib import User
import json
from validation import *

# YENI ISTIFADECI YARATMAQ
def createUser():
    newName = valName(input("Name: "))
    newUsername = valUsername(input("Username: "))
    newPassword = valPassword(input("Password: "),input("Repeat Password: "))
    accRole = valRole(input("Account Type(Admin, SuperAdmin or Editor): "))
    db.append(User(newName, newUsername, newPassword, accRole).toDictionary())
    with open("newDB.json", 'w') as json_file:
        json.dump(db, json_file)

# BUTUN ISTIFADECILERI GOSTERMEK
def showAllUsers():
    for i in db:
        print(i)

# Password ve confirmation eyni while'da









