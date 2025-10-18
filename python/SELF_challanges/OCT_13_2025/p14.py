#Given two strings, check if one is a permutation / anagram of the other.


class Solution:
    def p14_anagram(self,s1,s2):
        s1 = s1.replace(" ", "").lower()
        s2 = s2.replace(" ", "").lower()

        if len(s1)!=len(s2):
            return False
        d1=dict()

    
        for i in s1:
            d1[i]=d1.get(i,0)+1
        for j in s2:
            if j not in d1:
                return False
            d1[j]-=1
            if d1[j]<0:
                return False
        for k in d1:
            if d1[k]!=0:
                return False
        return True

a=Solution()
print(a.p14_anagram("listen", "silent"))  # ✅ True
print(a.p14_anagram("triangle", "integral"))  # ✅ True
print(a.p14_anagram("rat", "car"))  # ❌ False
print(a.p14_anagram("dusty", "study"))  # ✅ True
print(a.p14_anagram("SchoolMASTER", "TheClassROOM"))  # ✅ True
print(a.p14_anagram("a gentleman", "elegant man"))  # ✅ True
print(a.p14_anagram("python", "java"))  # ❌ False
print(a.p14_anagram("abcd", "abcde"))  # ❌ False
print(a.p14_anagram("@#!!", "!!#@"))  # ✅ True
print(a.p14_anagram("112233", "332211"))  # ✅ True
