# A=10
# B=20
# MAX = A if A>B else B
# print(MAX)


# def find_majority(k):
#     def hash_it(q):
#         return q

#     map_of = [0]*len(k)

#     for i in k:
#         mapped_to = hash_it(i) #hash function
#         map_of[mapped_to]+=1


# find_majority([1,2,3,4,3,3,2,4,5,6,1,2,3,4,5,1,2,3,4,6,5])

#write a python program to purposefully raise indention error and correct it.
#incorrect
# lst = 22
# if lst/2:
# print(lst)

# #correct
# lst = 22
# if lst/2:
#     print(lst)

# write the python program to print student informaration(name,regd.no,branch,group)
# name = input("Enter your name:")
# regd_no = int(input("Enter the registationn number:"))
# branch = input("Enter your branch:")
# group = input("Enter your group:")
# print("your name is:",name)
# print("your registation number is:",regd_no)
# print("your branch is:",branch)
# print("your group is:",group)



# import datetime

# current_time = datetime.datetime.now()

# print("Time and date now at india is :", current_time)


#Write a program to  print area of triangle

# base = int(input("Enter the base length of base:"))
# height = int(input("Enter the height:"))
# print("Area of Triangle is:",0.5*base*height)
#


#write a program to find the ASCII value of character

# ASCII = input("Enter the character you want that ascii value:")
# print("The ascii value is:",ord(ASCII))

 #Given variable x = 30 and y = 20, write a python program to print "30 + 20 = 50"

# x = 30
# y = 20
# print(str(x),'+',str(y),'=',x+y)

#write a python program which accept the radius of circle from user and comput the area.

# radius = int(input("Enter the radius of circle:"))
# print("Area of circle is:",3.141*radius*radius) #Formula to find the area of circle






# how to use list comprehensions in python
# def even():
#     return [i for i in range(11) if i%2==0]
# def odd():
#     return [i for i in range(11) if i%2!=0]

# #__main__

# a = even()
# b = odd()
# print(a,b)



# def xyz(l,x):
#     return [i for i in l if i<x]
# l = [1,2,3,4,5,10,6,7,7,8,9]
# x = 5
# a = xyz(l,x)
# print(a)





#to find largest and sevcond largest

# def m(l):
#     if not l:
#         return None
#     else:
#         m1 = l[0]
#         for i in range(len(l)):
#             if l[i]>m1:
#                 m1 = l[i]
#         m2 = l[0]
#         for i in range(len(l)):
#             if l[i]<m1:
#                 m2=l[i]
#         return m1 , m2
# l = eval(input())
# w = m(l)
# print(w)




#check the list sorted or not

# def check_sort(l):
#     i = 1
#     while i<len(l):
#         if l[i]<l[i-1]:
#             return False
#         i+=1
#     return True
# a = eval(input())
# b = check_sort(a)
# print(b)






#reverse the list
#pritams methords

# def reverse(l):
#     a = []
#     for i in range(len(l)+1):
#         a.append(l[-i])
#     a.pop(0)
#     return a

# l = eval(input())
# b = reverse(l)
# print(b)



# def reverse(l):
#     s = 0
#     e = len(l)-1
#     while s<e:
#         l[s],l[e] =l[e], l[s]
#         s+=1
#         e-=1

# l = eval(input())
# reverse(l)
# print(l)





#remove duplicate from non shorted array
# def Remove(dupl):
#     final_list = []
#     for num in dupl:
#         if num not in final_list:
#             final_list.append(num)
#     return final_list

# a = [1,2,3,3,4,4,4,4,4,5,4,4,4,3,3,3,3,3,4,5,4,4,4,4,4,4,4,4,6]
# b = Remove(a)
# print(b)






#remove duplicate from sorted array
#galat he ye code
# def rem_dup(l,n):
#     a = 1
#     for i in range(1,n):
#         if(l[a-1]!=l[i]):
#             l[a]=l[i]
#             a+=1
#     return a

# l = [1,2,3,1,4,55,4,3,3,2,2,2,3,4,4,4,3,3,2,2,3,3,4,3,2,2]
# a = rem_dup(l,len(l))
# print(a)






#immidate smaller in the array
# def immediateSmaller(arr,x):
#     closest_smaller = -1  # Initialize to a value that indicates no smaller element found
#     for current_element in arr:
#         if current_element < x:
#             # Update closest_smaller if the current_element is closer to X           
#             if closest_smaller == -1 or abs(x - current_element) < abs(x - closest_smaller):
#                 closest_smaller = current_element

#     return closest_smaller
# #__main__
# l = [1,4,2,3,7,8,5,9]
# x = int(input())
# print(immediateSmaller(l,x))





# def immediateGreater(arr,x):
#     closest_greater = 0
#     for current_element in arr:
#         if current_element > x:
#             if closest_greater == 0 or abs(x - current_element) < abs(x - closest_greater):
#                 closest_greater = current_element
#     return closest_greater if closest_greater != float('inf') else -1

# #__main__
# l = [1,4,2,3,7,8,5,9]
# x = int(input())
# print(immediateGreater(l,x))






# A = [1, 2, 3, 4, 5]
# D = int(input())
# D%=len(A) 
# c = [A.pop(0) for _ in range(D)]
# d=A+c
# print(d)





#game of XOR
# class Solution:
#     def gameOfXor(self, N, A):
#         if N % 2 == 0:
#             return 0
#         ans = A[0]
#         for i in range(2, N, 2):
#             ans ^= A[i]
#         return ans




# def fib(n):
#     if n==0:
#         return 0
#     if n==1:
#         return 1
#     return fib(n-1) + fib(n-2)
# print(fib(4))





# def fun(n):
#     if n<=1:
#         return 0
#     else:
#         return fun(n//2)+1
# print(fun(27))




# def rec(n):
#     if n<=0:
#         return
#     rec(n-1)
#     print(n)
# rec(3)



# def rec(n):
#     if n<=0:
#         return
#     print(n)
#     rec(n-1)
    
# rec(3)





# def isPalRec(st, s, e) :
# 	if (s == e):
# 		return True
# 	if (st[s] != st[e]) :
# 		return False
# 	if (s < e + 1) :
# 		return isPalRec(st, s + 1, e - 1);
# 	return True

# def isPalindrome(st) :
# 	n = len(st)
# 	if (n == 0) :
# 		return True
# 	return isPalRec(st, 0, n - 1);
# st = "geeg"
# if (isPalindrome(st)) :
# 	print("Yes")
# else :
# 	print("No")







#print an array using recursion

# class Solution:
#     def printArrayRecursively(self, arr, n):
#         # Base case: if index is out of bounds, return
#         if n == 0:
#             return
#         self.printArrayRecursively(arr, n - 1)
#         # Print the current element
#         print(arr[n - 1], end=' ')





#count how many digites are there in a number
# def countDigits(n):
#     if n<10:
#         return 1
#     return 1+countDigits(n//10)
# a = 1233452
# print(countDigits(a))
        

# class Solution:	
#     #Function to reverse every sub-array group of size k.
# 	def reverseInGroups(self, arr, n, k):
# 		# code here
# 		a = []
# 		for i in range(k):
# 		    a.append(arr[i])
# 		a.reverse()
		
		
    
# a = Solution()
# print(a.reverseInGroups([1,2,3,4,5],5,3))


#searching
#binary search

# import time
# def binary_search(arr,x):
    # l = 0
    # r = len(arr)-1
    
    # while l<=r:
    #     mid = (l+r)//2
        
    #     if arr[mid]==x:
    #         return mid
    #     elif arr[mid]<x:
    #         l=mid+1
    #     elif arr[mid]>x:
    #         r = mid -1
    # return -1
# start = time.time()     
# print(binary_search([1,2,3,4,5,6,7,8,9],6))
# end = time.time()
# print(start-end)






#recursive binary search

# def rec_binary(list,x,low,high):
    # mid = (low+high)//2
    # if low>high:
    #     return -1
    # if list[mid]==x:
    #     return mid
    # elif list[mid]<x:
    #     return rec_binary(list,x,mid+1,high)
    # elif list[mid]>x:
    #     return rec_binary(list,x,low,mid-1)
# def bsearchmain(l,x):
#     return rec_binary(a,6,0,len(a)-1)
# a = [1,2,3,4,5,6,7,8,9]
# print(bsearchmain(a,6))
    
    






#index of first occurance of an element in searching
# note this will work only in sorted arrayx


# def f_occurance(arr,x):
#     l = 0
#     r = len(arr)-1  
#     while l<=r:
#         mid = (l+r)//2
#         if arr[mid]<x:
#             l=mid+1
#         elif arr[mid]>x:
#             r = mid -1
#         else:
#             if mid==0 or arr[mid-1]!= arr[mid]:
#                 return mid
#             else:
#                 r = mid -1
#     return -1
        
# print(f_occurance([1,2,4,5,6,7,8,9],6))







#last occurance of a element in a list
#we can make this by using abinary search algoridim

# def lastocc(l, x):
#     low = 0
#     high = len(l) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if l[mid] < x:
#             low = mid + 1
#         elif l[mid] > x:
#             high = mid - 1
#         else:
#             if mid == len(l) - 1 or l[mid] != l[mid + 1]:
#                 return mid
#             else:
#                 low = mid + 1
#     return -1

# print(lastocc([1, 2, 4, 5, 6, 6, 6, 6, 7, 8, 9], 6))







#count the occurance of an element 
#by using binary search methord


# def c_occurrence(l, x):
#     def find_first_occurrence():
#         low, high = 0, len(l) - 1
#         first = float('inf')
#         while low <= high:
#             mid = (low + high) // 2
#             if l[mid] == x:
#                 first = min(first, mid)
#                 high = mid - 1
#             elif l[mid] < x:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return first

#     def find_last_occurrence():
#         low, high = 0, len(l) - 1
#         last = -1
#         while low <= high:
#             mid = (low + high) // 2
#             if l[mid] == x:
#                 last = max(last, mid)
#                 low = mid + 1
#             elif l[mid] < x:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return last

#     first_occurrence = find_first_occurrence()
#     if first_occurrence == float('inf'):
#         return 0  # Element not found
#     last_occurrence = find_last_occurrence()
#     return last_occurrence - first_occurrence + 1
# print(c_occurrence([1, 2, 4, 5, 6, 6, 6, 6, 7, 8, 9], 6))











# def twoSum( nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return i ,j

# print(twoSum([3, 2, 4], 6))






#number of 1's in binary tree 

# def f_occurance(arr,x):
#     l = 0
#     r = len(arr)-1  
#     while l<=r:
#         mid = (l+r)//2
#         if arr[mid]<x:
#             l=mid+1
#         elif arr[mid]>x:
#             r = mid -1
#         else:
#             if mid==0 or arr[mid-1]!= arr[mid]:
#                 return len(arr)-3
#             else:
#                 r = mid -1
#     return -1
        
# print(f_occurance([0,0,0,1,1,1,1],1))






#root over of any number

# def sqrootfloor(n):
#     low=1 
#     high=n 
#     ans=-1
#     while(low<=high):
#         mid=(low+high)//2
#         msq=mid*mid
#         if(msq==n):
#             return mid
#         elif (msq>n):
#             high=mid-1
#         else:
#             low=mid+1 
#             ans=mid 
#     return ans
# n=9
# print(sqrootfloor(n))



























#sorting
#example stable sort  - bubble sort,insersion sort,merge sort
#example unstable sort - selection sort ,quick sort,heap sort
#it is the optimised solution≠≠
#bubble_sort - stable sort 
# def bubble_sort(l):
#     n = len(l)
#     for i in range(n-1):
#         swapped = False
#         for j in range(n-i-1):
#             if l[j]>l[j+1]:
#                 l[j],l[j+1]=l[j+1],l[j]
#                 swapped= True
#         if swapped==False:
#             return
            
#     return l
# print(bubble_sort([1,9,8,7,6,5,4,3,2]))



#selection sort - unstable sort

# def selection_sort(l):
#     n = len(l)
#     for i in range(n-1):
#         max_indx = i
#         for j in range(i+1,n):
#             if l[j]<l[max_indx]:
#                 max_indx=j
#         l[max_indx],l[i] = l[i], l[max_indx]
# a = [1,9,8,7,6,5,4,3,2]
# selection_sort(a)
# print(*a)# remove the list or square bracket only element


#inseration sort - stable sort

# def insertion_sort(l):
#     for i in range(1,len(l)):
#         x = l[i]
#         j = i-1
#         while j>=0 and x<l[j]:
#             l[j+1]=l[j]
#             j = j-1
#         l[j+1]=x
        

# a = [1,9,8,7,6,5,4,3,2]
# insertion_sort(a)
# print(*a)




#merg sort - stable sort

# def merge(left, right):
#     a = []
#     i, j = 0, 0

    # while i < len(left) and j < len(right):
    #     if left[i] <= right[j]:
    #         a.append(left[i])
    #         i += 1
    #     else:
    #         a.append(right[j])
    #         j += 1

    # a.extend(left[i:])
    # a.extend(right[j:])

    # return a

# a = [10, 15,20,45,56,67]
# b = [5, 6, 6, 30, 40,67]
# print(*merge(a,b))




# def merge(a, b):
    # a = []
    # m = len(a)
    # n = len(b)
    # i = j = 0
    # while i < m and j < n:
    #     if a[i] < b[j]:
    #         a.append(a[i])
    #         i += 1
    #     else:
    #         a.append(b[j])
    #         j += 1
    # while i < m:
    #     a.append(a[i])
    #     i += 1
    # while j < n:
    #     a.append(b[j])
    #     j += 1
    # return a
# a = [10, 15,20,45,56,67]
# b = [5, 6, 6, 30, 40,67]
# print(*merge(a, b))






# a = [1,2,3,4,5,6]
# for i in a:
#     a.remove(i)
# print(a)
"""
output will be =[2, 4, 6]
when the loop ittrate for first time list will be which has ben done for index 0 to remove element 1 [2,3,4,5,6]
then it will look for index 1 to remove 3 this will continue
"""


# def (a, low, mid, high):
    # left = a[low:mid + 1]
    # right = a[mid + 1:high + 1]
    # i = j = 0
    # k = low
    # while i < len(left) and j < len(right):
    #     if left[i] < right[j]:
    #         a[k] = left[i]
    #         k += 1
    #         i += 1
    #     else:
    #         a[k] = right[j]
    #         k += 1
    #         j += 1
    # while i < len(left):
    #     a[k] = left[i]
    #     i += 1
    #     k += 1
    # while j < len(right):
    #     a[k] = right[j]
    #     j += 1
    #     k += 1
# a = [10, 15, 20, 40, 8, 11, 55]
# merge(a, 0, 3, 6)
# print(*a)







#merge sort algoridim
# import time 
# a = time.time()
# def merge(a, low, mid, high):
#     left = a[low:mid + 1]
#     right = a[mid + 1:high + 1]
#     i = j = 0
#     k = low
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             a[k] = left[i]
#             k += 1
#             i += 1
#         else:
#             a[k] = right[j]
#             k += 1
#             j += 1
#     while i < len(left):
#         a[k] = left[i]
#         i += 1
#         k += 1
#     while j < len(right):
#         a[k] = right[j]
#         j += 1
#         k += 1

# def mergeSort(arr, l, r):
#     if r > l:
#         m = (r + l) // 2
#         mergeSort(arr, l, m)
#         mergeSort(arr, m + 1, r)
#         merge(arr, l, m, r)
# arr = [10, 5, 30, 15, 7]
# a = time.time()
# mergeSort(arr, 0, 4)
# b = time.time()
# c = a-b
# print(*arr)
# print(c)


 



#union of two sorted array
# def union_twosortedarrray(a,b):
    # i = 0
    # j = 0
    # while(i<len(a) and j<len(b)):
    #     if (i>0 and a[i]==a[i-1]):
    #         i+=1
    #     elif(j>0 and b[j]==b[j-1]):
    #         j+=1
    #     elif(a[i]<b[j]):
    #         print(b[i],end=" ")
    #         i+=1
    #     elif (a[i]>b[j]):
    #         print(b[j],end=" ")
    #         j+=1
    #     elif (a[i]==b[j]):
    #         print(a[i], end=" ")
    #         i+=1
    #         j+=1
    # while(i<len(a)):
    #     if (i>0 and a[i]!=a[i-1]):
    #         print(a[i],end=" ")
    #     i+=1
    # while (j<len(b)):
    #     if (j>0 and b[j]!=b[j-1]):
    #         print(b[j],end=" ")
    #     j+=1
    
# a = [1,2,3,4]
# b = [1,2,3]
# union_twosortedarrray(a,b)





#intersection of two sorted array
# def intersection_two_sortedlist(a,b):
#     i = j = 0
#     while (i<len(a) and j<len(b)):
#         if (i>0 and a[i]==a[i-1]):
#             i+=1
#             continue
#         elif(a[i]>b[j]):
#             j+=1
#         elif(a[i]<b[j]):
#             i+=1
#         else:
#             print(a[i],end = ' ')
#             i+=1
#             j+=1


# a = [1,2,3,4]
# b = [1,2,3]
# intersection_two_sortedlist(a,b)





#Count inversions in Array

# def count_inversion_array(lst):
    # c = 0
    # for i in range(len(lst)-1):
    #     for j in range(i+1,len(lst)):
    #         if lst[i]>lst[j]:
    #             c+=1
    # return c
# a= [2,4,1,3,5]
# print(count_inversion_array(a))





# Python 3 program to count inversions in an array

# def mergeSort(arr, n):
# 	temp_arr = [0]*n
# 	return _mergeSort(arr, temp_arr, 0, n-1)
# def _mergeSort(arr, temp_arr, left, right):
# 	inv_count = 0
# 	if left < right:
# 		mid = (left + right)//2
# 		inv_count += _mergeSort(arr, temp_arr,
# 								left, mid)
# 		inv_count += _mergeSort(arr, temp_arr,
# 								mid + 1, right)
# 		inv_count += merge(arr, temp_arr, left, mid, right)
# 	return inv_count
# def merge(arr, temp_arr, left, mid, right):
# 	i = left	 
# 	j = mid + 1 
# 	k = left	 
# 	inv_count = 0
# 	while i <= mid and j <= right:
# 		if arr[i] <= arr[j]:
# 			temp_arr[k] = arr[i]
# 			k += 1
# 			i += 1
# 		else:
# 			temp_arr[k] = arr[j]
# 			inv_count += (mid-i + 1)
# 			k += 1
# 			j += 1
# 	while i <= mid:
# 		temp_arr[k] = arr[i]
# 		k += 1
# 		i += 1
# 	while j <= right:
# 		temp_arr[k] = arr[j]
# 		k += 1
# 		j += 1
# 	for loop_var in range(left, right + 1):
# 		arr[loop_var] = temp_arr[loop_var]
# 	return inv_count
# arr = [1, 20, 6, 4, 5]
# n = len(arr)
# result = mergeSort(arr, n)
# print("Number of inversions are", result)







#partion of given array
# def partion_array(l,p):
#     left= []
#     right = []
#     for i in range(len(l)):
#         if l[i]<=l[p]:
#             left.append(l[i])
#         elif l[i]>l[p]:
#             right.append(l[i])
#     left.extend(right)
#     right.clear()
#     return left
            
# l = [3,8,6,12,10,7]
# p = 5
# print(partion_array(l,p))




#lomuto Partion

# def lomutoPartition(arr, l, h):
#     pivot = arr[h]
#     i = l - 1
#     for j in range(l, h):
#         if arr[j] <= pivot:
#             i+=1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[h] = arr[h], arr[i + 1]
#     return i + 1
# arr = [10, 80, 30, 90, 50, 70,40,100,20]
# lomutoPartition(arr, 0, len(arr)-1)
# print(*arr)

        


#hoarePartition
# def hoarePartition(arr,l,h):
#     pivot=arr[l]
#     i=l-1
#     j=h+l
#     while True:
#         i=i+1
#         while arr[i]<pivot:
#             i=i+1
#         j=j-1
#         while arr[j]>pivot:
#             j=j-1
#         if i>=j:
#             return j
#         arr[i],arr[j]=arr[j],arr[i]

# arr = [5,3,8,4,2,7,1,10]
# hoarePartition(arr, 0, len(arr)-1)
# print(*arr)


def lomutoPartition(arr, l, h):
    pivot = arr[h]
    i = l - 1
    for j in range(l, h):
        if arr[j] <= pivot:  # error
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[h] = arr[h], arr[i + 1]
    return i + 1

def qSort(arr, l, h):
    if l < h:
        p = lomutoPartition(arr, l, h)
        qSort(arr, l, p - 1)
        qSort(arr, p + 1, h)

arr = [8, 4, 7, 9, 3, 10, 5]
qSort(arr, 0, 6)
print(*arr)







# def check_rotation(a,b):
#     if len(a)!=len(b):
#         return False
#     temp =''
#     temp=a+b
#     return temp.find(b)!=-1

# a = 'prachi'
# b = 'ihcarp'

# print(check_rotation(a,b))






#palandrom

# def palandrom(a):
#     low = 0
#     high = len(a)-1
#     for i in range(len(a)):
#         if a[low]==a[high]:
            
#             low+=1
#             high+=1
#             return 'yes'
#         else:
#             return 'no'
# print(palandrom('dsabaak'))


#palandrom_easy methord
# def palandrom(a):
#     z = a[::-1]
#     return a==z
# print(palandrom('aba'))




# def check_subsequence(a,b):
#     i,j=0,0
#     while(i<len(a) and j<len(b)):
#         if a[i]==b[j]:
#             j+=1
#         i+=1
#     return j==len(b)
        
    
# print(check_subsequence('abc','bc'))
 

#recursive_way
# def check_subsquence_rec(s1,s2,n,m):
#     if n==0:
#         return True
#     if m==0:
#         return False
#     if s1[n-1]==s2[m-1]:
#         return check_subsquence_rec(s1,s2,n-1,m-1)
#     else:
#         return check_subsquence_rec(s1,s2,n-1,m)
# s1 = 'abba'
# s2 = 'aba'
# print(check_subsquence_rec(s1,s2,len(s1),len(s2)))





#anagram-sortcurt way
# s1= input("Enter a String:\n")
# s2= input("Enter a String:\n")

# def areAnagram(s1,s2):
#     if len(s1) != len(s2):
#         return False
#     s1=sorted(s1)
#     s2=sorted(s2)
#     return(s1==s2)

        
#efficent appraoch
# s1= input("Enter a String:\n")
# s2= input("Enter a String:\n")

# def areAnagram(s1,s2):
#     if len(s1) != len(s2):
#         return False
#     count=[0]*256
#     for i in range(len(s1)):
#         count[ord(s1[i])]+=1
#         count[ord(s2[i])]-=1
#     for x in count:
#         if x!=0:
#             return False
#     return True




#left_most_reapting charater in srting
# def left_most_reapting(n):
#     for i in range(len(n)):
#         for j in range(i+1,len(n)):
#             if n[i]==n[j]:
#                 return i
#     return -1

# print(left_most_reapting('ababcccaccs'))
            


#approach - 2
# CHAR = 256 
# def leftmost(st) :
#     count = [0] * CHAR 
#     for i in range(len(st)) :
#         count[ord(st[i])] += 1 
#     for i in range(len(st)) :
#         if count[ord(st[i])] > 1 :
#             return i 
#     return -1 

# st = "abccbd"  
# print(leftmost(st))






# def reverse_string(n):
#     z = n.split()[::-1]
#     a = ' '
#     for i in range(len(z)):
#         a=a+' '+z[i]
#     return a

# print(reverse_string('pritam is softwar devloper in google'))




#Subarray with given sum
# class Solution:
#     def subArraySum(self, arr, n, target_sum):
#         left, right = 0, 0
#         current_sum = 0
#         for right in range(n):
#             current_sum += arr[right]
#             while current_sum > target_sum and left < right:
#                 current_sum -= arr[left]
#                 left += 1
#             if current_sum == target_sum:
#                 return [left + 1, right + 1]
#         return [-1]
# a = Solution()
# b = [1,4,20,3,10,5]
# print(a.subArraySum(b,len(b),33))




#missing number in an array
# def missingNumber(arr,n):
    # n = len(arr) + 1  
    # expected_sum = n * (n + 1) // 2
    # actual_sum = sum(arr)
    # missing_number = expected_sum - actual_sum
#     return missing_number         
# print(missingNumber([1,2,3,4,5,6,8]))






# class Solution:
#     def sort012(self,arr,n):
#         # code here
#         l0 = []
#         l1 = []
#         l2 = []
        
#         for i in range(n):
#             if arr[i]==0:
#                 l0.append(arr[i])
#             elif arr[i]==1:
#                 l1.append(arr[i])
#             elif arr[i]==2:
#                 l2.append(arr[i])
#         return l0+l1+l2

# l = [0,2,1,2,0]
# a = Solution()
# print(a.sort012(l,len(l)))


# def missingPanagram(s):
#     a = 'abcdefghijklmnopqrstuvwxyz'
#     s = s.lower()
#     c = ''
#     z = a+s
#     if len(z)>1:
#         for i in range(len(z)):
#             if z.count(z[i])<2:
#                 c+=z[i]
#     if len(c)>=1:       
#         return c
#     else:
#         return -1
# s = 'eSrWSFMSACUBBHJaTgHItgtFBByBYxcXsinhIVTJLLXiAnLqNYcksdDhaenlhvKSxbXbESRlZnSFshOLBg'
# print(missingPanagram(s))




#efficent approah 
# class Solution:
#     def missingPanagram(self, s):
#         a = 'abcdefghijklmnopqrstuvwxyz'
#         s = s.lower()
#         char_set = set(s)
#         result = ''.join(char for char in a if char not in char_set)
#         if result:
#             return result
#         else:
#             return -1






#bracket_checker

# class Solution:
#     def ispar(self, x):
#         stack = []
#         top = None  # Initialize top to None

#         for i in range(len(x)):
#             if x[i] in '({[':
#                 stack.append(x[i])
#                 top = stack[-1]  # Update top when a new element is pushed onto the stack
#             elif x[i] in ')}]' and top is not None:
#                 if x[i] == ')' and top == '(':
#                     stack.pop()
#                     if len(stack) > 0:
#                         top = stack[-1]
#                     else:
#                         top = None
#                 elif x[i] == ']' and top == '[':
#                     stack.pop()
#                     if len(stack) > 0:
#                         top = stack[-1]
#                     else:
#                         top = None
#                 elif x[i] == '}' and top == '{':
#                     stack.pop()
#                     if len(stack) > 0:
#                         top = stack[-1]
#                     else:
#                         top = None
#                 else:
#                     return False
#             else:
#                 return False

#         return len(stack) == 0
    
# a = Solution()
# print(a.ispar('{({})}'))





# def canpair(arr,k):
#     c=0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if (arr[i]+arr[j])%k==0:
#                 c+=1
#     return c
# a =  [9, 5, 7, 3]
# print(canpair(a,6))





#linked_list

# class Node():
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# def printlist(head):
#     current =head
    # while current!=None:
    #     print(current.data,end = ' ')
    #     current = current.next

# head = Node(10)
# head.next = Node(20)
# head.next.next  = Node(30)
# head.next.next.next = Node(40)

# print("Linked List elements:")
# printlist(head)







#search in link list

# class Node():
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None

# def search(head,x):
#         current= head
#         c=1
#         while current!=None:
#             if current.data==x:
#                 return c
#             c+=1
            
#             current = current.next
#         return -1

# head = Node(10)
# head.next = Node(20)
# head.next.next  = Node(30)
# head.next.next.next = Node(40)
# x = 30
# print(search(head,x))





# Insert at first element

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# def insert(head, x):
#     new_node = Node(x)
#     new_node.next = head
#     head = new_node
#     return head

# def print_list(head):
#     current = head
#     while current:
#         print(current.data, end=" ")
#         current = current.next
#     print()

# head = None
# head = insert(head, 30)
# head = insert(head, 20)
# head = insert(head, 10)
# print_list(head)


#Insert at END 

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# def insert_end(head, x):
#     if head is None:
#         return Node(x)
#     current = head
#     while current.next is not None:
#         current = current.next
#     current.next = Node(x)
#     return head

# def printList(head):
#     curr = head
#     while curr is not None:
#         print(curr.data, end=" ")
#         curr = curr.next

# head = None
# head = insert_end(head, 10)
# head = insert_end(head, 20)
# head = insert_end(head, 30)
# printList(head)


#insert at specific position
# class Node:
#     def __init__(self, k):
#         self.key = k
#         self.next = None

# def insertPos(head,data,pos):
#     temp = Node(data)
#     if pos ==1:
#         temp.next = head
#         return temp
#     curr = head

#     for i in range(pos-2):
#         curr = curr.next
#         if curr == None:
#             return head

#     temp.next = curr.next
#     curr.next = temp
#     return head

# def printList(head):
#     curr = head
#     while curr != None:
#         print(curr.key, end=" ")
#         curr = curr.next
#     print()

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# head.next.next.next.next = Node(50)
# printList(head)
# head = insertPos(head,45,4)
# printList(head)






#delete at begining

# class Node():
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None

# def del_head(head):
#     if head==None:
#         return None
#     return head.next

# def printList(head):
#     curr = head
#     while curr != None:
#         print(curr.data, end=" ")
#         curr = curr.next
#     print()

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# print('before deletion of head')
# printList(head)
# head = del_head(head)
# print('after deletion of head')
# printList(head)




#Delete at END 

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

# def del_end(head):
#     if head == None:
#         return  None
#     if head.next == None:
#         return None
#     curr = head

#     while curr.next.next != None:
#         curr = curr.next
#     curr.next = None
#     return head

# def printList(head):
#     curr = head
#     while curr is not None:
#         print(curr.data, end=" ")
#         curr = curr.next

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)
# printList(head)
# head = del_end(head)
# printList(head)


#Delete a node with pointer give to it
# class Node:
#     def __init__(self, k):
#         self.data = k
#         self.next = None

# def printList(head):
#     curr = head
#     while curr != None:
#         print(curr.data, end=" ")
#         curr = curr.next
#     print()

# def deleteNode(ptr):
#     temp = ptr.next
#     ptr.data = temp.data
#     ptr.next = temp.next

# head = Node(10)
# head.next = Node(10)
# head.next.next = Node(90)
# head.next.next.next = Node(20)
# printList(head)
# deleteNode(head)
# printList(head)



#insert a element in a Sorted Insert Linked List in Python
# class Node:
#     def __init__(self, k):
#         self.data = k
#         self.next = None

# def insert_element(head,x):
#     temp = Node(x)
#     if head==None:
#         return head
#     elif x<head.data:
#         temp.next = head
#         return temp
#     else:
#         curr = head
#         while curr.head !=None and curr.next.data<x:
#             curr=curr.next
#         temp.next = curr.next
#         curr.next = temp
#         return head

# head = Node(10)
# head.next = Node(20)
# head.next.next = Node(30)
# head.next.next.next = Node(40)

# h = head
# while h != None:
#     print(h.key)
#     h = h.next

# print()

# h = insert_element(head, 35)

# h = head
# while h != None:
#     print(h.key)
#     h = h.next











# class Solution:
#     def longSubarrWthSumDivByK(self, arr, n, k):
#         # Create a dictionary to store the remainder and its index
#         rem_dict = {}
        
#         # Initialize variables for tracking the sum and the maximum subarray length
#         curr_sum = 0
#         max_len = 0
        
#         for i in range(n):
#             # Calculate the cumulative sum
#             curr_sum += arr[i]
            
#             # Calculate the remainder when divided by K
#             rem = curr_sum % k
            
#             # If remainder is negative, convert it to a positive remainder
#             if rem < 0:
#                 rem += k
            
#             # If remainder is 0, update max_len to include the current index
#             if rem == 0:
#                 max_len = i + 1
            
#             # If remainder is in the dictionary, update max_len based on the stored index
#             elif rem in rem_dict:
#                 max_len = max(max_len, i - rem_dict[rem])
            
#             # If remainder is not in the dictionary, store the index
#             else:
#                 rem_dict[rem] = i
        

#         return max_len




# a = [1,2,3,4,5,6,7,8,9,10]

# for i in a :
#     a.remove(i)
# print(a)







# class Solution:
#     #Function to count the frequency of all elements from 1 to N in the array.
#     def frequencyCount(self, arr, N, P):
#         # code here
#         l = []
#         for i in range(1,P+1):
#             l.append(arr.count(i))
#         return l
# a= Solution()
# print(a.frequencyCount([2,3,2,3,5],5,5))


def fg(x,l=[]):
    for i in range(x):
        l.append(i*i)
    return l
print(fg(3,[3,2,1]))










# class Solution:
#     def rearrange(self, arr, n):
#         # Separate positive and negative numbers
#         p = [arr[i] for i in range(len(arr)) if arr[i] >= 0]
#         neg = [arr[i] for i in range(len(arr)) if arr[i] < 0]

#         # Initialize pointers and result list
#         pos_index, neg_index = 0, 0
#         k = []

#         # Iterate over the total number of elements
#         for i in range(n):
#             if i % 2 == 0 and pos_index < len(p):
#                 k.append(p[pos_index])
#                 pos_index += 1
#             elif neg_index < len(neg):
#                 k.append(neg[neg_index])
#                 neg_index += 1
#             elif pos_index < len(p):
#                 k.append(p[pos_index])
#                 pos_index += 1

#         return k
    
# a = Solution()
# print(a.rearrange([9, 4, -2, -1, 5, 0, -5, -3, 2],9))



a=bin(12)[2:]
for i in range(len(a)-1,-1,-1):
    print(i)





