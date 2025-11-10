#Longest consecutive sequence
# arr = [100, 4,4, 200, 1, 3, 2]



class Solution:
    def consutive_solution(self,arr):
        a=set(arr)
        longest=0
        for i in a:
            if i-1 not in a:
                curr=i
                l=1
                while curr+1 in a:
                    curr+=1
                    l+=1
                longest=max(longest,l)
        return longest


a = Solution()
print(a.consutive_solution([100, 4,4, 200, 1, 3, 2,5]))