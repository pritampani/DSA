def addbook(book,Data):
    nbook = input("Enter the book name")
    book_no = int(input("Enter the book no."))
    Data=[nbook,book_no]
    book.append(Data)

def deletBOOK(book):
    if book==[]:
        print("Stack is empty")
    else:
        print("Delet element is", Book.pop())

def displaybook(book):
    if book==[]:
        print("stack is empty!")
    else:
        print(book)

# #__main__

# book =  []

# while True:
#     print("1.add")
#     print("2.deletebook")
#     print("3.display")
#     print("4.break")
#     ch = input("Enter your choice:")
#     if ch ==1:
#         addbook(book,Data)
#     elif ch==2:
#         deletBOOK(book)
#     elif ch==3:
#         displaybook(book)
#     else:
#         break


#******************************************************************************************************************************************************************************8

#to print the prime number upto which user told

# lower_value = int(input("Enter the lower number:"))
# higher_value = int(input("Enter the higher value:"))

# for  number in range(lower_value,higher_value):
#     if number>1:
#         for i in range(2,number):
#             if (number%i)==0:
#                 break
#         else:
#             print(number)































#WAP to seperate digit from string
# def push(N,e):
#     N.append(e)

# def show(N):
#     if len(N)==0:
#         print("stack is empty!")
#     else:
#         print(N,end = ' ')
# N=[]
# string = input("Enter the string:")
# for k in range(len(string)):
#     if (string[k].isdigit()):
#         push(N,string[k])
# show(N)

#*************************************************************************************

#WAP seperate number which are divisible by 2.

# def push(N,e):
#     N.append(e)
# def show(N):
#     if len(N)==0:
#         print("stack is empty!")
#     else:
#         print("the list is ",N)

# N=[]
# lst = eval(input("Enter the list of number:"))

# for i in range(len(lst)):
#     if lst[i]%2==0:
#         push(N,lst[i])

# show(N)

#*****************************************************************************************************************************


#WAP seperate number which are divisible by 2 or 3 or 4 or 5 

# def push1(a,b):
#     a.append(b)
# def push2(c,d):
#     c.append(d)
# def push3(e,f):
#     e.append(f)
# def push4(g,h):
#     g.append(h)


# def show1(a):
#     if len(a)==0:
#         print("Stack is empty!")
#     else:
#         print("The number divisible by 2 is:",a)

# def show2(c):
#     if len(c)==0:
#         print("Stack is empty!")
#     else:
#         print("The number divisible by 2 is:",c)
# def show3(e):
#     if len(e)==0:
#         print("Stack is empty!")
#     else:
#         print("The number divisible by 2 is:",e)
# def show4(g):
#     if len(g)==0:
#         print("Stack is empty!")
#     else:
#         print("The number divisible by 2 is:",g)
# a=[]
# c=[]
# e=[]
# g=[]
# lst = eval(input("Enter the the list of number:"))

# for i in range(len(lst)):
#     if lst[i]%2==0:
#         push1(a,lst[i])
#     elif lst[i]%3==0:
#         push2(c,lst[i])
#     elif lst[i]%4==0:
#         push3(e,lst[i])
#     elif lst[i]%5==0:
#         push4(g,lst[i])

# show1(a)
# show2(c)
# show3(e)
# show4(g)

#*****************************************************************************************************************************

# R = {1:"PRITAM",2:'SW',3:'diba'}

# def push(N,e):
#     N.append(e)
# def show(N):
#     if len(N)==0:
#         print("Stack is empty!")
#     else:
#         print(N)

# N=[]

# for i in  R:
#     if i>=0:
#         push(N,i)

# show(N)

#*****************************************************************************************************************************

# def push(N,e):
#     N.append(e)

# def show(N):
#     if len(N)==0:
#         print("stack is Empty!")
#     else:
#         print(N)

# #lst = eval(input("Enter the list:"))
# N=[]
# lst = [12,1,3,8,34,76,2345,3444,4555,5555,6666,7777]

# for i in range(len(lst)):
#     if lst[i]+lst[i]>=100:
#         push(N,lst[i])


# show(N)

#*****************************************************************************************************************************



#WAP that depend  upon user either to add or remove the element from stack.
# lst=[12,1,3,8,34,76,2345,3444,4555,5555,6666,7777]
# def addelement(N,e):
#     e = int(input("Enter the element you want add:"))
#     N.append(e)
# def removeelement(N):
#     if N==N:
#         print("Stack is Empty!")
#     else:
#         c = int(input("enter the element to remove from list:"))
#         if c in N :
#             N.remove(c)

# def showelement(N):
#     if N==N:
#         print("Stack is not modified")
#     else:
#         print("After modification of list ",N)
# #__main__


# print("1.addelement")
# print("3.Removeelement")
# print("4.show element")
# c = input("Enter your choice:")

# if c==1:
#     addelement(N)
# elif c==2:
#     removeelement(N)
# elif c==3:
#     showelement(N)

#*****************************************************************************************************************************

# N=[12,1,3,8,34,76,2345,3444,4555,5555,6666,7777]

# a=int(input("Enter the number you want to add:"))

# N.append(a)

# print(N)

# c = int(input("enter the element to remove fromo list:"))

# if c in N :
#     N.remove(c)

# print(N)


#***********************************************************************************************************************************



