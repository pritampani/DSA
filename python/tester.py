# a=open('/home/dlb/Desktop/flappy_bird-v1-3.txt','r')
# data=a.read()
# print(data)
# a.close()

#
#import string
#
#a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#b = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
#for i in a:
#    c = print(ord(i))
#for j in b:
#    d = print(ord(j))
#
#if a in string.ascii_lowercase():
#    print("it is a lower case alphabate")
#elif b in string.ascii_uppercase():
#    print("it is uppar case alphabate")
#
#else:
#    print("sorry there is no charater")
#


# arr =  [1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1] = arr[i]
# print(arr)
# for i in range(0,6):
#     print(arr[i],end='')


# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*", end = ' ')
#     print()



# n=6
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end= " ")
#     for j in range(i+1):
#         print("*", end=' ')
#     print()


#how to remove duplicate element from the list



# lst =  eval(input("Enter the list:"))
# print("Original List",lst)
# res = [*set(lst)]
# print("List after removing element:",res)



#input--->a#$%^fwf$%^&
#output---->awf#$%^!@#$














# class Solution:
#     def modifyQueue(self, q, k):
#         a = []
        
#         # Extract the first k elements from the front of the queue and reverse them
#         for i in range(k):
#             a.append(q.pop(0))
#         a.reverse()
        
#         # Append the remaining elements to the reversed subsequence
#         for i in range(len(q)):
#             a.append(q.pop(0))

#         return a

# a = Solution()
# result = a.modifyQueue([1, 2, 3, 4, 5], 3)
# print(result)

a,b,c=1,1,1
d = 0.3







a = [0,11,0,2,3,4,0,5,6,7,0,1,0]
for i in range(1,5):
    print(i)
