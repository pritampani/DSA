# prefix evulation


class Solution:
    def prefix_eva(self,arr):
        stk=[]
        for i in arr[::-1]:
            if i.isdigit():
                stk.append(int(i))
            else:
                a=stk.pop()
                b=stk.pop()
                if i=='+':
                    stk.append(a+b)
                elif i=='-':
                    stk.append(a-b)
                elif i=='*':
                    stk.append(a*b)
                elif i=='/':
                    stk.append(a/b)
                elif i=='^':
                    stk.append(a**b)
        return stk[-1]
    


a = Solution()
print(a.prefix_eva(["+", "9", "*", "2", "6"]))        # 9 + 2*6 = 21
print(a.prefix_eva(["-", "*", "2", "3", "4"]))        # (2*3) - 4 = 2
print(a.prefix_eva(["+", "*", "5", "6", "7"]))        # (5*6) + 7 = 37
print(a.prefix_eva(["*", "+", "2", "3", "+", "4", "5"]))  # (2+3)*(4+5) = 45
print(a.prefix_eva(["-", "+", "10", "5", "2"]))       # (10+5)-2 = 13