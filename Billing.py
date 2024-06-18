def query(code,no):
    try:
        a="select Product_Code,Product_Name,Cost from stock where Product_Code="+str(code)
        b="update stock set Stock=Stock-"+str(no)+" where Product_Code="+str(code) 
        mycursor.execute(a)
        data=mycursor.fetchall()
        mycursor.execute(b)
        mydb.commit()
        for j,k,l in data:
            return j,k,l
    except mys.Error as error:
        print(error)
        mydb.rollback()
import mysql.connector as mys
mydb=mys.connect(host="localhost",user="root",passwd="kl7be256",charset='utf8',database="sales")
mycursor=mydb.cursor()
print("BILLING")
custcode=int(input("Enter Customer code:"))
name=input("Enter Customer Name:")
date=input("Enter date(yyyy-mm-dd):")
try:
    z="insert into Customer values("+str(custcode)+" ,'"+name+"' , ' "+date+"')"
    mycursor.execute(z)
    mydb.commit()
except mys.Error as error:
    print(error)
    mydb.rollback
total=0

print("==============BILL===========")
ans=int(input("Enter no of items:"))
for i in range(ans):
    print()
    code=int(input("Enter product code:"))
    no=int(input("Enter no.of items"))
    print()
    print("===========BILL==============")
    print('Code\tName\tCost\tTotal Cost')
    print("============================")
    j,k,l=query(code,no)
    print()
    summ=int(l)*no
    print(j,'\t',k,'\t',l,'\t',summ)
    total=total+summ
    print("============================")
    print()
    
print("Total Amt to pay is:",total)    


    
        
