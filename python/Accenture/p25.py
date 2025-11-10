# Intersection of Two Arrays – Given two arrays, print their intersection (common elements without duplicates).
# Description: Find distinct common elements. E.g. [1,2,2,3] ∩ [2,3,4] = [2,3].
# Sample I/O:
# Input: A=[89,24,75,11,23], B=[23,75,89,11] → Output: [11,23,75,89] (sorted intersection).
# Topic: Sets / Arrays. Difficulty: Easy. (Standard problem)


class Solution:
    def intersection(self,a,b):
        seen=set()
        res=[]
        for i in range(len(a)):
            seen.add(a[i])
        for j in range(len(b)):
            if b[j] in seen:
                res.append(b[j])
            seen.add(b[j])
        return res


a = Solution()

print(a.intersection([89,24,75,11,23], [23,75,89,11]))   # [11, 23, 75, 89]
print(a.intersection([1,2,2,3], [2,3,4]))                # [2, 3]
print(a.intersection([1,1,1], [1,2,3]))                  # [1]
print(a.intersection([], [1,2,3]))                       # []
print(a.intersection([1,2,3], []))                       # []

