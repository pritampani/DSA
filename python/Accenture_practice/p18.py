#Count vowels and consonants

class Solution:
    def count_vowl_const(self,ans):
        vowl=0
        conant=0
        for i in range(len(ans)):
            if ans[i] in {'a','e','i','o','u'}:
                vowl+=1
            else:
                conant+=1
        return vowl,conant


a=Solution()

print(a.count_vowl_const('aeiouqwrt'))


