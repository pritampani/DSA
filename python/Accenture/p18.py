#Find Element Occurring Odd Number of Times

class Solution:
    def find_ele(self,arr):
        res=0
        for i in arr:
            res^=i
        return res


a = Solution()

print(a.find_odd_occurrence([1, 2, 3, 2, 3, 1, 3]))   # Expected: 3
print(a.find_odd_occurrence([5, 7, 5, 7, 5]))         # Expected: 5
print(a.find_odd_occurrence([10, 10, 20]))            # Expected: 20
print(a.find_odd_occurrence([4]))                     # Expected: 4
print(a.find_odd_occurrence([1,1,2,2,3,3,4]))        # Expected: 4