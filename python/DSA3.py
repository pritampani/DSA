#longest common prefix
# class Solution(object):
#     def longestCommonPrefix(self, strs):
#         if not strs:
#             return " "
#         # Sort the strings to find the common prefix
#         strs.sort()
#         # Take the first and last strings after sorting
#         first_str, last_str = strs[0], strs[-1]
#         common_prefix = []
#         # Compare characters of the first and last strings
#         for i in range(len(first_str)):
#             if i < len(last_str) and first_str[i] == last_str[i]:
#                 common_prefix.append(first_str[i])
#             else:
#                 break
#         return "".join(common_prefix)




#find the Median of two  Sorted Arrays

# class Solution(object):
#     def findMedianSortedArrays(self, nums1, nums2):
#         # Merge the two sorted arrays
#         x = []
#         i, j = 0, 0
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] < nums2[j]:
#                 x.append(nums1[i])
#                 i += 1
#             else:
#                 x.append(nums2[j])
#                 j += 1
#         x.extend(nums1[i:])
#         x.extend(nums2[j:])
#         n = len(x)
#         if n % 2 == 0:
#             median_value = (x[n // 2 - 1] + x[n // 2]) / 2.0
#         else:
#             median_value = x[n // 2]
#         return median_value




#remove element from list


# def removeElement(nums, val):
#     i = 0  
#     for j in range(len(nums)):
#         if nums[j] != val:
#             nums[i] = nums[j]
#             i += 1
#     return i

# print(removeElement([1,2,3,4,5,5,6,6,6,6],6))


# def strStr(haystack, needle):
#     if not needle:
#         return 0
#     for i in range(len(haystack) - len(needle) + 1):
#         if haystack[i:i+len(needle)] == needle:
#             return i
#     return -1

# print(strStr("butsad",'sad'))




# Search Insert Position

# def searchInsert( nums, target):
#     pos = 0
#     for i in range(len(nums)):
#         if nums[i] >= target:
#             pos = i
#             break
#         pos = i + 1
#     return pos

# print(searchInsert([1,2,3,3,4,5],3))


# class Solution:
#     def removeKdigits(self, S, K):
#         stack = []
#         for i in S:
#             while K > 0 and stack and stack[-1] > i:
#                 stack.pop()
#                 K -= 1
#             stack.append(i)
#         while K > 0:
#             stack.pop()
#             K -= 1
#         result = ''.join(stack).lstrip('0')
#         return result if result else '0'

# a = Solution()
# print(a.removeKdigits('725083',5))






# a = 'abbcc'
# dic={}
# for num in a:
#     dic[num] = dic.get(num, 0) + 1







# def prime(n):
#     if n<2:
#         return False
#     if n in (2,3):
#         return True
#     if n%2==0 or n%3==0:
#         return False
#     for i in range(4,n+1):
#         if n%i==0:
#             return False
#         else:
#             return True

    

# n=int(input())
# print(prime(n))


# def fun(n):
#     x=1
#     if(n==1):
#         return x
#     for k in range(1,n):
#         x=x+fun(k)*fun(n-k)
    
#     return x

# print(fun(5))





# def find4Numbers( A, n, X):
#     # return true or false
#     for i in range(n-3):
#         if sum(A[i:i+4])==X:
#             return A[i:i+4]
#         else:
#             return 0

# print(find4Numbers([1, 4, 2, 6, 3, 8, 5, 9],8,20))






# class Solution:
#     def checkTriplet(self, arr):
#         if len(arr) < 3:
#             return 'NO'
#         k = [x * x for x in arr]
#         for i in range(len(k)-1):
#             s = k[i] + k[i+1] 
#             if s in k:
#                 return 'Yes'
#         return 'No'


# a = Solution()
# print(a.checkTriplet([3 ,8, 5]))



# class Solution:

#     def checkTriplet(self,arr):
#         # code here
#         square_dict={i*i: i for i in arr}
#         for sq1 in square_dict:
#             for sq2 in square_dict:
#                 if sq1+sq2 in square_dict:
#                     return "Yes"
#         return False

# a = Solution()
# print(a.checkTriplet([3 ,8, 5]))



# class Solution:
    
#     #Function to find length of longest increasing subsequence.
#     def longestSubsequence(self,a):
#         # code here
#         ml = 0

#         for i in range(len(a)):
#             for j in range(i+1,len(a)):
#                 if self.issorted(a[i:j]) and len(a[i:j])>ml:
#                     ml=len(a[i:j])
#                     continue
#         return ml
#     def issorted(self,a):
#         b= a
#         return sorted(a)==b

# a = Solution()
# print(a.longestSubsequence([0, 8, 4, 12, 2, 10 ,6, 14, 1, 9, 5 ,13, 3, 11, 7, 15]))






# class Solution:
#     def firstElementKTime(self, k, a):
#         # code here
#         uni=[]
#         dul=[]
#         for i in range(len(a)):
#             if a[i] not in uni:
#                 uni.append(a[i])
#             elif a[i] in uni:
#                 dul.append(a[i])
#         if len(dul)==0 or a.count(dul[0])<k:
#             return -1
#         return dul[0]

# a = Solution()
# print(a.firstElementKTime(2,[1, 7, 4 ,3 ,4 ,8, 7]))



# class Solution:
#     ##Complete this function
#     #Function to rearrange the array elements alternately.
#     def rearrange(self,arr): 
#         ##Your code here
#         i = 0
#         j = len(arr) - 1
#         temp=[0]*len(arr)
#         while i <= j:
#             for k in range(len(arr)):
#                 if k % 2 != 0:
#                     temp[k] = arr[i]
#                     i += 1
#                 else:
#                     temp[k] = arr[j]
#                     j -= 1
#         for i in range(len(arr)):
#             arr[i]=temp[i]
#         return arr

# arr = [1, 2, 3, 4, 5, 6]
# a = Solution()
# print(a.rearrange(arr))





# class Solution:
#     def allPairs(self, A, B, X):
#         # Your code goes here 
#         a = []
#         for i in range(len(A)):
#             for j in range(len(B)):
#                 if A[i]+B[j]==X:
#                     a.append((A[i],B[j]))
#         if len(a)==0:
#             return [()]
#         return a


# a = Solution()
# print(a.allPairs([1, 2, 4, 5, 7],[5, 6, 3, 4, 8],9))





# mat = [[1, 1, 1, 1],
#        [2, 2, 2, 2],
#        [3, 3, 3, 3],
#        [4, 4, 4, 4]]

# for i in range(len(mat)):
#     for j in range(len(mat)):
#         print(mat[j][i],end=' ')
#     print()





# class Solution:
#     def majorityElement(self, nums) -> int:
#         count_dict = {}
#         max=0
#         ele = 0
#         for num in nums:
#             count_dict[num] = count_dict.get(num, 0) + 1
#         for i in count_dict:
#             if count_dict[i]>max:
#                 max=count_dict[i]
#                 ele=i
#         return ele


# a = Solution()
# print(a.majorityElement([3,3,4]))



# class Solution:
#     def nextLargerElement(self, arr, n):
#         result = [-1] * n 
#         stack = []  
        
#         for i in range(n):
#             while stack and arr[i] > arr[stack[-1]]: 
#                 idx = stack.pop()  
#                 result[idx] = arr[i] 
#             stack.append(i)  
#         return result
# a = Solution()
# print(a.nextLargerElement([13,7,6,12,10],5))




# class Solution:
#     #Function to find sum of all possible substrings of the given string.
#     def sumSubstrings(self,s):
        
#         # code here
#         result=[]
#         i=0
#         j = len(s)-1
#         while i<=j:
#             k = s[i:j]
#             result.append(int(k))
#             i+=1
#             j-=1
#         return result
# a = Solution()
# print(a.sumSubstrings('421'))


# class Solution:
#     def leftRotate(self, arr,  d):
#         # code here
#         for i in range(d):
#             k = arr.remove(arr[i])
#             arr.append(k)
#         return arr

# a=Solution()
# print(a.leftRotate([1, 2, 3, 4, 5, 6, 7],2))




# class Solution:
#     def lenOfLongSubarr (self, arr, n, k) : 
#         #Complete the function
#         o = 0
#         for i in range(len(arr)):
#             for j in range(len(arr),i,-1):
#                 if sum(arr[i:j])==k and len(arr[i:j])>o:
#                     o=len(arr[i:j])
#         return o


                    

# a = [56, 67, 30, 79]

# print(sum(a)//len(a))



# def fo(a,b):
#     c = 0
#     a.sort()
#     b.sort()
#     for i in range(len(a)):
#         for j in range(i,len(b)):
#             if a[i]>b[j]:
#                 c+=1
#     return c

# print(fo([1,2,3,4,5],[6,6,1,1,1]))



# class Solution:
    
#     #Function to check whether there is a subarray present with 0-sum or not.
#     def subArrayExists(self,arr):
#         ##Your code here
#         #Return true or false
#         i = 0
#         j = len(arr)-1
        
#         while i<=j:
#             if sum(arr[i:j])==0:
#                 return True
#             else:
#                 i+=1
#                 j-=1
#                 continue 
            
#         return False
    
# a= Solution()

# print(a.subArrayExists([-9, -6, 7, -8, -2, 10, 9, -1]))





# class Solution:
    
#     #Function to check if two strings are isomorphic.
#     def areIsomorphic(self,str1,str2):
#         a = set(str1)
#         b= set(str2)
#         count_dict1={}
#         count_dict2={}
#         if len(a)==len(b):
#             for num in str1:
#                 count_dict1[num] = count_dict1.get(num, 0) + 1
#             for num in str2:
#                 count_dict2[num] = count_dict2.get(num, 0) + 1
            
#             for i in count_dict1:
#                 for j in count_dict2:
#                     if count_dict1[i]==count_dict2[j]:
#                         continue
#                     else:
#                         False
#         else:
#             return False
#         return True
        
# a = Solution()

# print(a.areIsomorphic('aba','xxy'))






































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































