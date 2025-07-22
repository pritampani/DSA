# class Solution:
#     def rowWithMax1s(self, arr):
#         # code here
#         maxi=0
#         for i in range(len(arr)):
#             c=0
#             for j in range(len(arr[0])-1,-1,-1):
#                 if arr[i][j]==1:
#                     c+=1
#             maxi=max(maxi,c)
#         return maxi


# a=Solution()
# arr=[[0,1,1,1], 
#  [0,0,1,1], 
#  [1,1,1,1],
#  [0,0,0,0]]
# print(a.rowWithMax1s(arr))




# find a zero where up,left,down,right==1 and return the index the the zero

# arr=[[0,1,0,0], 
#      [1,0,1,0], 
#      [0,1,0,0],
#      [0,0,0,0]]





#find the path from the matrix to reach from the source to destnation the path have only 1

# arr=[[1,-1,-1,-1], 
#      [2,1,4,6], 
#      [5,1,1,1],
#      [23,23,45,1]]




