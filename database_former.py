import mysql.connector


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))


print("\n")
prPurple("Enter the details to form the connection to database\n")

host_add = str(input("Enter HOST address : "))
username = str(input("Enter the user : "))
my_password = str(input("Enter the password : "))
my_database = str(input("Enter the database name : "))

global my_db

# This will connect to your database
try:
    my_db = mysql.connector.connect(host=host_add, user=username, password=my_password, database=my_database)
    print("\n")
    prPurple("Connection formed to database")

except mysql.connector.Error as e:
    print(e)

# prepare a cursor object using cursor() method
my_cursor = my_db.cursor()

# Creating table
my_sql = "CREATE TABLE data ( STUDENT_NAME VARCHAR(20) NOT NULL," \
         "ROLL_NO VARCHAR(10) NOT NULL," \
         "BOOK_NO VARCHAR(10)," \
         "DATE VARCHAR(20))"

try:

    # Execute the SQL command
    my_cursor.execute(my_sql)

    # Commit your changes in the database
    my_db.commit()

    prPurple("Table Formed")

except:

    # Rollback in case there is any error
    my_db.rollback()

# disconnect from the mysql-database server
my_cursor.close()
my_db.close()
