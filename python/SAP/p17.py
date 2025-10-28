#Check if string is palindrome


class Solution:
    def check_palandrinom(self,ans):
        return ans==ans[::-1]

a=Solution()
print(a.check_palandrinom('ippi'))
print(a.check_palandrinom('ipp'))



