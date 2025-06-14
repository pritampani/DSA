# Module Imports
# import mariadb
# import sys

# # Connect to MariaDB Platform
# try:
#     conn = mariadb.connect(
#         user="root",
#         password="db_user_passwd",
#         host="192.0.2.1",
#         port=3306,
#         database="employees"

#     )
# except mariadb.Error as e:
#     print(f"Error connecting to MariaDB Platform: {e}")
#     sys.exit(1)

# # Get Cursor
# cur = conn.cursor()


# n1=int(input("ENTER A NUMBER"))
# n2=int(input("enter 2nd nnumber"))
# n3=int(input("enter 3rd numbers"))
# maximum=0
# minimum=0
# if(n1>n2 and n1>n3):
#     maximum=n1
    
# elif(n2>n3):
#     maximum=n2
    
# else:
#     maximum=n3
# print(maximum)
# if(n1<n2 and n1<n3):
#     minimum=n1
    
# elif(n2<n3):
#     minimum=n2
    
# else:
#     minimum=n3
# print(minimum)


# fname = input("Enter the first name:")
# lname = input("Enter the last name:")
# fname_NO = int(input("Enter how many times you want to print the first name:"))
# lname_NO = int(input("Enter how many times you want to print the last name:"))
# a = 3
# i=1

# while i<=a :
#     print(fname*fname_NO,lname*lname_NO )
#     i+=1




# fname = input("Enter the first name:")
# lname = input("Enter the last name")
# a = 3
# i=1
# while i<=a :
#     while i<=a:
#         print(fname + lname*3 )
#         i+=1
#         break

# num = int(input("Enter the number:"))
# sum = 0

# while num > 0:
#     if num<0:
#         print("Enter a positive number")
#     else:
#         sum += num
    
#         num -= 1
# print("The sum is", sum)

# a = []
# for i in range(1000):
#     a.append('SORRY')

# print(a)


# a=int(input("enter a number:"))
# b=int(input("enter a number:"))
# c=int(input("enter a number:"))
# d=int(input("enter a number:"))
# print(a,b,c,d)

# a = 'chiku\pani'
# print(a)



Name = input("Enter the your name:")
N =int(input("Enter the number you want to print"))
while N>0:
    print(Name)
    N-=1