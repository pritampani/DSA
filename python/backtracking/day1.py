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







        

        