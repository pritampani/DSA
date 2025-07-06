# Next greater Element 

# class Solution:
#     def nextgreaterelement(self,arr):
#         stk=[]
#         ans=[]
#         for i in range(len(arr)-1,-1,-1):
#             while stk and stk[-1]<=arr[i]:
#                 stk.pop()
#             if not stk:
#                 ans.append(-1)
#             else:
#                 ans.append(stk[-1])
#             stk.append(arr[i])

#         return ans[::-1]
# a=Solution()
# print(a.nextgreaterelement([5,3,6,4,2,3,9,10]))
# print(a.nextgreaterelement([1,2,3,4,5,6,7,8,9]))
# print(a.nextgreaterelement([10,9,8,7,6,5,4,3,2,1]))
        






# Next smaller element

# class Solution:
#     def nextsmallerelement(self,arr):
        # stk=[]
        # ans=[]
        # for i in range(len(arr)-1,-1,-1):
        #     while stk and stk[-1]>=arr[i]:
        #         stk.pop()
        #     if not stk:
        #         ans.append(-1)
        #     else:
        #         ans.append(stk[-1])
        #     stk.append(arr[i])

        # return ans[::-1]
# a=Solution()
# print(a.nextsmallerelement([5,3,6,4,2,3,9,10]))
# print(a.nextsmallerelement([1,2,3,4,5,6,7,8,9]))
# print(a.nextsmallerelement([10,9,8,7,6,5,4,3,2,1]))





#previous greter element

# class Solution:
    # def previoussmallerelement(self,arr):
    #     stk=[]
    #     ans=[]
    #     for i in range(len(arr)):
    #         while stk and stk[-1]>=arr[i]:
    #             stk.pop()
    #         if not stk:
    #             ans.append(-1)
    #         else:
    #             ans.append(stk[-1])
    #         stk.append(arr[i])

    #     return ans
# a=Solution()
# print(a.previoussmallerelement([5,3,6,4,2,3,9,10]))
# print(a.previoussmallerelement([1,2,3,4,5,6,7,8,9]))
# print(a.previoussmallerelement([10,9,8,7,6,5,4,3,2,1]))





#previougreaterelement
# class Solution:
#     def previougreaterelement(self,arr):
#         stk=[]
#         ans=[]
#         for i in range(len(arr)):
#             while stk and stk[-1]<=arr[i]:
#                 stk.pop()
#             if not stk:
#                 ans.append(-1)
#             else:
#                 ans.append(stk[-1])
#             stk.append(arr[i])

#         return ans
# a=Solution()
# print(a.previougreaterelement([5,3,6,4,2,3,9,10]))
# print(a.previougreaterelement([1,2,3,4,5,6,7,8,9]))
# print(a.previougreaterelement([10,9,8,7,6,5,4,3,2,1]))





# Max histogram area

class Solution:
    def next_smaller_elemnt(self,arr):
        stk=[]
        ans=[]
        for i in range(len(arr)-1,-1,-1):
            while stk and arr[stk[-1]]>=arr[i]:
                stk.pop()
            if not stk:
                ans.append(len(arr))
            else:
                ans.append(stk[-1])
            stk.append(i)

        return ans[::-1]
    def previoussmallerelement(self,arr):
        stk=[]
        ans=[]
        for i in range(len(arr)):
            while stk and arr[stk[-1]]>=arr[i]:
                stk.pop()
            if not stk:
                ans.append(-1)
            else:
                ans.append(stk[-1])
            stk.append(i)

        return ans
    def Max_histogram_area(self,arr):

        a=self.next_smaller_elemnt(arr)
        b=self.previoussmallerelement(arr)
        maxi=0
        for i in range(len(arr)):
            width=(a[i]-b[i])-1
            maxi=max(maxi,width*arr[i])
        return maxi

a=Solution()
print(a.Max_histogram_area([6,2,5,4,5,1,6]))

