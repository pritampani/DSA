# from email import message
# import string
# import pyautogui as gui
# import time
# import random ,string

# number = input("Enter the number:")
# time.sleep(5)
# for i in range(int(number)):
#     stri = string.ascii_lowercase
#     message = " ".join(random.sample(stri,10))
#     gui.typewrite(message)
#     gui.press('enter')

#*********************************************************************************************************************************************************************


#wRITE A PROGRAM TO KNOW THE EMAIL ID IS VALID OR NOT

#email=input("Enter your email for verfication:")
#if ('@' in email and email.endswith("gmail.com")) and (email.islower()==True and (" " not in  email)):
#    print("its a valid email")
#
#else:
#
#    print("it not a valid email")


#*********************************************************************************************************************************************************************

#generating QR code
#import qrcode as qr
#img = qr.make("shipun kenda")
#img.save("sipun chutia.png")

#*********************************************************************************************************************************************************************
# from turtle import title
# from tkinter import *
# import os

# st = Tk()

# st,title("Shutdown app")
# st.geometry("50*50")

# st.mainloop()

    
#*********************************************************************************************************************************************************************


#THIS IS THE STONE PAPER SEZZER GAME FOR KIDS
# from imaplib import Int2AP
# from random import random
# import ramdom 


# a = input("Enter the your choice 1.STONE 2.PAPPER 3.SEZZER")
# if a == 1:
#     random.


#*********************************************************************************************************

#coping data from two file to past in another file

# data = data2 = ""
  
# # Reading data from file1
# with open('/home/dlb/Desktop/file1.txt') as fp:
#     data = fp.read()
  
# # Reading data from file2
# with open('/home/dlb/Desktop/file2.txt') as fp:
#     data2 = fp.read()
  
# # Merging 2 files
# # To add the data of file2
# # from next line
# data += "\n"
# data += data2
  
# with open ('/home/dlb/Desktop/file3.txt', 'w') as fp:
#     fp.write(data)


#*******************************************************************************************************************************************




# f = open("/home/dlb/Desktop/file.txt",'w')

# data =(
#     'chiku\n'
#     'pani\n'
#     'pritam\n'
#     'chintu\n'
#     'chiku\n'
#     'pritam'
# )

# f.write(data)
# f.close()

#**********************************************************************************************************************************************


# f = open("/home/dlb/Desktop/file.txt")
# data = f.readlines()
# print(data)
# #data = ['a','b','b','a','b','c']
# for i in data:
#     if i==i:
#         data.remove(i)

# print(data)

#**********************************************************************************************************************************************

#
#import smtplib, ssl  
#from email.mime.text import MIMEText  
#from email.mime.multipart import MIMEMultipart  
#import sys  
#  
##A class is written that will be used to have all the functions that will be used For getting various details which are required for sending the mail and finally sending the mail  
#class MyMail:  
#
## a constructor is written to initialise all the required class variables and set the value of all these class variables to none  
#    def __init__(self):  
#        self.sender_email = None  
#        self.receiver_email = None  
#        self.sender_password = None  
#        self.email_subject = None  
#        self.email_body = None  
#
## a function is written to get the details of the sender the various details that are captured by this function are the email address of the sender and the corresponding password associated with that entered email  
#    def get_sender_details(self):  
#        print("Enter the email of the sender::")  
#        self.sender_email = input()  
#        print("Enter the Password of the sender::")  
#        self.sender_password = input()  
#
## another function is written that is used to retrieve all the receiver details the various  receiver details that are captured by this functions are the email is of the receiver  
#    def get_reciever_details(self):  
#        print("Enter the email of the receiver::")  
#        self.receiver_email = input()  
#
## another function is written that is particularly capturing the details off the email the various  aspects which are captured by this function are the subject of the sending email and the body of the sending email  
#    def get_email_details(self):  
#        print("Enter the Subject of the sending email::")  
#        self.email_subject = input()  
#        print("Enter the Body of the sending email::")  
#        self.email_body = input()  
#
#
## this function is used to print all the details Android by the user like sender email receiver email email subject email body and  verify those details  
#    def print_details(self):  
#        print("Sender Mail::")  
#        print(self.sender_email)  
#        print("Receiver Mail::")  
#        print(self.receiver_email)  
#        print("Email Subject::")  
#        print(self.email_subject)  
#        print("Email Body::")  
#        print(self.email_body)  
#
#
#
## and finally a function is written that is actually used to send the email to the specified receiver email address by the specified input sender email address along with the corresponding subject of the email body of the email and if there is an attachment that is also sent with the email  
#    def send_email(self):  
#
#        message = MIMEMultipart("alternative")  
#        message["Subject"] = self.email_subject  
#        message["From"] = self.sender_email  
#        message["To"] = self.receiver_email  
#
#        text = """\\{}""".format(self.email_body)  
#        html = """\  
#        <html>  
#        <body>  
#            <p>Hi,<br>  
#            this is a test email by Nirnay!<br> .  
#            </p>  
#        </body>  
#        </html>  
#        """  
#
#        obj1 = MIMEText(text, "plain")  
#        obj2 = MIMEText(html, "html")  
#
#        # Add HTML/plain-text parts to MIMEMultipart message  
#        # The email client will try to render the last part first  
#        message.attach(obj1)  
#        message.attach(obj2)  
#
#        context_obj = ssl.create_default_context()  
#        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context_obj) as server:  
#            server.login(self.sender_email,self.sender_password)  
#            server.sendmail(self.sender_email, self.receiver_email, message.as_string())  
#
#
#        print("Email sent successfully.")  
#
#
##  in the end the main function is written that will be used to call all these functions by creating the object of the above-written class   
#def main():  
#
#    mailer = MyMail()  
#
#    while(True):  
#        print("Please choose one of the below-listed options::")  
#        print("1. To enter the details of the sender. [Sender email and sender Password]")  
#        print("2. To enter the details of the receiver. [Receiver email]")  
#        print("3. To enter the sending email's subject.")  
#        print("4. To enter the body of the sending email.")  
#        print("5. To send the email.")  
#        print("6. To verify all the entered details. [Sender email, Sender Password, Receiver email, Email Subject and Email Body.")  
#        print("7. To exit from the code execution.")  
#        menu_choice = input()  
#        menu_choice = int(menu_choice)  
#
#        if menu_choice == 1:  
#            mailer.get_sender_details()  
#
#        elif menu_choice == 2:  
#            mailer.get_reciever_details()  
#            
#        elif menu_choice == 3:  
#            mailer.get_email_details()  
#
#        elif menu_choice == 4:  
#            mailer.get_email_details()  
#
#        elif menu_choice == 5:  
#            mailer.send_email()  
#
#        elif menu_choice == 6:  
#            mailer.print_details()  
#
#        elif menu_choice == 7:  
#            sys.exit()  
#        
#        print("wanna proceed with the program or want to exit the program [Y/n]")  
#        continue_or_exit = input()  
#
#        if continue_or_exit == 'y' or continue_or_exit == 'Y':  
#            pass  
#        elif continue_or_exit == 'n' or continue_or_exit == 'N':  
#            sys.exit()  
#
#
#if __name__ == '__main__':  
#    main()  
#    
#
#


#*****************************************************************************************************************************************************************************

# n=5
# a=[[0 for _ in range(2*n-1)]for _ in range(2*n-1)]
# for i in range(n,-1,-1):
#     y=n-i
#     for x in range(y,2*n-1-y):
#         a[y][x]=i
#         a[x][y]=i
#     y=2*n-2-y
#     for x in range(n-i,y+1):
#         a[y][x]=i
#         a[x][y]=i
# for i in a:
#     print(''.join(str(j) for j in i))


#***************************************************************************************************************************************************************************
#Bakchodi
# a=1
# b=2
# c = id(a) + id(b)
# print(c)
#*************************************************************************************************************************************************************

#WAP to make any year calander 

# import calendar as cl

# a = cl.TextCalendar()

# year = int(input("Enter the year you want to find calander:"))
# print(a.pryear(year))

#*************************************************************************************************************************************************************

#WAP to convet text to audio.

# from gtts import gTT
# from playsound import playsound

# audio = 'speech.mp3'

# language = 'en'

# sp = sTTs(text = "enter your text which you want to convert into audo file", lang = language,slow = False)

# sp.save(audio)
# playsound(audio)


#*************************************************************************************************************************************************************


#WAP to convet photo to catoon

# import cv2
# import numpy as np

# img = cv2.imread("catimge.png")

# gray = cv2.cvt color(img,cv2.COLOR_BGR2GRAY)
# gray = cv2.medianBlur(gray,5)
# edges = cv2.adaptive Threshold (gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)

# color cv2.bilaternalFilter(img,9,250,250)

# cartoon = cv2.bitwise_and(color,color,mask=edges)

# cv2.imshow("Image",img)
# cv2.imshow("edges",edges)
# cv2.imshow("Cartoon",cartoon)
# cv2.waitkey(0)






# cv2.destoryALLWindows()

########################################################################################################################################################################

# num1 = int(input("Enter First number: "))    # taking input for first number
# num2 = int(input(" Enter Second number: "))    # taking input for second number
# sum = num 1 + num2    # adding num1 and num2 and storing them in sum 
# print(sum)    # print sum to the screen


########################################################################################################################################################################

# ls = []
# for i in range(100):
#     if i%3==0:
#         ls.append(i)
# print(ls)
#################################################################################################################################
# ls = [i for i in range(100) if i%2 and i%3]
# print(ls)

#################################################################################################################################

# dict1 = {i:f"item {i}" for i in range(1, 10001) if i%100==0}
# dict1 = {i:f"Item {i}" for i in range(5)}
#
# dict2 = {value:key for key,value in dict1.items()}
# print(dict1,"\n", dict2)

# dresses = [dress for dress in ["dress1", "dress2","dress1",
#                                "dress2","dress1", "dress2"]]
# print(type(dresses))

# evens = (i for i in range(100) if i%2==0)
# print(evens._next_())

# for item in evens:
#     print(item)


#################################################################################################################################


# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# dob = input("Enter your date of birth:")
# print(name)
# print(age)
# print(dob)


# num1 = int(input("Enter your number:"))
# num2 = int(input("Enter your number:"))

# print(num1 + num2)


'''
write a program to prompt the user for entering the number of hours and rate per hour to compute gross pay
Input and output 
enter hours:
enter rate:
pay:
Formula in hour(hours(rate + 5))

'''


# hours = int(input("Enter the no of hour:"))
# rate = int(input("Enter the rate:"))
# pay = hours*(rate+5)

# print("The gross pay is ",pay)




#################################################################################################################################

# x = lambda a : a + 10
# print(x(5))


# def myfunc(n):
#       return lambda a : a * n

# mydoubler = myfunc(2)
# mytripler = myfunc(3)

# print(mydoubler(11))
# print(mytripler(11))


#################################################################################################################################

#CLASS FUNCTION

# class MyClass:
#       x = 5
#       c = 3

# p1 = MyClass()
# print(p1.x + p1.c)



###########################################################################################################################################################

# class Person:
#       def __init__(self, name, age):
#             self.name = name
#             self.age = age

# p1 = Person("John", 36)

# print(p1.name)
# print(p1.age)


###########################################################################################################################################################

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"{self.name}({self.age})"

# p1 = Person("John", 36)
# print(p1)

###########################################################################################################################################################
# import rocky
# class Person:
#     def __init__(self, name, age,group,address,pin,email_id):
#         self.name = name
#         self.age = age
#         self.group = group
#         self.address = address
#         self.pin = pin
#         self.email_id = email_id


#     def myfunc(self):
#         print("Hello my name is " + self.name)
#         print("MY age is:",self.age)
#         print("MY group:",self.group)
#         print("My address:",self.address)
#         print("My PIN:",self.pin)
#         print("My email",self.email_id)

# no_per = int(input("Enter the number of data of each person you want to enter:"))
# for i in range(no_per):
#     name = input("Enter your name:")
#     age = int(input("Enter your age:"))
#     group = input("Enter your group:")
#     addr = input("Enter the address:")
#     pin = int(input("Enter your pin:"))
#     emailid = input("Enter the email id:")
#     p1 = Person(name,age,group,addr,pin,emailid)
# p1.myfunc()

###########################################################################################################################################################

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# #Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname() 



###########################################################################################################################################################
# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     pass

# x = Student("Mike", "Olsen")
# x.printname()




###########################################################################################################################################################

# class Person:
#     def __init__(self, fname, lname):
#         self.firstname = fname
#         self.lastname = lname

#     def printname(self):
#         print(self.firstname, self.lastname)

# class Student(Person):
#     def __init__(self, fname, lname, year):
#         super().__init__(fname, lname)
#         self.graduationyear = year

#     def welcome(self):
#         print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# x = Student("Mike", "Olsen", 2019)
# x.welcome()


###########################################################################################################################################################
def exec_code():
    loc = '''
    class MyNumbers:
        def __iter__(self):
            self.a = 1
            return self

        def __next__(self):
            x = self.a
            self.a += 1
            return x

    myclass = MyNumbers()
    myiter = iter(myclass)

    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
        
    '''
#     exec(loc)
# exec_code()
###########################################################################################################################################################
#StopIteration

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 60:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)



###########################################################################################################################################################


# a = int(input("Enter the nnumber:"))
# b = int(input("Enter the number:"))
# if a>b:
#     print("a is greater")
# else:
#     print("b is greater")


###########################################################################################################################################################


# a = int(input("Enter the nnumber:"))
# if a%2==0:
#     print("it is even")
# elif a==0:
#     print("you have enter zero!")
# else:
#     print("it si odd")

###########################################################################################################################################################
# a = int(input('Enter first number  : '))

# b = int(input('Enter second number : '))

# c = int(input('Enter third number  : '))


# largest = 0
# smallest =0

# if a > b and a > c:
#     largest = a
# if b > a and b > c:
#     largest = b
# if c > a and c > b:
#     largest = c 

# if a < b and a < c :
#     smallest = a
# elif b < a and b < c :
#     smallest = b
# elif c < a and c < b :
#     smallest = c
# else:
#     print("all the number are equal")

# print("is the largest of three numbers: ",largest)
# print("is the smallest of three numbers: ",smallest)

###########################################################################################################################################################


# a=int(input("enter first no:-"))
# b=int(input("enter second  no:-"))
# c=int(input("enter third no:-"))
# largest=a
# smallest=a
# if a==b==c:
#     print("all are equal")
# else:
#     if b>largest:
#         largest=b
#     if c>largest:
#         largest=c
#     print(largest,"largest")
#     if b<smallest:
#         smallest=b
#     if c<smallest:
#         smallest=c
#     print(smallest,"smallest")

###########################################################################################################################################################



# a = int(input("Enter your Maths marks : "))
# b = int(input("Enter your Physics marks : "))
# c = int(input("Enter your Chemistry marks : "))

# mean= (a+b+c)/3


# if mean in [91,92,93,94,95,96,97,98,99,100]:
#     print("your grade is A++")
# elif 81<=mean>=90:
#     print("your grade is A")
# elif 71<=mean>=80:
#     print("B+")
# elif 61<=mean>=70:
#     print("your grade is B")
# else:
#     print("your grade is C")



###########################################################################################################################################################


# a = int(input("Enter the number:"))
# b = int(input("Enter the number:"))

# a = str(a)
# b = str(b)

# for i in range(len(a)):
#     if a[i] in b:
#         print("Anagram")
#     else:
#         print("its not Anagram")
###########################################################################################################################################################


# a = int(input("Enter the number:"))
# b = int(input("Enter the number:"))
# c=0

# for i in range(0,4):
#     c = a%10
#     print(c)

#     a = a//10


# for i in range(10):
#     print(i)


# def list_comparasion(): 
#     a = [i for i in range(100) if i%4==0]
#     return a

# print(list_comparasion())

# a = [9,1,2,3,4,5,1]
# new_list = []
# def sudent_remove():
#     c = a.sort()
#     if a!=c:
#         new_list.append(c)
#         return new_list

# print(sudent_remove())
# L = []
# for i in range(10000000):
#     L.append("I LOVE YOU")
# print(L)



 
# with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\testing.txt",'w') as d:
#     d.write('''Hi, my name is Deepak Kumar.
# Currently I am a Btech student at CGU. 
# I have learned Python language as a techinical skills. 
# For a technical carrier my Aspiration is Mr. SUNDAR PICHAI, 
# cofounder of GOOGLE.''')


# with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\testing.txt",'a') as d:
#     d.write('''I love to play a Badmintion and riding Bike
#     ......Thanks::)  ''')
# with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\testing.txt",'r') as d:
#     print(d.read())



# import builtins
# c =[]
# identifiers = dir(builtins)

# for identifier in identifiers:
#     c.append(identifier)

# print(c)


# a = []
# for i in range(10000):
#     a.append("SORRY")
# print(a)



# import csv



# with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\meeting.csv", mode ='r')as file:
   
#   # reading the CSV file
#   csvFile = csv.reader(file)
 
#   # displaying the contents of the CSV file
#   for lines in csvFile:
#         print(lines)
# a =23
# n =a*2

# n2 = a*3
# print(str(a) +str(n)+ str(n2))
# a  = input("Enter your  fname ")
# b = input("Enter your lastname")
# for i in range(3):
#     print(a," ",b*3)

# n = int(input("Enter how many time you want to run the loop"))
# while n>0:
#     print(a)
#     n= n-1






# a = int(input("Enter a number"))

# b = str(a)*2
# c = str(a)*3
# print(a+int(b)+int(c))

# armstromg number
 
# n = int(input("Enter a number:"))
# s = n 
# b = len(str(n))
# sum1 = 0
# while n != 0:
#     r = n % 10
#     sum1 = sum1+(r**b)
#     n = n//10
# if s == sum1:
#     print("The given number", s, "is armstrong number")
# else:
#     print("The given number", s, "is not armstrong number")

# a = {1:"chiku",2:"ashu",3:"harshit"}
# for i in a:
#     print(i)


# alpha = []
# digit = []
# space = []
# name = input("Enter a your name:")
# for i in range(len(name)):
#     if name[i].isalpha():
#         alpha.append(name[i])
#     elif name[i].isdigit():
#         digit.append(name[i])
# a = len(alpha)
# b=len(digit)
# c = len(space)
# d = 15-(a+b)
# print(d)
# for i in range(d):
#     space.append(" ")
# print(alpha)
# final = str(alpha+space+digit)
# print(type(final))
# print(final)


# alpha = ' '
# digit =  ' '
# space = ' '
# name = input("Enter your name:")

# for i in range(len(name)):
#     if name[i].isalpha():
#         alpha+=name[i]
#     elif name[i].isdigit():
#         digit+=name[i]

# a = len(alpha)
# b = len(digit)
# c= 15-(a+b)
# for i in range(c):
#     space+=" "

# print(alpha + space + digit)

# a = eval(input("Enter a number:"))
# r_lst = []
# for i in range(len(a)-1,-1,-1):
#     r_lst.append(a[i])
# print(r_lst)


# my_array = [[0 for j in range(6)] for i in range(6)]
# my_array[0][0][0] = 1
# my_array[1][2] = 2
# my_array[2][3] = 3
# for row in my_array:
#     print(row)



# a = eval(input("Enter a list of  number"))
# c = a[1] + a [-2]
# j = int((len(a)-1)/2)
# print(j)
# k = a[j]

# if k==c:
#     print("middle number has been match")
# else:
#     print("did'nt match the middle number")
        
        
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     marks = student_marks[query_name]
#     average = sum(marks) / len(marks)
#     print('{:.2f}'.format(average))

# import numpy



# rows, columns,p = map(int, input().split())
# list_1 = []
# list_2 = []
# for i in range(rows):
#     a = list(map(int, input().split()))
#     list_1.append(a)
# for i in range(columns):
#     b = list(map(int, input().split()))
#     list_2.append(b)
# print( numpy.concatenate((list_1,list_2), axis = 0))







# import numpy as np
# shape = tuple(map(int, input().split()))
# zeros_array = np.zeros(shape, dtype=np.int64)
# ones_array = np.ones(shape, dtype=np.int64)
# print(zeros_array)
# print(ones_array)





# import numpy
# rows, columns = map(int, input().split())
# print(numpy.eye(rows,columns,k = 1))





# import numpy as np

# n, m = map(int, input().split())
# a = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     a.append(row)
# b = []
# for j in range(m):
#     row = list(map(int, input().split()))
#     b.append(row)
# print(np.add(a, b))
# print(np.subtract(a, b))
# print(np.multiply(a,b))
# print(np.divide(a,b))
# print(np.mod(a,b))
# print(np.power(a,b))



# n = int(input())  # Number of students

# students = []  # List to store students' names and grades

# for _ in range(n):
#     name = input()
#     grade = float(input())
#     students.append([name, grade])

# # Sort the students list based on grades in ascending order
# students.sort(key=lambda x:x[1])

# # Find the second lowest grade
# second_lowest_grade = students[1][1]

# # Create a list to store names of students with the second lowest grade
# names = []

# # Add names of students with the second lowest grade to the names list
# for student in students:
#     if student[1] == second_lowest_grade:
#         names.append(student[0])

# # Sort the names list alphabetically
# names.sort()

# # Print each name on a new line
# for name in names:
#     print(name)

# from itertools import permutations
# m, n = input().split()
# permutation_list = sorted(permutations(m, int(n)))
# for perm in permutation_list:
#     print(''.join(perm))





# from itertools import combinations
# s , n  = input().split()

# for i in range(1, int(n)+1):
#     for j in combinations(sorted(s), i):
#         print(''.join(j))



# from itertools import combinations_with_replacement
# s , n  = input().split()
# l=sorted(combinations_with_replacement(sorted(s),int(n)))
# for i in l:
#     print(''.join(i))






# from itertools import groupby
# def compress_string(s):
#     compressed_string = ""
#     for key, group in groupby(s):
#         count = len(list(group))
#         compressed_string += f"({count}, {key}) "
#     return compressed_string

# # Read the input string
# string = input().strip()

# # Compress the string
# compressed = compress_string(string)

# # Print the compressed string
# print(compressed)


# def print_formatted(number):
#     width = len(bin(number)[2:]) 

#     for i in range(1, number + 1):
#         decimal = str(i)
#         octal = oct(i)[2:]
#         hexadecimal = hex(i)[2:].upper()
#         binary = bin(i)[2:]

#         print(decimal.rjust(width), octal.rjust(width), hexadecimal.rjust(width), binary.rjust(width))

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)



# def average(a):
#     avg = 0
#     # a = set(array)
#     for i in range(len(a)):
#         v=sum(a)/len(a)
        
#     return v

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)



## Read the size of set A
#size_A = int(input())
#
## Read the elements of set A
#set_A = set(map(int, input().split()))
#
## Read the size of set B
#size_B = int(input())
#
## Read the elements of set B
#set_B = set(map(int, input().split()))
#
## Calculate the symmetric difference
#symmetric_diff = sorted(list(set_A ^ set_B))
#
## Print the symmetric difference
#for num in symmetric_diff:
#    print(num)


# n = int(input())
# stamps = [input() for _ in range(n)]
# distinct_stamps = set()
# for stamp in stamps:
#     distinct_stamps.add(stamp)

# print(len(distinct_stamps))



#s = ""
#number =int(input())
#digit = []
#while number>0:
#    d = number % 10
#    digit.append(d)
#    number //= 10
#for i in digit:
#    if i==0:
#        digit.remove(i)
#for i in digit:
#    s+= str(i)
#print(s)






#a = input("Enter a string")
#string = ""
#max = ord(a[0])
#for i in range(len(a)):
#    if ord(a[i])>max:
#        max=ord(a[i])
#        string=a[i]
#min = 0
#l = a.replace(string,"")
#for j in range(len(l)):
#        min+=ord(l[j]) 
#print(min)



# sum = int(input())
# l = eval(input())
# for j in range(len(l)):
#     for k in range(j,len(l)):
#         if l[j]+l[k]==sum:
#             print("the position are",j,k)
#             break



#def find_subarray_with_sum(sum, l):
#    for j in range(len(l)):
#        curr_sum = 0
#        for k in range(j, len(l)):
#            curr_sum += l[k]
#            if curr_sum == sum:
#                return [j+1, k+1] 
#    return [-1]  
#
#
#sum1 = int(input())
#arr1 = eval(input())
#result1 = find_subarray_with_sum(sum1, arr1)
#print(result1) 



# number =int(input())
# n= number
# digit = 0
# while number>0:
#     d = number % 10
#     digit = digit*10 +d
#     number //= 10
# if n==digit:
#     print("its a palandrom number")
# else:
#     print("its not a palandrom number")






#missing number
# l = eval(input())
# n= l
# expected_sum = sum(range(min(n), max(n) + 1))
# actual_sum = sum(n)
# if sorted(n) == list(range(min(n), max(n)+1)):
#     print("all ar in sequence")

# elif  sorted(n) != list(range(min(n), max(n)+1)):
#     missing_number = expected_sum - actual_sum
#     print("number missing",missing_number)





# my_list = eval(input())
# small = int(input())
# for i in range(len(my_list)):
#     for j in range(i + 1, len(my_list)):

#         if my_list[i] > my_list[j]:
#             my_list[i], my_list[j] = my_list[j], my_list[i]

# n= my_list
# print(n[small])




# a = int(input())
# c = 1
# for i in range(1,a+1):
#     c*=i
# print(c)

# def fact(n):
#     if n==0:
#         return 1
#     return n* fact(n-1)
# n= 26
# print(fact(n))


# import time
# start = time.time()

# for i in range(403291461126605635584000000):
#     print(i)
# end=time.time()
# print(end-start)



# n = int(input())
# fact = 1

# for i in range(1,n+1):
#     fact*=i

# print(fact)
# traling_zeros = 0
# while fact>0:
#     d = fact%10
#     if d==0:
#         traling_zeros+=1
#     fact//=10
# print(traling_zeros)




# a = int(input())
# b = int(input())

# while a!=b:
#     if a>b:
#         a-=b
#     else:
#         b-=a
# print(a)


#efficent way to check prime number

# def is_prime(number):
#     if number < 2:
#         return False
#     if number in (2, 3):
#         return True
#     if number % 2 == 0:
#         return False

#     for i in range(3, int(number**0.5) + 1, 2):
#         if number % i == 0:
#             return False
#     return True

# num_to_check = int(input())
# if is_prime(num_to_check):
#     print(f"{num_to_check} is a prime number.")
# else:
#     print(f"{num_to_check} is not a prime number.")

  

# a = int(input())
# lst = []
# for i in range(1,10):
#     if a%i==0:
#         lst.append(i)
# print(lst)



# a = int(input())
# lst = []
# for i in range(1,a+1):
#     if a%i==0:
#         lst.append(i)
# print(lst)



# import time
# start = time.time()
# def comp_power(x,n):
#     return x**n

# x = int(input())
# n= int(input())
# print(comp_power(x,n))
# end = time,time()
# print(start-end)




# def SieveOfEratosthenes(num):
# 	prime = [True for i in range(num+1)]
# 	p = 2
# 	while (p * p <= num):
# 		if (prime[p] == True):
# 			for i in range(p * p, num+1, p):
# 				prime[i] = False
# 		p += 1
# 	for p in range(2, num+1):
# 		if prime[p]:
# 			print(p)
# if __name__ == '__main__':
# 	num = int(input())
# 	print("Following are the prime numbers smaller"),
# 	print("than or equal to", num)
# 	SieveOfEratosthenes(num)


# def digitsInFactorial(N):
#     a=1
#     c = 0
#     if N==0 or N==1:
#         return 1
#     else:
#         for i in range(1,N+1):
#             a*=i
#     b = a
#     while b>0:
#         temp = a%10
#         c+=1
#         b//=10
#     return c
    
# n = int(input())
# print(digitsInFactorial(n))






# import math
# class Solution:
#     def exactly3Divisors(self, N):
#         count = 0
#         limit = int(math.sqrt(N))
#         primes = [True] * (limit + 1)
#         primes[0] = primes[1] = False
#         for i in range(2, int(limit ** 0.5) + 1):
#             if primes[i]:
#                 for j in range(i * i, limit + 1, i):
#                     primes[j] = False
        
#         for i in range(2, limit + 1):
#             if primes[i]:
#                 count += 1
        
#         return count

# solution = Solution()
# print(solution.exactly3Divisors(6)) 
# print(solution.exactly3Divisors(10)) 


# n = int(input())
# c = 0
# for i in range(1,n+1):
#     if n%i==0:
#         c+=1
#         print(i, end=' ')
# print('\n')
# print(c)


# class Solution:
#     def exactly3Divisors(self, N):
#         count = 0

#         def is_prime(num):
#             if num <= 1:
#                 return False
#             if num <= 3:
#                 return True
#             if num % 2 == 0 or num % 3 == 0:
#                 return False
#             i = 5
#             while i * i <= num:
#                 if num % i == 0 or num % (i + 2) == 0:
#                     return False
#                 i += 6
#             return True

#         for i in range(2, int(N**0.5) + 1):
#             if is_prime(i):
#                 count += 1
#         return count

# def main():
#     ob = Solution()
#     N = int(input("Enter a number: "))
#     print(ob.exactly3Divisors(N))

# if __name__ == "__main__":
#     main()





# import math
# a = int(input())
# b =  int(input())
# c= int(input())
# x = (b*b)-4*a*c
# s1 = (-b+math.sqrt(x))/2*a
# s2 = (-b-math.sqrt(x))/2*a
# print(int(s1))
# print(int(s2))



# class Solution:    
#     def modInverse(self, a, m):
#         def extendedEuclidean(a, b):
#             if b == 0:
#                 return a, 1, 0
#             gcd, x1, y1 = extendedEuclidean(b, a % b)
#             x = y1
#             y = x1 - (a // b) * y1
#             return gcd, x, y
#         gcd, x, y = extendedEuclidean(a, m)        
#         if gcd != 1:
#             return -1          
#         return (x % m + m) % m

# s = Solution()
# a1 = 2
# m1 = 1
# print(s.modInverse(a1, m1))  







# def avg(l):
#     return sum(l)/len(l)

# n= int(input())
# l = [int(input()) for i in range(n)]
# print(avg(l))


# def sep(l):
#     even = []
#     odd = []
#     for i in range(len(l)):
#         if i%2==0:
#             even.append(l[i])
#         elif i%3==0:
#             odd.append(l[i])
#     return even,odd
# n= int(input())
# l = [int(input()) for i in range(n)]
# a,b = sep(l)
# print(a,b)


# def duplicates(arr):
#     ans = []
#     n = len(arr)
#     freq = [0] * n
    
#     for i in range(n):
#         freq[arr[i]] += 1
    
#     for i in range(n):
#         if freq[i] > 1:
#             ans.append(i)
    
#     if not ans:
#         ans.append(-1)
    
#     return ans

# #__main__
# n = int(input())
# arr = []
# for i in range(n):
#     a = int(input())
#     arr.append(a)
# print(duplicates(arr))




# import statistics as st
# a = eval(input())
# print(st.stdev(a))




"""how to calculate standed devation in python"""

# import math
# def calculate_standard_deviation(data):
#     mean = sum(data) / len(data)
#     squared_diff = [(x - mean)**2 for x in data]
#     variance = sum(squared_diff) / len(data)
#     std_deviation = math.sqrt(variance)
#     return std_deviation
# data_list = eval(input())
# result = calculate_standard_deviation(data_list)
# print("Standard Deviation:", result)

 

# a = "ahfsabcuhfu"
# n = 'abc'
# if n in a:
#     print(True)
# else:
#     print(False)


# class Solution:
#     def singleElement(self, arr, n):
#         count_dict = {}
        
#         # Count the occurrences of each element in the array
#         for num in arr:
#             count_dict[num] = count_dict.get(num, 0) + 1
        
#         # Find the element with count 1
#         single_element = next(key for key, value in count_dict.items() if value == 1)
        
#         return int(single_element)

# a = Solution()
# arr = [3, 2, 1, 34, 34, 1, 2, 34, 2, 1]
# print(a.singleElement(arr,len(arr)))




# class Solution:
#     def checkPangram(self, s):
#         a = s.lower()
#         k = ''
#         for i in range(len(a)):
#             if a[i].isalpha():
#                 k+=a[i]
                
#         b = [i for i in range(97,123)]
#         for i in range(len(k)):
#             if ord(k[i]) in b:
#                 a = b.index(ord(k[i]))
#                 b[a]=0

#         for i in range(len(b)):
#             if b==[0]*26:
#                 return 1
#             else:
#                 return 0
            
# a = Solution()
# print(a.checkPangram('abcdefghijlmnopqrstuvwxyllll'))








# class Solution:
# 	def reverseKthelement(self,arr, k):
# 		c = arr
# 		a = []
# 		br=[]
# 		for i in range(k):
# 			br.append(arr[k])
# 			k+=1
# 		for i in range(len(arr)):
# 			if arr[i] not in br:
# 				a.append(arr[i])
# 		l = br[::-1]
# 		a[3:3]=l
# 		return a		


# a = Solution()
# print(a.reverseKthelement([1, 2, 3, 4, 5, 6, 7, 8],3))



# higest frequency of consecutive letter 
# a = 'AabhhkklhhHccaAahhhhbb'
# max_count = 0
# current_count = 1
# result_letter = ''

# for i in range(1, len(a)):
#     if a[i] == a[i-1]:
#         current_count += 1
#     else:
#         if current_count > max_count:
#             max_count = current_count
#             result_letter = a[i-1]
#         current_count = 1  


# if current_count > max_count:
#     max_count = current_count
#     result_letter = a[-1]

# print(result_letter, max_count)

    











# a = 'AabhhkklhhHccaAahhhhbb'
# a=a.lower()
# char_frequency = {}
# max_count = 0
# result_letter = ''

# for i in range(len(a)):
#     char = a[i]
#     char_frequency[char] = char_frequency.get(char, 0) + 1

#     if char_frequency[char] > max_count:
#         max_count = char_frequency[char]
#         result_letter = char

# print(char_frequency)







# a = [1,2,3,4,5,6,7]
# for i in range(len(a)):
#     if i

# l = [1, 2, 3, 4, 5, 6, 7]
# step = 1

# while len(l) > 1:
#     if step % 2 == 0:
#         l.remove(min(l))
#     else:
#         l.remove(max(l))
#     step += 1


# print(l)






# a = 'AabhhkklhhHccaAahhhhbb'
# char_frequency = {}
# max_count = 0
# m = 3
# c = 0
# g = []
# k = []
# for i in range(len(a)):
#     char = a[i]
#     char_frequency[char] = char_frequency.get(char, 0) + 1

# for j in char_frequency:
#     k.append(char_frequency[j])

# b = sorted(k)
# for i in range(m):
# print(c)






# a = [1,2,3,4,5,6,7,8,9,10]

# start = 2
# end=5
# k = a[start:end+1]
# r = a[:start]+k[::-1]+a[5:]
# print(r)




# s = "1: Pr567har Agrawal, 2: Manish Kumar Raii, 3: Rishabh Gupta56"
# p=''
# l=[]
# for i in range(len(s)):
#     if s[i].isdigit():
#         p+=s[i]
#         l.append(s[i])
# print(p)
# print(l)




# def kl(k):
#     if k<=0:
#         return 
#     print(k)
#     kl(k-1)
# kl(10)























































































































