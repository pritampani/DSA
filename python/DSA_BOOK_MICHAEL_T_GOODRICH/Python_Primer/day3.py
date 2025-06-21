class Solution:
    def checkoutofbound(self,arr,ele,idx):
        if idx>=len(arr):
            return 'Dont Try buffer overflow attack in python'
        
        for i in range(idx, len(arr)):
            if arr[i] == ele:
                return i
        
        return 'Element not found from given index'


s = Solution()
print(s.checkoutofbound([1,2,3,4,5], 4, 2))  # Output: 3
print(s.checkoutofbound([1,2,3,4,5], 6, 2))  # Output: 'Element not found from given index'
print(s.checkoutofbound([1,2,3], 2, 5))      # Output: 'Index out of bounds'