import mysql.connector
import sys
from datetime import datetime


def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))


print("\n")
prPurple("Hey! I am your Library Assistant")
prPurple("Please enter the necessary details to login to database")
print("\n")

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

while True:

    print("\n")
    prPurple("What you wanna do "
             " You wanna Make a new entry or Update the old entries\n"
             "\n"
             " Press 1 for add new entry\n"
             " Press 2 for update old entry\n"
             " Press 3 for delete entry\n"
             " Press 4 to see any student data\n"
             " Press bye/exit to exit Lib DB system")

    print("\n")
    entry = input("Enter your choice : ")
    print("\n")

    now_date = datetime.now()
    formatted_date = now_date.strftime('%Y-%m-%d')

    try:
        if entry == "1":

            student_name_1 = str(input("Enter the student name : "))
            roll_no_1 = str(input("Enter the student roll no : "))

            query_1 = "INSERT INTO data (STUDENT_NAME, ROLL_NO, BOOK_NO, DATE, FINE)" \
                      " VALUES (%s, %s, DEFAULT, DEFAULT)"
            val_1 = (student_name_1, roll_no_1)
            my_cursor.execute(query_1, val_1)

            # Commit your changes in the database
            my_db.commit()

            print(my_cursor.rowcount, "record inserted.")

        elif entry == "2":

            prPurple("What you wanna do Re-issue or Return or Issue\n"
                     " Press 5 for re-issue thee book\n"
                     " Press 6 for return the book\n"
                     " Press 7 for issue the book")

            what = str(input("Enter your choice : "))
            print("\n")

            if what == "5":

                re_book_no_2_1 = str(input("Enter the returned book no : "))
                issue_book_no_2_1 = str(input("Enter the issued book no : "))

                query_2_1 = "UPDATE data SET BOOK_NO = %s, DATE = %s WHERE BOOK_NO = %s"
                val_2_1 = (issue_book_no_2_1, formatted_date, re_book_no_2_1)
                my_cursor.execute(query_2_1, val_2_1)

                # Commit your changes in the database
                my_db.commit()

                print(my_cursor.rowcount, "record inserted.")

            elif what == "6":

                re_book_no_2_2 = str(input("Enter the returned book no : "))

                query_2_2 = "UPDATE data SET BOOK_NO = NULL, DATE = NULL WHERE BOOK_NO = %s"
                val_2_2 = (re_book_no_2_2,)
                my_cursor.execute(query_2_2, val_2_2)

                # Commit your changes in the database
                my_db.commit()

                print(my_cursor.rowcount, "record inserted.")

            elif what == "7":

                student_name_2_3 = str(input("Enter the student name : "))
                roll_no_2_3 = str(input("Enter the student roll no : "))
                book_no_2_3 = str(input("Enter the book no : "))

                query_2_3 = "UPDATE data SET BOOK_NO = %s, DATE = %s WHERE STUDENT_NAME = %s AND ROLL_NO = %s"
                val_2_3 = (book_no_2_3, formatted_date, student_name_2_3, roll_no_2_3)
                my_cursor.execute(query_2_3, val_2_3)

                # Commit your changes in the database
                my_db.commit()

                print(my_cursor.rowcount, "record inserted.")

            elif entry == "bye" or "exit":

                # disconnect from the mysql-database server
                my_cursor.close()
                my_db.close()
                sys.exit()

        elif entry == "3":

            student_name_3 = str(input("Enter the student name : "))
            roll_no_3 = str(input("Enter the student roll no : "))

            query_3 = "DELETE FROM data WHERE STUDENT_NAME = %s AND ROLL_NO = %s"
            val_3 = (student_name_3, roll_no_3)

            my_cursor.execute(query_3, val_3)

            # Commit your changes in the database
            my_db.commit()

            print(my_cursor.rowcount, "record inserted.")

        elif entry == "4":

            student_name_4 = str(input("Enter the student name : "))
            roll_no_4 = str(input("Enter the student roll no : "))

            query_4 = "SELECT * FROM data WHERE STUDENT_NAME = %s AND ROLL_NO = %s"
            val_4 = (student_name_4, roll_no_4)

            my_cursor.execute(query_4, val_4)

            result_4 = my_cursor.fetchall()

            for x in result_4:
                print("\n")
                print(x)

        elif entry == "bye" or "exit":

            # disconnect from the mysql-database server
            my_cursor.close()
            my_db.close()
            sys.exit()

        else:

            print("!!!! Wrong Input")

    except mysql.connector.Error as err:
        print(err)
        print("Error Code:", err.errno)
        print("SQLSTATE", err.sqlstate)
        print("Message", err.msg)
        pass
