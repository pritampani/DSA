#Sort Array of 0s, 1s, and 2s


class Solution:
    def sort012(self,arr):

        l=0
        m=0
        h=len(arr)-1
        while m<=h:
            if arr[m]==0:
                arr[l],arr[m]=arr[m],arr[l]
                l+=1
                m+=1
            elif arr[m]==2:
                arr[m],arr[h]=arr[h],arr[m]
                h-=1
            else:
                m+=1
        return arr

s = Solution()
print(s.sort012([0, 2, 1, 2, 0]))  # Output: [0, 0, 1, 2, 2]
print(s.sort012([2, 2, 1, 0]))      # [0, 1, 2, 2]
print(s.sort012([1, 1, 1]))          # [1, 1, 1]
print(s.sort012([0]))                # [0]
