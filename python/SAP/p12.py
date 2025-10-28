#Inverted triangle pattern



class Solution:
    def inv_right_angle(self,n):
        for i in range(n-1,-1,-1):
            print("*"*i)


a=Solution()
print(a.inv_right_angle(7))
