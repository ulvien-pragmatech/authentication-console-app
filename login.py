from register import *

def login():
    while True:
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        flag = False
        for i in db:
            if username == i["username"] and password == i["password"]:
                flag = True
                break

        if flag == True:
            print(f"Welcome, {username}")
        else:
            print(f"Wrong username or password. Enter '0' to go Main Page or any key to try again")

        exitORtry = int(input())
        if exitORtry == 0:
            break



