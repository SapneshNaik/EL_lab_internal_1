import mysql.connector
import sys 
import getopt
import datetime
global conn,cursor;

conn = mysql.connector.connect(host="localhost", user="root",password="root")


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def connection():
    
    if conn.is_connected():
        return True
    else:
        return False



def insertvalue(usrname,passwd):
    query = "INSERT INTO logindetails(user, password) VALUES(%s,%s)"
    args = (usrname,passwd);
    cursor = conn.cursor(); 
    cursor.execute(query,args);
    conn.commit();


def retreiveall():
    query = "SELECT * FROM logindetails";
    cursor =  conn.cursor();
    cursor.execute(query)
    rows = cursor.fetchall();
    print("No of Record: ", cursor.rowcount)
    print(rows)
    for row in rows:
        print(row);


def retreiveone():
    query = "SELECT * FROM logindetails";
    cursor =  conn.cursor();
    cursor.execute(query)
    row = cursor.fetchone()
    print("No of Record: ", cursor.rowcount)
    while row is not None:
        row = cursor.fetchone()
        print(row)


def create_database():
    if connection():
        mycursor = conn.cursor()
        try:
            mycursor.execute("CREATE DATABASE db_181041004")
            print(bcolors.OKGREEN + "\n Success: Database 'db_181041004' created \n" + bcolors.ENDC)
        except:
            print(bcolors.WARNING + "\n Warning: Database 'db_181041004' already exists \n" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "\n Error: Could not connect to mysql server \n" + bcolors.ENDC)


def create_table():
    conn_db = mysql.connector.connect(host="localhost", db="db_181041004", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()
        try:
            mycursor.execute("CREATE TABLE reg_no(id INT(10) PRIMARY KEY, fname VARCHAR(255), lname VARCHAR(255), dob DATE)")
            print(bcolors.OKGREEN + "\n Success: Table 'reg_no' created\n" + bcolors.ENDC)
        except:
            print(bcolors.WARNING + "\n Warning: Table 'reg_no' already exists \n" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "\n Error: Could not connect to mysql server \n" + bcolors.ENDC)



def insert_values():
    conn_db = mysql.connector.connect(host="localhost", db="db_181041004", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        sql = "INSERT INTO reg_no (id, fname, lname, dob) VALUES (%s, %s, %s, %s)"

        id = input("\nEnter id\n")
        fname = input("\nEnter fname\n")
        lname = input("\nEnter lname\n")
        dob = input("\nEnter dob ( yyyy-mm-dd )\n")

        if not valid_date(dob):
            print(bcolors.FAIL + "\n Error: Incorrect 'dob' format, should be YYYY-MM-DD \n" + bcolors.ENDC)
            sys.exit()


        val = (id, fname, lname, dob)
        try:
            mycursor.execute(sql, val)
            conn_db.commit()
            print(bcolors.OKGREEN + "\n Success: Insertion Successful \n" + bcolors.ENDC)

        except:
            print(bcolors.FAIL + "\n Error: Could not insert the values \n" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "\n Error: Could not connect to mysql server \n" + bcolors.ENDC)



def alter_table():
    conn_db = mysql.connector.connect(host="localhost", db="db_181041004", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        col = input("\nEnter column name\n")
        sql = "ALTER TABLE reg_no add %s VARCHAR(255)" % (col)

        try:
            mycursor.execute(sql)
            conn_db.commit()
            print(bcolors.OKGREEN + "\n Success: column added to table Successful \n" + bcolors.ENDC)

        except:
            print(bcolors.FAIL + "\n WARNING: column already exists in table \n" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "\n Error: Could not connect to mysql server \n" + bcolors.ENDC)


def truncate_table():
    conn_db = mysql.connector.connect(host="localhost", db="db_181041004", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        sql = "DROP TABLE reg_no"
        try:
            mycursor.execute(sql)
            conn_db.commit()
            print(bcolors.OKGREEN + "\n Success: table dropeed Successfully \n" + bcolors.ENDC)

        except:
            print(bcolors.FAIL + "\n WARNING: could not drop table \n" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "\n Error: Could not connect to mysql server \n" + bcolors.ENDC)


def display_values():
    conn_db = mysql.connector.connect(host="localhost", db="db_181041004", user="root",password="root")
    if conn_db.is_connected():
        mycursor = conn_db.cursor()

        try:
            mycursor.execute("SELECT * FROM customers")
            myresult = mycursor.fetchall()
            for x in myresult:
              print(x)

        except:
            print(bcolors.FAIL + "\n WARNING: could not print table \n" + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "\n Error: Could not connect to mysql server \n" + bcolors.ENDC)

def valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True;
    except ValueError:
        return False

def main():
    while True:
        print("\nEnter your choice::\n")
        print(bcolors.OKBLUE + "Create database - 1:" + bcolors.ENDC)
        print(bcolors.OKBLUE + "Create table (reg_no) - 2:" + bcolors.ENDC)
        print(bcolors.OKBLUE + "Insert values (reg_no) - 3:" + bcolors.ENDC)
        print(bcolors.OKBLUE + "Display table values (reg_no) - 4:" + bcolors.ENDC)
        print(bcolors.OKBLUE + "Alter table (add column) - 5:" + bcolors.ENDC)
        print(bcolors.OKBLUE + "Trucate table (reg_no) - 6:" + bcolors.ENDC)
        print(bcolors.OKBLUE + "Quit- q:\n" + bcolors.ENDC)
        choice = input("Enter the option:\t")
        if choice == '1':
            create_database()
        if choice == '2':
            create_table()
        if choice == '3':
            insert_values()
        if choice == '4':
            display_values()    
        if choice == '5':
            alter_table()
        if choice == '6':
            truncate_table()
        if choice == 'q':
            sys.exit()
        



if __name__ == "__main__":
    main();
    


