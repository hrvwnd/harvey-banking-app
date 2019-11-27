from pymysql import connect
import os
import banking_front_end


"""connect stuff"""
connection = connect(
        host = os.getenv("MYSQL_HOST"),
        user = os.getenv("MYSQL_USER"),
        password = os.getenv("MYSQL_PASSWORD"),
        db = os.getenv("MYSQL_DATABASE"),
        charset = "utf8mb4"
)


user_list = banking_front_end.create_account()
print(user_list)

"""read and write from sql"""
#'insert into banking_customers (firstname,lastname,address,emailaddress,password)values ("bob","bobson","2 b road","bobbobby@bob.com","bobpassword");'
def write(sql_string):
    try:
        with connection.cursor() as cursor:
            query = f"insert into banking_customers (firstname,lastname,address,emailaddress,password) values ('{user_list[0]}', '{user_list[1]}', '{user_list[2]}', '{user_list[3]}', '{user_list[4]}');"
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


def insert():
    pass
def alter ():
    user_input = input = ("Please enter your alter command: \n")
    write('alter table banking_customers add age int (3)');
    

#write()
#read()





    
