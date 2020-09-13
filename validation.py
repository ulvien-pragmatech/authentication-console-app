
from register import *
# VALIDATIONLAR
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
alphabets = [
"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]


# NAME VALIDATION
def valName(checkName):
    # ANCAQ HERFLERDEN TESHKIL OLUNUB MU, BOSHLUQ ve HECNE var mi
    while True:
        isAlpha = True
        textual = checkName
        for i in checkName.lower():
            if i not in alphabets:
                isAlpha = False
                break
        if isAlpha == False or isSpacingOrNoType(textual):
            checkName = input("Non-alphabetic type, try again: ")
        elif isAlpha == True:
            break
    return checkName


# ISTIFADECI ADI VALIDATION
def valUsername(checkUsername):
    # BOSHLUQ VAR MI
    while True:
        textual = checkUsername
        if isSpacingOrNoType(textual):
            checkUsername = input("Your username consist of spacing or nothing is typed, try again: ")
        elif dataBaseUsernameCheck(checkUsername):
            checkUsername = input("This username is in use, try again: ")
        else:
            break
    return checkUsername

# PASSWORD VALIDATION
def valPassword(checkPassword, confirmPassword):
    # EN AZ BIR BOYUK, BIR KICIK HERFDEN TESHKIL OLUNUB MU + MIN BIR DENE YA SIMVOL YA REQEM ELAVE OLUNUB MU
    while True:
         textual = checkPassword
         kicik = boyuk = specChar = False
         for i in checkPassword:
             if kicik == False and i == i.lower() and i in alphabets:
                 kicik = True
             elif boyuk == False and i == i.upper() and i.lower() in alphabets:
                 boyuk = True
             elif specChar == False and i in nums or i not in nums and i.lower() not in alphabets:
                 specChar = True
         if kicik and boyuk and specChar and len(checkPassword)>=8 and isSpacingOrNoType(textual)==False and confirmPassword==checkPassword:
             break
         else:
             checkPassword = input("Try again, Password must contain at least one lower and upper letter, one symbol or numeric (min 8chars & no spaces): ")
             confirmPassword = input("Repeat Password, please: ")
    return checkPassword

# VALIDATION FOR ROLE
def valRole(checkRole):
    userroles = ["Admin", "SuperAdmin", "Editor"]
    while True:
        for x in userroles:
            if x == checkRole:
                return checkRole
        checkRole = input("This type of Admin doesn't exists: ")

# GONDERILEN ARGUMENTDE BOSLUGU YOXLAYIR
def isSpacingOrNoType(textual):
    for i in textual:
        if i == " ":
            return True
    if len(textual) == 0:
        return True
    return False


# Database check
def dataBaseUsernameCheck(checkUsername):
    for user in db:
        if user["username"] == checkUsername:
            return True
    return False
