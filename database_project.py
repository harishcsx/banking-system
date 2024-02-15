import mysql.connector as mysql
import datetime
import random


def execute(query):
    mydb = mysql.connect(host = "localhost", passwd = "unknown",
                    database = "bank", user = "root"
    )
    status = "fail to connect"
    if mydb.is_connected:
        cur = mydb.cursor()
        cur.execute(query)
        mydb.commit()
        cur.close()
        status = "sucessfully connected"
        print(query)
    mydb.close()
    return status

# current time and date 
def get_time_date():
    current_date = datetime.date.today()
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    return current_time,current_date

class Account:
    def __init__(self,username,age):
        self.name = username
        self.age = age
    created = False
    def create_account(self):
        if self.age < 18:
            print("not eligible to create an account in bank!!!")
            return None
        # generating a account number 
        account_no = 0
        for i in range(5):
            generate_random_no = random.randint(0,9)
            account_no = (account_no*10)+generate_random_no
        self.account_no = account_no
        print("your account no:",self.account_no, "of len",len(str(self.account_no)))
        self.password = int(input("4 digit password: "))
        self.balance = int(input("enter your balance"))
        self.created = True
        # query = f"insert into history values('{self.name}',{self.account_no}, {self.password},{self.age},{self.display_balance},'account creation','{get_time_date()[1]}','{get_time_date()[0]}');"
        query = f"INSERT INTO history (user, accno, pass, age, balance, action, date, time) VALUES ('{self.name}', {2342}, {self.password}, {self.age}, {self.balance}, 'account creation', '{get_time_date()[1]}', '{get_time_date()[0]}');"
        status = execute(query)
        print(f"status(database): {status}")
        print("account created sucessfully!!!!")

    def debit(self,amount):
        if not self.created:
            print("create account first!!")
            return None
        self.amount = amount
        if self.amount <= 0:
            print("no money found to debit!!")
        self.balance -= self.amount
        query = f"insert into history values('{self.name}',{self.account_no}, {self.password},{self.age},{self.display_balance()},'amount debit of{self.amount}','{get_time_date()[1]}','{get_time_date()[0]}');"
        status = execute(query)
        print(f"status(database): {status}")
        print(f"the amount of ${self.amount} debited from your account")
        print(f"total amount: ${self.display_balance()}")
    
    def credit(self,credit_amount):
        if not self.created:
            print("create account first!!")
            return None
        self.credit_amount = credit_amount
        self.balance += self.credit_amount
        query = f"insert into history values('{self.name}',{self.account_no}, {self.password},{self.age},{self.display_balance()},'account credit of {self.credit_amount}','{get_time_date()[1]}','{get_time_date()[0]}');"
        status = execute(query)
        print(f"status(database): {status}")
        print(f"the amount of ${self.credit_amount} credited to your account!")
        print(f"total amount: ${self.display_balance()}")

    def history(self):
        # when accound created and all the credit debit details 
        if not self.created:
            print("create account first!!")
            return None
    
    def display_balance(self):
        if not self.created:
            print("create account first!!")
            return None
        return self.balance

    def exit(self):
        print("thank you")
        exit()




# harish = Account("harish",30)
# harish.create_account()
# harish.debit(50)

print(f"hello world {print("hi")} ")