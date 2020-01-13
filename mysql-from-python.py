import os
import pymysql

# Get our username from the Gitpod workspace. Username is stores as an eniornment variable
# (Modify this variable if running on another enviornment) I.E your own machine

username = os.getenv('GITPOD_USER')

# Connect to the database (Our connection object)
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor() as cursor:
        sql = "SELECT * FROM Artist;"   
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)           
finally:
    # Close the connection, regardless of whether the above was successful or not
    connection.close()