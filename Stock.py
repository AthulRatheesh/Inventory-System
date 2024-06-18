def display():
    try:
        mycursor.execute("select * from stock")
        data=mycursor.fetchall()
        print("++++++++++++++++++++++++++++++++++++")
        print("\t\t       STOCK")
        print()
        for i,j,k,l,m in data:
            print(i,'\t',j,'\t',k,'\t',l,'\t',m)
            print()
        print("++++++++++++++++++++++++++++++++++++")
        print()
    except mys.Error as error:
        print("Error:",error)
        mydb.rollback()


print("//////////////////////////////////////////////////////WELCOME TO STOCK/////////////////////////////////////////////////////////////")
import mysql.connector as mys
mydb=mys.connect(host="localhost",user="root",passwd="kl7be256",charset='utf8',database="sales")
mycursor=mydb.cursor()
try:
    query="create table if not exists stock(Product_code int(4) not null primary key,Product_Name varchar(20),Stock int(5),Cost int(8),Total_Cost int(10))"
    mycursor.execute(query)
    mydb.commit()
except mys.Error as error:
    print(error)
    mydb.rollback()


i=True
while i:
    print()
    print("1.Add Stock")
    print()
    print("2.Remove Stock")
    print()
    print("3.Update Stock")
    print()
    print("4.Display Stock")
    print()
    print("5.Exit Stock")
    print()
    ans=int(input("Enter choice:"))
    print()
    if ans==1:
        while 1==1:
            ch=int(input("Enter -1 to stop and any other no. to continue:"))
            if ch==-1:
                break
            code=int(input("EnterProduct Code:"))
            name=input("Enter product name:")
            stock=int(input("Enter stock:"))
            cost=int(input("enter cost:"))
            total=cost*stock
            mycursor.execute('insert into stock values('+str(code)+'," '+name+' " ,'+str(stock)+' , '+str(cost)+' , '+str(total)+')')
            mydb.commit()
            print(mycursor.rowcount,"Record Inserted")
    elif ans==2:
        code=int(input("Enter Code:"))
        try:
            mycursor.execute('delete from stock where Product_Code='+str(code))
            mydb.commit()
            print("Removed Successfully")
        except mys.Error as error:
            print("Failed to remove due to error:",error)
            mydb.rollback()
    elif ans==3:
        code=int(input("Enter Product code:"))
        stock=int(input("Enter new stock:"))
        try:
            mycursor.execute('update stock set stock='+str(stock)+' where Product_Code='+str(code))
            mydb.commit()
            print("Successfully Updated")
        except mys.Error as error:
             print("Failed to update due to error:",error)
             mydb.rollback()
    elif ans==4:
        try:
            display()
        except mys.Error as error:
            print("Failed to display due to error:",error)
            mydb.rollback()        
    elif ans==5:
        i=False
        import Main
    else:
        print("Wrong Option.\n\nTry Again")
        print("=================================")
    
        

    
