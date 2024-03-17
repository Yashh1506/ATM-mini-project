import pymysql as mq
import random as rd
conn=mq.connect(host='localhost',user='',password='',database='ATM')
mycursor=conn.cursor()
print("Connection is done")
mycursor.execute("CREATE DATABASE ATM")
print("ATM database created")
mycursor.execute("CREATE TABLE customer_data(acc_n bigint PRIMARY KEY not null,name varchar(20),balance int, branch varchar(20),pin int)")
print("Table created sucessfully")

def get():
    print("Enter account details")
    #acc_n = input("Enter your account number : ")
    acc_n=rd.randint(1000000000,9999999999)
    name = input("Enter your name : ")
    branch = input("Enter branch name : ")
    balance = input("Amount you want to deposit : ")
    insert_query = """INSERT INTO customer_data(acc_n, name, branch, balance) VALUES(%s,%s,%s,%s)"""
    record=(acc_n,name,branch,balance)
    mycursor.execute(insert_query,record)
    conn.commit()
    print("Set pin to your account!!")
    while True:
        pin = int(input("Enter your pin : "))
        c_pin = int(input("Re-enter pin : "))
        if(c_pin==pin):
            pin_query="""UPDATE customer_data SET pin=(%s) WHERE acc_n=(%s)"""
            record=(pin,acc_n)
            mycursor.execute(pin_query,record)
            conn.commit()
            print("Pin Set!!")
            print("--------------------------------------------------------------------------------------------")
            print("Account Created!!!!")
            print("Account Number : ",acc_n)
            print("--------------------------------------------------------------------------------------------")
            break
        else:
            print("Pin doesnot match!!!")
    print("Record entered sucessfully")

def show(acc_n):
    pin=int(input("Enter pin : "))
    print("-----------------------------------------------------------------------------------------------")
    fetch="""SELECT pin from customer_data WHERE acc_n=(%s)"""
    mycursor.execute(fetch,acc_n)
    fetch_pin=mycursor.fetchone()
    if(pin==fetch_pin[0]):
        show_details="""SELECT * FROM customer_data WHERE acc_n=(%s)"""
        mycursor.execute(show_details,acc_n)
        details=mycursor.fetchall()
        for x in details:
            print("Account number : ",x[0])
            print("Name : ",x[1])
            print("Balance : ",x[2])
            print("Branch : ",x[3])
            print("Pin : ",x[4])
            print("-----------------------------------------------------------------------")
    else:
        print("Incorrect Pin!!")

def withdraw(amount,acc_n):
    print("Account Number :",acc_n)
    print("Amount Entered : ",amount)
    pin=int(input("Enter pin : "))
    fetch="""SELECT pin from customer_data WHERE acc_n=(%s)"""
    mycursor.execute(fetch,acc_n)
    fetch_pin=mycursor.fetchone()
    if(pin==fetch_pin[0]):
        fetch_balance="""SELECT balance from customer_data WHERE acc_n=(%s)"""
        mycursor.execute(fetch_balance,acc_n)
        balance = mycursor.fetchone()
        c_balance = balance[0] - amount
        update_balance = """UPDATE customer_data SET balance=(%s) WHERE acc_n=(%s)"""
        record=(c_balance,acc_n)
        mycursor.execute(update_balance,record)
        conn.commit()
        print("Current Balance :",c_balance)
        print("Balance Updated!")
        print("---------------------------------------------------------------------------------")
    else:
        print("Incorrect Pin!!")
        print("----------------------------------------------------------------------------------")

def deposit(amount,acc_n):
    print("Account Number :",acc_n)
    print("Amount Entered : ",amount)
    pin=int(input("Enter pin : "))
    fetch="""SELECT pin from customer_data WHERE acc_n=(%s)"""
    mycursor.execute(fetch,acc_n)
    fetch_pin=mycursor.fetchone()
    if(pin==fetch_pin[0]):
        fetch_balance="""SELECT balance from customer_data WHERE acc_n=(%s)"""
        mycursor.execute(fetch_balance,acc_n)
        balance = mycursor.fetchone()
        c_balance = balance[0] + amount
        update_balance = """UPDATE customer_data SET balance=(%s) WHERE acc_n=(%s)"""
        record=(c_balance,acc_n)
        mycursor.execute(update_balance,record)
        conn.commit()
        print("Current Balance :",c_balance)
        print("Balance Updated!")
        print("---------------------------------------------------------------------------------")
    else:
        print("Incorrect Pin!!")
        print("---------------------------------------------------------------------------------")

def change_pin(acc_n):
    print("Account number : ",acc_n)
    pin=int(input("Enter pin : "))
    fetch="""SELECT pin FROM customer_data WHERE acc_n=(%s)"""
    mycursor.execute(fetch,acc_n)
    fetch_pin=mycursor.fetchone()
    if(pin==fetch_pin[0]):
        while True:
            n_pin=int(input("Enter new pin : "))
            r_pin=int(input("Re-enter new pin : "))
            if(n_pin==r_pin):
                update_pin="""UPDATE customer_data SET pin=(%s) WHERE acc_n=(%s)"""
                record=(n_pin,acc_n)
                mycursor.execute(update_pin,record)
                conn.commit()
                print("New pin updated!!")
                break
            else:
                print("Does'nt match!")
    else:
        print("Incorrect Pin!!")

def delete_acc():
    acc_n=input("Enter your account number : ")
    fetch="""DELETE FROM customer_data WHERE acc_n=(%s)"""
    mycursor.execute(fetch,acc_n)
    conn.commit()
    print("Account deleted sucessfully!!")

def menu():
    print("-----------------------WELCOME TO LAXMI CHEAT FUND-----------------------")
    print("1)Create Account")
    print("2)Get account details")
    print("3)Withdraw")
    print("4)Deposit")
    print("5)Change pin")
    print("6)Delete account")
    print("7)Exit")

def main():
    while True:
        menu()
        choice=int(input("Enter your choice : "))
        if(choice==1):
            get()
        elif(choice==2):
            acc_n=input("Enter your account number : ")
            show(acc_n)
        elif(choice==3):
            acc_n=input("Enter account number : ")
            amount=int(input("Enter amount : "))
            withdraw(amount,acc_n)
        elif(choice==4):
            acc_n=input("Enter account number : ")
            amount=int(input("Enter amount : "))
            deposit(amount,acc_n)
        elif(choice==5):
            acc_n=input("Enter account number : ")
            change_pin(acc_n)
        elif(choice==6):
            delete_acc()
        elif(choice==7):
            exit=input("Do you want to exit? (y/n) : ")
            exit.lower()
            if(exit=="y"):
                break
            else:
                pass
main()    