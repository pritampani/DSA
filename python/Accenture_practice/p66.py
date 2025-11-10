#Group anagrams
from collections import defaultdict as dd
class Solution:
    def group_anagram(self,arr):
        res=dd(list)
        for i in arr:
            count=[0]*26
            for j in i:
                count[ord(j)-ord('a')]+=1
            res[tuple(count)].append(i)
        return list(res.values())


a = Solution()

print(a.group_anagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(a.group_anagram([""]))
print(a.group_anagram(["a"]))
print(a.group_anagram(["abc", "bca", "cab", "xyz", "zyx"]))
print(a.group_anagram(["listen", "silent", "enlist", "google", "gooegl"]))
print(a.group_anagram(["rat", "tar", "art", "car"]))


