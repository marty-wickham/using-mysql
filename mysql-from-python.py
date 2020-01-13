import os
import datetime
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
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        list_of_names = ['fred', 'Fred']
        # Prepare a string with the same number of placeholders as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit() # Saves the changes to your table
  
finally:
    # Close the connection, regardless of whether the above was successful or not
    connection.close()