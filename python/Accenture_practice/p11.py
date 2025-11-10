#Right-angled triangle pattern
# *
# **
# ***
# ****
# *****
# ******


class Solution:
    def right_angle_triangle(self,n):
        for i in range(1,n):
            print(i*'*')
a=Solution()
print(a.right_angle_triangle(7))
