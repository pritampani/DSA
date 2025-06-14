# bugrger_in_stock = 10
# burger_you_want = int(input("Enter how many burger you want??"))
# if bugrger_in_stock<burger_you_want:
#        print("SORRY WE ARE OUT OF STOCK")
# else:
#     while bugrger_in_stock>0:
#            if burger_you_want<bugrger_in_stock:
#               print("WE ARE IN STOCK")
#               print("REMAINING BURGER ARE",bugrger_in_stock-burger_you_want)
#               print("THANKS FOR COMING!")
#               break


# lst = eval(input("Enter a list of number:"))
# result = 1
# for i in lst:
#        print(result*i)
# l = []
# for i  in range(11):
#        l = l+[i]

# for j in l:
#        print(j*j)
# print(l)

#a = [10,20,30,[40,50,60,[70,8.563],90,100],113452.435620,120]
#a[3][3][1] =10000
# print(a)

# # c = ['mcstan','mcsqure','mclofer']
# c = [1,2,3,4,4]
# k = a.extend(c)
# print(k)


# l=[1,2,3]
# b=[4,5,6]
# b.extend(l)
# print(b)



# Wap write a unique value and repeated value from list in the list.
# list1 =eval(input("Enter the list:"))
# _size = len(list1)
# repeated = []
# unique = []
# for i in range(_size):
#     k = i + 1
#     for j in range(k, _size):
#         if list1[i] == list1[j] and list1[i] not in repeated:
#             repeated.append(list1[i])

# print('Repeted element are:',repeated)

# list1 = set(list1)
# print("Unique element are",list(list1))


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





# num = int(input("Enter a number:"))
# sum = 0
# if num<0:
#        print("Enter the positive number:")
# else:
#        while (num>0):
#               sum+=num
#               num-=1
#        print("The sum is ",sum)

# to print finbonaccy series
# num = int(input("Enter the number:"))

# n1,n2 = 0,1

# sum = 0

# if num<=0:
#        print("Please enter positive number:")
# else:
#        for i in range(0,num):
#               print(sum,end=' ')
#               n1=n2
#               n2 = sum
#               sum =n1+n2

              

# n = int(input("Enter the number:"))

# sum = 0

# order = len(str(n))

# copy_n = n

# while(n>0):
#    digit = n%10
#    sum+=digit**order
#    n= n//10

# if (sum==copy_n):
#    print(copy_n,'is a armsstrong number')
# else:
#    print(copy_n, 'is not an armstrong number')




# a = int(input("Enter the number:"))

# for i in range(0,4):
#     c = a%10
#     print(c)
#     if c==b:
#         print("Anagram")
#     else:
#         print("it's not an anagram")
#     a = a//10


# a = [1,2,4,5,6,9,5,9,76,54]
# print(a[1])
# print(type(a))
# b = (1,2,4,4,46)

# print(type(b))




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



# a = int(input("Enter a number"))
# r = 0
# while (a>0):
#     n = a%10
#     r=r*10 +n
#     a=a//10
# print(r)




























































    