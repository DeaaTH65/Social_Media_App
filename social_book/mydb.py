import mysql.connector

dataBase = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    passwd = 'Deaath@65',
)


# prepare a cursor object
cursorObject = dataBase.cursor()



# create a database
cursorObject.execute("CREATE DATABASE social_book")

# to confirm database creation
print("social_book database created")
