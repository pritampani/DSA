# import string
# import random

# #from numpy import number

# s1 = string.ascii_lowercase
# #print(s1)
# #s2 = string.ascii_uppercase
# #print(s2)
# s3 = string.digits
# #print(s3)
# #s4 = string.punctuation
# #print(s4)

# plen=8
# s=[]
# s.extend(list(s1))
# #s.extend(list(s2))
# s.extend(list(s3))
# #s.extend(list(s4))

# print(s)
# number_pass=int(input("enter number of password you want:"))
# for i in range(number_pass):
#     random.shuffle(s)
#     print(''.join(s[0:plen]))



# num1 = int(input("Enter First number: "))    # taking input for first number
# num2 = int(input(" Enter Second number: "))    # taking input for second number
# sum = num1 + num2    # adding num1 and num2 and storing them in sum 
# print(sum)    # print sum to the screen



#fUNCTION


# def my_function(*kids):
#       print("The youngest child is " + kids[3])

# my_function("Emil", "Tobias", "Linus","chiku")


# def my_function(fname):
#       print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")


# def my_function(x):
#       return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))


# def myfunction():
#       pass



# def tri_recursion(k):
#       if(k > 0):
#             result = k + tri_recursion(k - 1)
#             print(result,end= ' ')
#       else:
#             result = 0
#       return result

# print("\n\nRecursion Example Results")
# tri_recursion(5)



# def chiku(str1):
#       print("this is" + str1)
      
# chiku("Harry")


# def factorial_iterative(n):
#     """
#         :param n: Integer
#         :return: n * n-1 * n-2 * n-3.......1
#     """
#     fac = 1
#     for i in range(n):
#         fac = fac * (i+1)
#     return fac
# number = int(input("Enter the number:"))
# print(factorial_iterative(number))
# def factorial_recursive(n):
#     if n ==1 or n==0:
#         return 1
#     else:
#         return n * factorial_recursive(n-1)
# numbr = int(input("p"))
# print(factorial_recursive(numbr))

    # 5 * factorial_recursive(4)
    # 5 * 4 * factorial_recursive(3)
    # 5 * 4 * 3 * factorial_recursive(2)
    # 5 * 4 * 3 * 2 * factorial_recursive(1)
    # 5 * 4 * 3 * 2 * 1 = 120


# write a function to calculate n fibonacci number by recursive methord.

# class Solution:
#     def nthFibonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n == 1:
#             return 1
#         fib = [0] * (n + 1)
#         fib[1] = 1
#         for i in range(2, n + 1):
#             fib[i] = (fib[i - 1] + fib[i - 2]) % 1000000007
#         return fib[n]


#WAP to take integer input from user and print the multipluction table of the number

# mult = int(input("Enter the number you want see that table:"))
# def multipluction(k):
      
#       if(k > 0):
#             result = mult + multipluction(k - 1)
#             print(result)
#       else:
#             result = 0
#       return result

# print("\n\nRecursion Example Results")
# multipluction(10)

# fname = input("WHAT IS YOUR NAME")
# lname = input("What is you last name")
# print("first name {} and last name is {}".format(fname,lname))

# for i in range(101):
#     if ((i%2!=0 and i%3!=0) and (i%3!=0 and i%4!=0)) and ((i%5!=0 and i%6!=0) and (i%7!=0 and i%8!=0)):
#         print('the prime number are',i)

# def isPalindrome(s):
#     return s == s[::-1]
 
 

# s = "malayalam"
# ans = isPalindrome(s)
 
# if ans:
#     print("Yes")
# else:
#     print("No")




# n = int(input("Enter a number: "))
# s = 0
# t = n
# while t > 0:

#    digit = t % 10

#    s += digit ** 3

#    t //= 10
# if n == s:

#    print(n,"is an Armstrong number")
# else:
#    print(n,"is not an Armstrong number")



num = int(input("Enter the number:"))

n1,n2 = 0,1

sum = 0

if num<=0:
       print("Please enter positive number:")
else:
       for i in range(0,num):
              print(sum,end=' ')
              n1=n2
              n2 = sum
              sum =n1+n2
















































































