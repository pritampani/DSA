	# 	Merge Intervals

	# •	Example: [[1,3],[2,6],[8,10],[15,18]] → [[1,6],[8,10],[15,18]]


class Solution:
    def merge_interval(self,arr):
        arr.sort(key=lambda x:x[0])
        res=[]
        res.append(arr[0])
        for start,end in arr[1:]:
            lastend=res[-1][1]
            if start<=lastend:
                res[-1][1]=max(lastend,end)
            else:
                res.append([start,end])
        return res


a = Solution()
print(a.merge_interval([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
print(a.merge_interval([[1,4],[4,5]]))                 # [[1,5]]
print(a.merge_interval([[1,10],[2,3],[4,8]]))          # [[1,10]]
print(a.merge_interval([[6,8],[1,9],[2,4],[4,7]]))     # [[1,9]]
print(a.merge_interval([[1,2]]))                       # [[1,2]]