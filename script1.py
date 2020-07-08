import mysql.connector

# create a database 

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        username="root",
        password=""
    )   

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE mydb")
    print("Database is created successfully..")


    # mycursor.execute("SHOW DATABASES")

    # for d in mycursor:
    #     print(d)

except EOFError as err :
    print(err)