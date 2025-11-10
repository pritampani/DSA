#Evaluate postfix expression


class Solution:
    def evulate_postfix(self,arr):
        stk=[]
        for i in arr:
            if i.isdigit():
                stk.append(int(i))
            else:
                a=stk.pop()
                b=stk.pop()
                if i=='+':
                    stk.append(b+a)
                elif i=='-':
                    stk.append(b-a)
                elif i=='*':
                    stk.append(b*a)
                elif i=='/':
                    stk.append(b/a)
                elif i=='^':
                    stk.append(b**a)
        return stk[-1]

a = Solution()
print(a.evulate_postfix(["2", "3", "1", "*", "+", "9", "-"]))  # 2 + 3*1 - 9 = -4
print(a.evulate_postfix(["4", "13", "5", "/", "+"]))            # 4 + (13/5) = 6
print(a.evulate_postfix(["5", "6", "2", "+", "*"]))             # 5*(6+2) = 40
print(a.evulate_postfix(["2", "3", "+", "4", "*"]))             # (2+3)*4 = 20
print(a.evulate_postfix(["10", "2", "8", "*", "+", "3", "-"]))  # 10+2*8-3 = 23
                