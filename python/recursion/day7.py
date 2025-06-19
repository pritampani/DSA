#find all the subset of from the array(using loop)
# class Solution:
#     def subset(self, arr):
#         res = [[]]  
#         for num in arr:
#             new_subsets = []
#             for subset in res:
#                 new_subsets.append(subset + [num])
#             res.extend(new_subsets)  
#         return res
# a=Solution()
# print(a.subset([1,2,3]))    


#find all the subset of from the array(using recursive approach)

class Solution:
    def subset(self, arr):
        res = []
        self.helper(arr, 0, [], res)
        return res

    def helper(self, arr, index, current, res):
        if index == len(arr):
            res.append(current[:])  # Append a copy of current subset
            return
        # Include the current element
        current.append(arr[index])
        self.helper(arr, index + 1, current, res)
        # Exclude the current element
        current.pop()
        self.helper(arr, index + 1, current, res)

a = Solution()
print(a.subset([1, 2, 3]))
