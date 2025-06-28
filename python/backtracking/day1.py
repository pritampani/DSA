# class Solution:
#     def subsets(self,arr):
#         i=0
#         currarr=[]
#         res=[]
#         self.helper(arr,i,currarr,res)
#         return res

        
#     def helper(self,arr,i,currarr,res):
#         if i>=len(arr):
#             res.append(currarr[:])
#             return


#         #consider the element
#         currarr.append(arr[i])
#         self.helper(arr,i+1,currarr,res)


#         #not consider
#         currarr.pop()
#         self.helper(arr,i+1,currarr,res)


# a=Solution()
# print(a.subsets([1,2,3]))



class Solution:
    def issorted(self,arr):
        if len(arr)==0 or len(arr)==1:
            return True
        i=0
        return self.helper(arr,i)
    def helper(self,arr,i):
        if i==len(arr)-1:
            return True
        if arr[i]<=arr[i+1]:
            return self.helper(arr,i+1)
        return False
a=Solution()
print(a.issorted([1,2,3,4,5]))
print(a.issorted([3,1,2]))



        

        