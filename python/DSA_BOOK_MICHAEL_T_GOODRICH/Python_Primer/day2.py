#1.11

# class Solution:
#     def listcompresion(self,n):
#         arr=[2**i for i in range(n)]
#         return arr
# a=Solution()
# print(a.listcompresion(9))


#1.14]

# class Solution:
#     def checkdistinct(self,arr):
#         if len(arr)==0:
#             return set()
#         seen=set()
#         for i in range(len(arr)):
#             for j in range(len(arr)):
#                 if (arr[i]*arr[j])%2!=0 and (arr[i],arr[j]) not in seen:
#                     seen.add((arr[i],arr[j]))
#         return seen
# a=Solution()
# print(a.checkdistinct([1,2,3,4,5,6,7,7,8,9]))



#1.15
class Solution:
    def checkforelemntrepetations(self,arr):
        if len(arr)==0:
            return 'no elemnet is in the array'
        seen=set()
        for i in range(len(arr)):
            if arr[i] not in seen:
                seen.add(arr[i])
            else:
                return 'element is repeted'
        return 'no element is repeting'
a=Solution()

print(a.checkforelemntrepetations([1,2,3,4,5,6,7]))
print(a.checkforelemntrepetations([1,2,3,4,5,6,6,7]))
print(a.checkforelemntrepetations([]))






















































































