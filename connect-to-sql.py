from pymysql import connect
import os


"""connect stuff"""
connection = connect(
        host = os.getenv("MYSQL_HOST"),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        db = os.getenv("MYSQL_DATABASE"),
        charset = "utf8mb4"
)

"""read and write from sql"""
def write():
    try:
        with connection.cursor() as cursor:
            query = 'insert into banking_customers (firstname,lastname,address,emailaddress,password)values ("bob","bobson","2 b road","bobbobby@bob.com","bobpassword");'
            cursor.execute(query)
        connection.commit()
    finally:
        connection.close() 


def read():
    try:
        with connection.cursor() as cursor:
            query = "Select * from banking_customers"
            cursor.execute(query)
            result = cursor.fetchall()
            print(result)
    finally:
        connection.close()

#write()
read()





    
