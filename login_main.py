import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',passwd='kl7be256',charset='utf8',database="sales")
mycursor=mydb.cursor()
print('/////////////////////////////////WELCOME TO INVENTORY SYSTEM//////////////////////////////////////')
print('1.Register:')
print()
print()
print('2. Login:')
print()
print()
print("3.Quit")
print()
n=int(input('Enter your Choice :'))
print()
i=j=True
while i:
    if n==1:
        try:
            name=input('Enter Username:')
            print()
            while j:
                passwd=int(input('Enter your 4-digit Password :'))
                a=str(passwd)
                if len(a)>4 or len(a)<4:
                    print("Password exceeded 4 digits...Try Again")
                elif len(a)==4:
                    print()
                    j=False
                    print()
                    A="INSERT INTO login(password,username) values(" + str(passwd) + ",' "+ name +" ' )"
                    mycursor.execute(A)
                    mydb.commit()
                    print()
                    print ('User created successfully')
                    i=False
                    
            
            
            
        except sql.Error as error:
            print("Error",error)
            conn.rollback()
    elif n==2:
        try:
            name=input('Enter Username:')
            print()
            passwd=int(input('Enter your Password :'))
            print()
            B="SELECT username,password from login where  password= "+str(passwd)+" and username=' "+name+" ' "
            mycursor.execute(B)
            if mycursor.fetchall() is None:
                print()
                print("Invalid Username or Password")
            else:
                print()
                print("ACCESS GRANTED")
                print()
                
                i=False
        except sql.Error as error:
            print("Error",error)
            conn.rollback()
    elif n==3:
        i=False
        print("Thank You!")
        exit()
    else:
        print("Wrong Option...Try Again")
        print()
