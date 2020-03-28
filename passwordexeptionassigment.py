class TooShort(Exception):
    def __init__(self,msg):
        self.msg=msg

def password(lengtt):
    if lengtt<8:
        raise TooShort("Password is too short!")

lst=input("introduce the password, min 8 charakters:\n")

try:
    password(len(lst))
except TooShort:
    print("password too short!")

