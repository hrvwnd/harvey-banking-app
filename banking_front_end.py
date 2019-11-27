def frontend():
    print ("Hello and welcome to the banking app company")
    print ("You have the following options")
    print ("1. Create Account")
    print ("2. Deposit")
    print ("3. Withdraw")
    print ("4. Show Account Details")
    print ("5. Exit")
    user_input = input("Please enter your choice: ")
    user_choice(user_input)


def user_choice(choice):
    while True:
        if choice in ["1","Create Account","create account"]:
            create_account()
        elif choice in ["2", "Deposit", "deposit"]:
            deposit()
        elif choice in ["3","Withdraw","withdraw"]:
            withdraw()
        elif choice in ["4","Show Account Details","show account details",
                        "Account Details","account details"]:
            account_details()
        elif choice in ["5","Exit","exit"]:
            user_exit()
        else:
            import time
            print ("Wrong input, please try again")
            time.sleep(1)
            frontend()



"""
#Testing purposes 
first_name = "blah"
surname = "blahson"
address = "blahburry way"
email_address = "blahblahson@email.com"
password = "password"
sql_string = '("'+first_name+ '","' + surname + '","' + address + '","' +email_address + '","' + password + '")'
print (sql_string)
from connect_to_sql import write 
write(sql_string)
"""


def create_account():
    # takes user inputs and formats them in sql syntax
    email_address = input("Please enter your email address: ")
    #change this - check database for email
    first_name = input("Please enter your first name: ")
    surname = input("Please enter your suranme: ")
    date_of_birth = input ("Please enter your date of birth in dd/mm/yy: ")
    address = input("Please enter your adddress: ")
    #postcode = input("Please enter your postcode: ")
    password = create_password()
    sql_string = '("'+first_name+ '","' + surname + '","' + address + '","' +email_address + '","' + password + '")"'
    print (sql_string)
    from connect_to_sql import write
    write(sql_string)
    user_information = [first_name,surname,address,email_address,password]
    return user_information


def deposit():
    pass
def withdraw():
    pass
def account_details():
    pass
def user_exit():
    pass

def create_password():
    import getpass
    try:
        password = getpass.getpass("Password: ")
    except Exception as error:
        print("ERROR",error)
    return password

class BankAccount():
    _money = 0

    def deposit(self, money, password):
        if password_authenticate(password):
            self.money += money

    def withdraw(self,money,password):
        if password_authenticate(password):
            self.money -= money 

def password_authenticate():
    import getpass
    try:
        password = getpass.getpass("Password: ")
    except Exception as error:
        print("ERROR",error)
    else:
        print("Password entered: ", password)
    if password == "password":
        print ("Correct Password")
    else:
        print ("Incorrect Password")
    

"""
if __name__ == "__main__":
    frontend()
"""
