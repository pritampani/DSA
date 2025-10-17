#. Given a string representing a nested structure like "[1,2,[3,4],5]", parse it into a nested list / array.
class Solution:
    def p7(self, s: str):
        stack = []
        num = ''
        for c in s:
            if c == '[':
                stack.append([])
            elif c.isdigit():
                num += c
            elif c == ',':
                if num:
                    stack[-1].append(int(num))
                    num = ''
            elif c == ']':
                if num:
                    stack[-1].append(int(num))
                    num = ''
                last = stack.pop()
                if stack:
                    stack[-1].append(last)
                else:
                    return last
        return []

