import mysql.connector
import sys

class DBhelper:

    def __init__(self):
        # writing the code for connect the database.
        try:
            self.conn = mysql.connector.connect(host = "localhost", user = "root", password = "",database = "hit-db-demo")

            # Now we make the cursor object to comunicate with the database. because cursor object has a cability to talk with the database
            self.mycursor = self.conn.cursor()

        except:
            print("Some error occured . Could not connect to database")
            sys.exit(0)
        else:
            print("connected to database")

    def register(self,name,email,password):
        # for comunicate with the data we call the cursor file again.
        try:
            self.mycursor.execute("""
            INSERT INTO `users` (`Id`, `Name`, `Email`, `Password`) VALUES (NULL, '{}', '{}', '{}');
            """.format(name,email,password))
            self.conn.commit()
        except:
            return -1
        else:
            return 1
    # writing the code for not getting the same email id

    def search(self,email,password):
        self.mycursor.execute("""
        SELECT * FROM users WHERE email LIKE '{}' AND password LIKE '{}'
        """.format(email,password))

    # this above code is the kind of read quries not a write quries. write quries means we can edit,del,remove the data while in read quries only we can fetch the data with the help of mycursor.

        data = self.mycursor.fetchall()
        return data