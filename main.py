import json
from register import *
from login import login

print("""
=======================================================================================
0. Exit
1. REGISTER
2. LOGIN
3. SHOW ALL USERS
========================================================================================
""")


while True:
    nav = int(input("Choose operation: "))
    if nav == 0:
        print("Thank you for using our system!")
        break
    elif nav == 1:
        createUser()
        print("New User successfully added!")
    elif nav == 2:
        login()
        print("You have been Loggen in!")
    elif nav == 3:
        showAllUsers()
        print("List of All users above!")


with open("newDB.json", 'w') as json_file:
    json.dump(db, json_file)

# dump => 1ci argument (db) faylin icine ne yazacagimizdir, json_file hansi fayla yazacagimizdir
