import mysql.connector as mys
mydb=mys.connect(host="localhost",user="root",passwd="kl7be256",charset='utf8',database="sales")
mycursor=mydb.cursor()
i=True
mycursor.execute("select distinct(Cust_ID),Customer_Name from Customer")
data= m=mycursor.fetchall()
    
while i:
    print()
    print("++++++++++++++++++++++++++++++++++")
    print()
    print("1.CUSTOMER DETAILS")
    print()
    print("2.HISTORY")
    print()
    print("3.EXIT")
    print()
    ans=int(input("Enter option:"))
    print()

    if ans==1:
        print()
        print("CustCode\t\tCustName")
        print()
        
        for i,j in m:
            print(i,"\t\t",j,"\t")
        print()    
    elif ans==2:
        try:
            query="select * from Customer order by Date_Of_Purchase desc"
            mycursor.execute(query)
            data=mycursor.fetchall()
            print("CustCode\t\tCustName,\tDate_Of_Purchase")
            print()
            for i,j,k in data:
                print(i,"\t\t",j,"\t\t",str(k))
            print()    
        except mys.Error as error:
            print(error)
            mydb.rollback()
    elif ans==3:
        print()
        print("THANK YOU")
        i=False
        print()
        import Main
    else:
        print()
        print("Wrong Option...Please Try Again")
        print()

