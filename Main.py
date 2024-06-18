#Connection
import mysql.connector as mys
mydb=mys.connect(host="localhost",user="root",passwd="kl7be256",charset='utf8')
mycursor=mydb.cursor()
mycursor.execute("create database if not exists sales")
mydb=mys.connect(host="localhost",user="root",passwd="kl7be256",charset='utf8',database="sales")
mycursor=mydb.cursor()
try:
    query='create table if not exists login(password int(4) not null primary key,username varchar(30))'
    mycursor.execute(query)
    mydb.commit()
except mys.Error as error:
    print("Error:",error)
    mydb.rollback()
try:
    query='create table if not exists Customer(Cust_ID int(5),Customer_Name varchar(30),Date_Of_Purchase date)'
    mycursor.execute(query)
    mydb.commit()
except mys.Error as error:
    print(error)
    mydb.rollback()

import login_main    
#Processes
i=True
while i==True:
    print('''1. Enter Stock
            \n2.Display Customer Details
            \n3.New Sales Billing
            \n4.Log Out''')
    choice=int(input("\nEnter choice(1,2,3,4):"))
    if choice==1:
        import Stock        
    elif choice==2:

        import Customer
    elif choice==3:    
        import Billing
    elif choice==4:
        i=False
        exit()
    else:
        print("Wrong Option.\nTry Again")
    
