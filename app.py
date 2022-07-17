import sys
from dbhelper import DBhelper

class flipkart:

    def __init__(self):
        # we shoud connect the object with the our database.
        self.db = DBhelper()
        self.menu()

    def menu(self):
        user_input = input(""" 
        1. Enter 1 to register
        2. Enter 2 to Login
        3. Anything else to leave 
        """)

        if user_input == "1":
            self.register()
        if user_input == "2":
            self.login()

        else:
            sys.exit(1000)
            # for getting this sys code we have to import the sys code.

    def login_menu(self):
        input("""
        1. Enter 1 to see the profile
        2. Enter 2 to edit profile
        3. Enter 3 to delete profile
        4. Enter 4 to logout
        """)

    def register(self):
        name = input("Enter Your Name")
        email = input("Enter the Email")
        password = input("Enter the Password")

        responce = self.db.register(name,email,password)

        if responce:
            print("Registration successfully")
        else:
            print("Registration failed")

        self.menu()

    # creating for the login function.
    def login(self):
        email = input("enter email")
        password = input("enter password")

        data = self.db.search(email,password)

        if len(data) == 0:
            print("Incorrect email/password")
            self.login()
        else:
            print("Hello",data[0][1])
            self.login_menu()



obj = flipkart()