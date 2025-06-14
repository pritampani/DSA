'''import time 
start=time.time()
a=int(input("enter a number"))
k=0
for i in range(2,a//2+1):
    if (a%i==0):
        k+=1
if k<=0:
    print("it is a prime number")
else:
    print("it's not a prime nummber")
end=time.time()
print(end-start)
'''
######################################################

# import time
# start=time.time()
# n=3
# x=1
# while x<=n:
#     y=1
#     while y<=n:
#         z=1
#         while z<=n:
#             print(x,y,z)
#             z=z+1
#         y=y+1
#     x=x+1
# end=time.time()
# print(end-start)

'''
def isEmpty(stk):
    if stk == []:
        return True
    else:
        return False

def push(stk,Item):
    stk.append(Item)
    top = len(stk) - 1

def display(stk):
    if isEmpty(stk):
        print("stack is empty")
    else:
        top = len(stk) - 1
        print(stk[top],"Top")
        for i in range(top-1,-1,-1):
            print(stk[i])

#__main__

Stack = []

top = None

while True:
    print("Stack OPERATION")
    print("1.Push")
    print("2.Display stack")
    print("3.Exit")
    ch = int(input("Enter your choice"))
    if ch ==1:
        bno = int(input("Enter book number to be inserted:"))
        bname = input("Enter Book name to be intrested:")
        Item = [bno,bname]
        push(Stack,Item)
        input()
    elif ch==2:
        display(Stack)
        input()
    elif ch==3:
        break
    else:
        print("Invalide choose!")
        input()
'''

# a = input("Enter the string")
# for i  in range(len(a)-1,-1,-1):
#     print(a[i], end = " ")



# lst=[1,1,2,[],3,5,[2,4,6],7,8,[],[]]
# a=[]
# for i in lst:
#     if i==a:
#         #if len(i)==0:
#         lst.remove(i)
# print(lst)


#Python | Remove empty tuples from a list

# s = set([1,2,3,4,5,6])
# s.add(1)
# s.add(2)
# print(s)
# print(type(s))


# a = "🤣"
# lst = []
# b = int(input("Enter the number you want to print a:"))
# for i in range(b):
#     lst.append(a)
# print(lst)


#####################################################################


# check the list is in range

# range_of_list = 5

# lst = eval(input("Enter the list of number:"))


# if len(lst) > range_of_list:
#     print("You have exeided the range of entering number")
# elif len(lst) == range_of_list:
#     print("you have enter the maximum charater")
# elif len(lst) < range_of_list:
#     print("you have not reach the maximum number")
# else:
#     print("kuch nai hosakta tera")



# a = "chiku"
# k = 234
# #b = "this is my year %s %s"%(a, k)
# b = "This is {1} {0}"
# c = a.format(a , k)

# print(c)


# a = 90
# print(bin(a))


# a = int(input("Enter the max number:"))
# b = int(input("Enter the max number:"))
# c = int(input("Enter the max number:"))

# if (a>b):
#     print("max is ",a)
# elif(b>c):
#     print("max is ",b)
# elif(c>a):
#     print("max is ",c)


# Function to convert decimal number
# to binary using recursion
# def DecimalToBinary(num):
	
# 	if num >= 1:
# 		DecimalToBinary(num // 2)
# 	print(num % 2, end = '')

# # Driver Code
# if __name__ == '__main__':
	
# 	# decimal value
# 	dec_to_binary=int(input("Enter the number the you want to conver to binary:"))
# 	# Calling function
# 	DecimalToBinary(dec_to_binary)



#Make a calculator

# while True:
#     sine = input("Enter the operator you want to assign [+,-,*,**,/,//]:")
#     num1 = int(input("enter the number:"))
#     num2 = int(input("Enter the number:"))
#     if sine== "+":
#         print("Sum of numbers are:",num1+num2)
#     elif sine=="-":
#         print("substraction of numbers are:",num1-num2)
#     elif sine=="*":
#         print("multipliction of number are:",num1*num2)
#     elif sine=="**":
#         print("expontital form of number are:",num1**num2)
#     elif sine=='/':
#         print("division of number are:",num1/num2)
#     elif sine=='//':
#         print("floor division of number are:",num1//num2)
#     elif sine!=['+','-','*','**','/','//']:
#         print("enter a valid operator!")
#         break





# how to find the majority element from a list


# def majority_element(num_list):
#         idx, ctr = 0, 1
        
#         for i in range(1, len(num_list)):
#             if num_list[idx] == num_list[i]:
#                 ctr += 1
#             else:
#                 ctr -= 1
#                 if ctr == 0:
#                     idx = i
#                     ctr = 1
        
#         return num_list[idx]

# print(majority_element([1, 2, 3, 4, 5, 5, 5, 4,5,8, 4,4,5, 5,4,4,4, 6]))





# a=int(input("enter first no:-"))
# b=int(input("enter second  no:-"))
# c=int(input("enter third no:-"))

# gre =a
# mini =a

# if a==b==c:
#     print("all the number you have input are equall")
# elif (gre>b):
#     print("greatest is a",a)




# a = int(input("Enter the first number:"))
# b= int(input('Enter the second number:'))
# c = int(input("Entr the third number:"))
# print(max(a,b,c))
# print(min(a,b,c))



# for i in range(101):
#     if [(i%2!=0 and i%3!=0) and (i%4!=0 and i%5!=0)] and [(i%6!=0 and i%7!=0) and (i%8!=0 and i%9!=0)]:
#         print(i)
# lst = []
# ls = [i for i in range(101) if i%1==0 ]
# lst.append(ls)
# print(lst)
# for i in lst:
#     if [(i%2!=0 and i%3!=0) and (i%4!=0 and i%5!=0)] and [(i%6!=0 and i%7!=0) and (i%8!=0 and i%9!=0)]:
#         print(i)


#To print the prime number upto which user tell.

# lower_value = int(input ("Please, Enter the Lowest Range Value: "))
# upper_value = int(input ("Please, Enter the Upper Range Value: "))

# print ("The Prime Numbers in the range are: ")
# for number in range (lower_value, upper_value + 1):
#     if number > 1:
#         for i in range (2, number):
#             if (number % i) == 0:
#                 break
#         else:
#             print(number)



#to find the repeted element from the the list.

# def Repeat(x):
#     _size = len(x)
#     repeated = []
#     for i in range(_size):
#         k = i + 1
#         for j in range(k, _size):
#             if x[i] == x[j] and x[i] not in repeated:
#                 repeated.append(x[i])
#     return repeated
 
# # Driver Code
# list1 =eval(input("Enter the list:"))
# print (Repeat(list1))
############################################################################################################################
#to find the repeted element from the the list.

# list1 =eval(input("Enter the list:"))
# r = []

# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] == list1[j] and list1[i] not in r:
#             r.append(list1[i])

# print(r)

############################################################################################################################
#Reverse Row sort in Lists of List
# test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
# print("The original list is : ",test_list)
# for ele in test_list:
#     ele.sort(reverse=True)
# print("The reverse sorted Matrix is : " , test_list)




#Pair elements with Rear element in Matrix Row
# test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5]]
# print("The original list is : ",test_list)
# res = []
# for i in test_list:
#     res.append([[j, i[-1]] for j in i[:-1]])
# print ("The list after pairing is : ",res)





###########################################################################################################################################################

# a = int(input("Enter your num1 : "))
# b = int(input("Enter your num2 : "))
# c = int(input("Enter your num2 : "))
# # logic-->1
# d = [a,b,c]
# if d[0]>d[1]:
#     print("greatest is :",d[0])
# elif d[1]>d[2]:
#         print("greatest is :",d[1])
# elif d[2]>d[1]:
#     print("greater is ",d[2])

# l = [a,b,c]

# if l[0]<l[1]:
#     print("smallest is :",d[0])
# elif l[1]<l[2]:
#         print("smallest is :",d[1])
# elif l[2]>l[1]:
#     print("smallest is ",d[2])


#logic -->2
# d = [a,b,c]
# largest = d[0]
# smallest = d[0]
# while True:
#     if d[1]>largest:
#         largest=d[1]
#     if d[2]>largest:
#         largest=d[2]
#     print(largest,"largest")
#     if d[1]<smallest:
#         smallest=d[1]
#     if d[2]<smallest:
#         smallest=d[2]
#     print(smallest,"smallest")
#     break


###########################################################################################################################################################
#to find the majority element from the list.

# list1 =eval(input("Enter the list:"))
# r = []

# for i in range(len(list1)):
#     for j in range(i+1,len(list1)):
#         if list1[i] == list1[j] and list1[i] not in r:
#             r.append(list1[i])

# print("The majority element are:",r)

###########################################################################################################################################################



# import pickle
# a = open("/home/dlb/Downloadsjohn_Wick.jpg",'rb')
# b =a.read()
# print(b)


# maths = int(input("Enter the marks:"))
# physics = int(input("Enter the marks:"))
# chemistry = int(input("Enter the marks:"))

# avg=(maths+physics+chemistry)/3

# if avg in [91,92,93,94,95,96,97,98,99,100]:
#     print("Grade is A+")
# elif avg in [81,82,83,84,85,86,87,88,89,90]:
#     print("Grade is A")
# elif avg in [71,72,73,74,75,76,77,78,79,80]:
#     print("Grade is B+")
# elif avg in [61,62,63,64,65,66,67,68,69,70]:
#     print("Grade is B") 
# else:       
#     print("Grade is C")

###########################################################################################################################################################
#Remove elements larger than a specific value from a list in Python

# a = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# limit =6
# b = [i for i in range(len(a)) if a[i]>6]
# print(b)
# limit = 3
# i=0
# while i<len(a):
#     if a[i]>limit:
#         a.remove(a[i])
#     i+=1
# for x in a:
#     print(x)
# limit = 3

# for i in a:
#     #print(type(i))
#     if i<limit:
#         a.remove(i)
# print(a)

###########################################################################################################################################################


# a = [1,'chiku',3,4,5,'bsdk',56]

# for i in a:
#     if str(a).isalpha():
#         list(a)[]
##############################################################################################################################################################
# import random
# import string
# import csv
# def add_patient(p_details):

#     patient_name = input("Enter the patient name:")
#     patient_phone_number = input("Enter the patient phone number:")
#     patient_Email = input("Enter patient email address:")
#     patient_age  = int(input("Enter the patient  age:"))
#     patient_Gender = input("Enter patient gender:")
#     patient_Issue = input("Enter the patient issue:")
#     s1 = string.ascii_lowercase
#     plen=8
#     s=[]
#     s.extend(list(s1))

#     for i in range(1):
#         for y in range(plen,16):
#             random.shuffle(s)
#             patient_ID = ''.join(s[0:y])
#     data = [patient_name,patient_phone_number,patient_Email,patient_age,patient_Gender,patient_Issue,patient_ID]
#     p_details.append(data)
#     with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\patient_details.csv",'w') as f:
#         csv_w = csv.writer(f,delimiter=',')
#         csv_w.writerow(data)
#         return csv_w



# p_details = []
# add_patient(p_details)


# def factorial(x):
#     result = 1
#     for i in range(2, x + 1):
#         result =result * i
#     return result
# a = 5
# print (factorial(a))


##############################################################################################################################################################

# def recursive_factorial(n):
#   if n == 1:
#      return n
#   else:
#      return n*recursive_factorial(n-1)


# number = int(input("Enter the number : "))
# print("The factorial of", number, "is", recursive_factorial(number))

########################################################################################################################################################

# def similar(str1, str2):
#     if len(str1)==len(str2):
#         if
 

# test_string1 = 'pritam'
# test_string2 = 'prachi'
# res = similar(test_string1, test_string2)
# print ("The similarity between 2 strings is : " + str(res))



# a = 'chiku'
# b = 'chintu'
# lst = []
# for i in range(len(a)):
#     for j in range(i-1,len(b)):
#         if a[i]==b[j]:
#             lst.append(a[i])
# print('The similarity between two string are:',lst)


# def sum(a,b):
#     return a+b
# n1 = int(input("Enter the number:"))
# n2 = int(input("Enter the number:"))
# print("sum of two number is:",sum(n1,n2))



# def Remove(dupl):
#     final_list = []
#     for num in duplicate:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list

# duplicate = eval(input("Enter the list of number:"))
# print(Remove(duplicate))


# def sum_three(number): 
#     a = number // 100
#     b = number // 10 % 10
#     c = number % 10
#     print(a + b + c)
# number = int(input("enter three digit number:"))
# c = sum_three(number)



# all_freq = {}
# f = open(r"C:\Users\ashut\OneDrive\Documents\testing.txt",'r')
# ch = f.read()
# for i in ch:
#     if i in all_freq:
#         all_freq[i] += 1
#     else:
#         all_freq[i] = 1

# print("Count of all characters in GeeksforGeeks is :\n " + str(all_freq))




# f = open(r"C:\Users\ashut\OneDrive\Documents\testing.txt",'r')
# ch = f.read()
# print("befor reversing:",ch)
# ch = ch[::-1]


# print("after reversing: ",ch)

# f = open(r"C:\Users\ashut\OneDrive\Documents\testing.txt",'r')
# a = f.read()
# b = f.readline()
# ch  = a.split()
# x = 0
# y = []
# z = 0

# for i in a:
#     x+=1
# for j in b:
#     y+=1
# for l in ch:
#     z+=1
# print("Number of charater are:",x)
# print("Number of lines are:",y)
# print("Number of words are:",z)


# f = open(r"C:\Users\ashut\OneDrive\Documents\testing.txt",'r')

# b = f.readlines()
# n = int(input("Enter the line you want to read:"))


# for j in range(n):
#     print(b)



# f = open(r"C:\Users\ashut\OneDrive\Documents\testing.txt",'r')
# string = f.readlines()
# print("befor deletion of data:",string)
# for i in range(len(string)):
#     string = string.clear()
#     print("after removing all data:",string)
# f.close()








# def count_file_stats(file_path):
#     with open(r"C:\Users\ashut\OneDrive\Desktop\file_path.txt", 'r') as f:
#         lines = f.readlines()
#         characters = sum(len(line) for line in lines)
#         words = sum(len(line.split()) for line in lines)
#         lines = len(lines)
#     return characters, words, lines

# file_path = r"C:\Users\ashut\OneDrive\Desktop\file_path.txt"
# characters, words, lines = count_file_stats(file_path)
# print(f'The file has {characters} characters, {words} words, and {lines} lines.')


# a = int(input("Enter you number:"))
# b  = int(input("Enter you number:"))
# c = int(input("Enter you number:"))

# if a>b:
#     print("a is max",a)
# elif b>c:
#     print("b is max",b)
# elif c>a:
#     print("c is max",c)
# elif a==b==c:
#     print("all the  number are equal")

# import datetime
# import os
# import smtplib
# import csv
# meetings = []

# while True:
#     # Print options to the user
#     print("1. Schedule a new meeting")
#     print("2. Reschedule an old meeting")
#     print("3. Cancel a meeting")
#     print("4. Exit")
#     # Get user's choice
#     choice = input("Enter your choice: ")
#     if choice not in ("1","2","3","4"):
#         print("invalid entery")
#     else:  
       
#         if choice == "1":
#             # Schedule a new meeting
#             # Get the details of the meeting
#             title = input("Enter the title of the meeting: ")
#             date = input("Enter the date of the meeting (YYYY-MM-DD): ")
#             start_time = input("Enter the start time of the meeting (HH:MM): ")
#             end_time = input("Enter the end time of the meeting (HH:MM): ")
#             participants_file = input("Enter the name of the file containing the participant email addresses: ")

#             # Generate a unique meeting ID
#             meeting_id = len(meetings) + 1

#             # Store the meeting details
#             meeting = [meeting_id, date, start_time, end_time, participants_file]
#             meetings.append(meeting)

#             # Write the meeting details to a CSV file
#             with open("meetings.csv", "a") as file:
#                 file.write(f"{meeting_id},{date},{start_time},{end_time},{participants_file}\n")
            
#                 meeting = {"title": title, "date": date, "start_time": start_time, "end_time": end_time}
#             # Add the meeting to the list
#             meetings.append(meeting)

#             print("Meeting scheduled successfully! Meeting ID:", len(meetings))

#             # Get participant emails
#             participant_file = input("Enter the name of the participant email file: ")
#             with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\participants_file.txt", 'r') as file:
#                 participant_emails = file.read().splitlines()

#             # Send email to participants with meeting details
#             sender_email = input("Enter your email address: ")
#             password = input("Enter your email password: ")
#             message = "Subject: Meeting Scheduled\n\nA meeting has been scheduled on {} at {} - {}.\nTitle: {}".format(date, start_time, end_time, title)
#             try:
#                 with smtplib.SMTP("smtp.gmail.com", 587) as server:
#                     server.ehlo()
#                     server.starttls()
#                     server.login(sender_email, password)
#                     for email in participant_emails:
#                         server.sendmail(sender_email, email, message)
#                     print("Meeting details sent to participants!")
#             except Exception as e:
#                 print("Error sending email:", e)
#         elif choice == "2":
#             # Reschedule a meeting
#             # Get the old meeting ID
#             old_meeting_id = int(input("Enter the ID of the old meeting: "))
#             # Check if the meeting ID exists
#             def update_meeting_time(old_meeting_id, new_time, meetings):
#                 found = False
#                 for meeting in meetings:
#                     if old_meeting_id in meeting:
#                         found = True
#                         meeting[old_meeting_id] = new_time
#                         break
#                 if not found:
#                     print("Meeting not found")
#                 return meetings

#              # Get the new meeting details
#             date = input("Enter the new date of the meeting (YYYY-MM-DD): ")
#             start_time = input("Enter the new start time of the meeting (HH:MM): ")
#             end_time = input("Enter the new end time of the meeting (HH:MM): ")
#             participant_file = input("Enter the name of the participant email file: ")
#             # Update the meeting details
#             meetings[1] = date
#             meetings[2] = start_time
#             meetings[3] = end_time
#             meetings[4] = participant_file
    
#             # Write the updated meeting details to the CSV file
#             with open("meetings.csv", "w") as file:
#                 for m in meetings:
#                     file.write(f"{m[1]},{m[2]},{m[3]},{m[4]}\n")
#                     # Get the participant emails
#             with open(r"C:\Users\ashut\OneDrive\Desktop\PYTHON\programing\python\participants_file.txt", 'r') as file:
#                 participant_emails = file.read().splitlines()
    
#             # Send email to participants with the updated meeting details
#             sender_email = input("Enter your email address: ")
#             password = input("Enter your email password: ")
#             message = "Subject: Meeting Rescheduled\n\nThe meeting has been rescheduled to {} at {} - {}.\nTitle: {}".format(date, start_time, end_time, title)
#             try:
#                 with smtplib.SMTP("smtp.gmail.com", 587) as server:
#                     server.ehlo()
#                     server.starttls()
#                     server.login(sender_email, password)
#                     for email in participant_emails:
#                         server.sendmail(sender_email, email, message)
#                     print("Meeting details sent to participants!")
#             except Exception as e:
#                 print("Error sending email:", e)
#             print("Meeting rescheduled successfully! Meeting ID:", old_meeting_id)

#         elif choice == "3":
#             import csv
#             def cancel_meeting(meeting_id):
#                 with open('meetings.csv', 'r') as file:
#                     reader = csv.reader(file)
#                     rows = [row for row in reader]
#                 with open('meetings.csv', 'w', newline='') as file:
#                     writer = csv.writer(file)
#                     for row in rows:
#                         if row[0] != meeting_id:
#                             writer.writerow(row)
#                 print(f"Meeting with ID {meeting_id} has been cancelled.")
#                 return

#             meeting_id = input("Enter the meeting ID: ")
#             cancel_meeting(meeting_id)
#         else:
#             # Exit the program
#             break
#     a=input("second time of operation , yes or no ")
#     if a=="no":
#         break
#     else:
#         continue  

# list1 = [2,1,3,4,5,6,65656,56]
# max = list1[0]
# for x in list1:
#     if x > max:
#         max = x
# print(max)
# print("Largest element is:", max)



# number = 123
# c = str(number)
# f = 0
# for i in range(len(c)):
#     f=f+int(c[i])
#     print(f)

# x=30
# y=20
# print(x,"+",y,"=",x+y)


# n = int(input("Enter a number:"))
# rev = 0
 
# while(n > 0):
#     a = n % 10
#     rev = rev * 10 + a
#     n = n // 10
 
# print(rev)


# lst = eval(input("Enter a list of number "))
# count=0
# for i in range(len(lst)):
#     count+=lst[i]
# print(count)



# def miniMaxSum(arr):
#     # Write your code here
#     l_s = []
#     s_s = []
#     new_list = []

#     while arr:
#         minimum = arr[0]  # arbitrary number in list 
#         for x in arr: 
#             if x < minimum:
#                 minimum = x
#         new_list.append(minimum)
#         arr.remove(minimum)    
#     for i in range(len(new_list)-1):
#         s_s.append(new_list[i])
#     new_list.pop(0)
#     for i in range(len(new_list)):
#         l_s.append(new_list[i])
#     a = sum(l_s)
#     b = sum(s_s)
#     return a , b 
# arr = list(map(int, input().split()))
# a,b = miniMaxSum(arr)
# print(a,b)


# for i in range(len(new_list)):
#     new_list[i].pop(0)
#     l_s+=new_list[i]
#     new_list[i].pop(-1)
#     s_s+=new_list[i]
# print(l_s)
# print(s_s)



# def birthdayCakeCandles(candles):
#     max_height =candles[0]
#     for i in candles:
#         if i> max_height:
#             max_height = i
#     count = 0
#     # count = candles.count(max_height)
#     for i in candles:
#         if (i == max_height):
#             count = count + 1
#     return count

# if __name__ == '__main__':
#     candles = list(map(int , input().split()))  
#     result = birthdayCakeCandles(candles)
#     print(result)




# s = input("Enter the time in hh:mm:ss am/pm")
# tc = ""
# A = str(s[8] + s[9])
# if A == "PM" or A == "pm":
#     hh = s[0:2]
#     if hh == '12':
#         h = int(hh)
#     else:
#         h = 12 + int(hh)
#     h0 = str(h).zfill(2)
#     tc = h0 + ":" + s[3:5] + ":" + s[6:8]
# elif s.startswith('12') and (s.endswith('AM') or s.endswith('am')): 
#     tc = "00" + s[2:8]
# elif A == 'AM' or A == 'am':
#     tc = str(s[0:8])
# print(tc)



# ar = [1,3,2,6,1,2]
# k = 3
# c= 0
# for i in range(len(ar)):
#     for j in range(i+1,len(ar)):
#         if (ar[i]+ar[j])%k==0:
#             c+=1
# print(c)


# ar = [1, 2, 3, 4, 5, 6]
# k = 5
# count = 0

# for i in range(len(ar)):
#     for j in range(i+1, len(ar)):
#         if (ar[i] + ar[j]) % k == 0:
#             count += 1

# print(count)




# ar = [1, 3, 2, 4, 2, 2, 1, 3, 3, 2, 4, 4, 4]
# highest_freq_element = None
# highest_freq_count = 0

# for i in range(len(ar)):
#     count = 0
#     for j in range(i, len(ar)):
#         if ar[j] == ar[i]:
#             count += 1
#     if count > highest_freq_count:
#         highest_freq_count = count
#         highest_freq_element = ar[i]

# print("Highest frequency element:", highest_freq_element)
             
                    
# def kangaroo_jump(x1, v1, x2, v2):
#     if x1 == x2 and v1 == v2:
#         return "YES"

#     if x1 == x2 and v1 != v2:
#         return "NO"
#     if v1 > v2 and x1 > x2:
#         return "NO"
#     if v2 > v1 and x2 > x1:
#         return "NO"
#     if v1 != v2 and (x2 - x1) % (v1 - v2) == 0:
#         return "YES"
#     else:
#         return "NO"
# #__main__
# x1 = int(input())
# v1 = int(input())
# x2 = int(input())
# v2 = int(input())
# kangaroo_jump(x1,v1,x2,v2)

# lst = []
# for i in range(1,11):
#     for j in range(1,11):
#         lst.append(i*j)
# print(lst)


# def plusMinus(arr):
#     # Write your code here
#     p =0
#     n =0 
#     z =0
#     for i in range(len(arr)):
#         if arr[i]>0:
#             p+=1
#         elif arr[i]<0:
#             n+=1
#         elif arr[i]==0:
#             z+=1

#     k = str(p/len(arr)) + str('0000')
#     b = str(n/len(arr))+ str('0000')
#     c = str(z/len(arr))+ str('0000')
#     return k , b ,c
# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     a,b,c = plusMinus(arr)
#     print(a)
#     print(b)
#     print(c)                                                                    


                                                                                                                                                                      
            
# def staircase(n):
#     for i in range(1, n + 1):
#         spaces = " " * (n - i)
#         hashes = "#" * i
#         c =spaces + hashes
#         print(c)
# if __name__ == '__main__':
#     n = int(input().strip())
#     staircase(n)



# def dayOfProgrammer(year):
#     if year == 1918:
#         return '26.09.1918'
#     elif (year <= 1917 and year % 4 == 0) or (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)):
#         return '12.09.' + str(year)
#     else:
#         return '13.09.' + str(year)


# if __name__ == '__main__':
#     year = int(input().strip())
#     result = dayOfProgrammer(year)
#     print(result)



# import numpy
# a = eval(input())
# my_array = numpy.array(a)
# print(numpy.reshape(my_array,(3,3)))

    


# def avg(*num):
#     if len(num)==0:
#         return None
#     sum=0
#     for i in num:
#         sum=sum+i
#         moy=sum/len(num)
#     return(moy)

    

# if __name__ == '__main__':
    
#     nums = map(int,input().split())                 
#     res = avg(*nums)
#     print(res)





# n = int(input())  # number of elements in the tuple
# integer_list = list(map(int, input().split()))  # input elements as integers

# result = hash(tuple(integer_list[i]) for i in range(n))  # compute the hash value of each element and calculate the overall hash value
# print(result)  # print the result





 # a = [8,5,6,7,4]

# c = []
# for i in range(len(a)):
#     if a[i]<max(a) and a[i] not in c:
#         c .append(a[i])
# k=c.sort()  
# print(c[-1])

#romanvalue to number

# class Solution(object):
#     def romanToInt(self, s):
#         dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#         result = 0
#         prev_value = 0
#         for i in range(len(s)):
#             current_value = dic[s[i]]
#             if current_value > prev_value:
#                 result += current_value - 2 * prev_value
#             else:
#                 result += current_value
#             prev_value = current_value
#         return result





# head =eval(input())

# b = []
# for i in range(len(head)-1,-1,-1):
#     b.append(head[i])
# if head==b:
#     print("True")
# else:
#     print("False")
    
    
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# # Accessing elements using nested loops
# for sublist in nested_list:
#     for element in sublist:
#         print(element)

    





# a = [10, 20, 30, 40, 50]

# b = []
# for i in range(len(a)):
#     b.append(sum(a[i]))


# print(b)





# from collections import Counter

# # Example with a string
# s = "abccc"
# char_count = Counter(s)
# print(char_count)




# class Solution:
#     def swapNibbles (self, n):
#         # code here 
#         a=bin(n)[2:]
#         b=a.zfill(8)
#         k=b[4:]
#         h=b[:4]

#         m=k+h
#         return int(m,2)

# a = Solution()
# print(a.swapNibbles(100))



# class Solution:
#     def findSubString(self, str):
#         # Your code goes here
#         c=''
#         k=0
#         for i in range(len(str)):
#             for j in range(i+1,len(str)):
#                 if (len(str[i:j])==len(set(str[i:j])))  and len(set(str[i:j]))>k:
#                     c=set(str[i:j])
#                     k=len(set(str[i:j]))
#                 else:
#                     continue
#         return c
# a=Solution()
# print(a.findSubString('aabcbcdbca'))
















































































































































































































































































































































