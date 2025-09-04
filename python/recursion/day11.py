# #print all subsequence using resursion

# class Solution:
#     def prinntallsubsequence(self,s):
#         curr=[]
#         res=[]
#         self.helper(s,0,curr,res)
#         return res
#     def helper(self,s,i,curr,res):

#         if i==len(s):
#             res.append(''.join(curr[:]))
#             return
        
#         curr.append(s[i])
#         self.helper(s,i+1,curr,res)
        
#         curr.pop()
#         self.helper(s,i+1,curr,res)
# #main
# a=Solution()
# print(a.prinntallsubsequence('312'))



class Solution:
    def prinntallsubsequence(self, s):
        curr = []
        res = []
        print(f"Starting recursion for string: {s}\n")
        self.helper(s, 0, curr, res)
        return res

    def helper(self, s, i, curr, res):
        # Base case
        if i == len(s):
            print(f"Reached end with subsequence: {''.join(curr)}")
            res.append(''.join(curr[:]))
            return

        # Include current character
        curr.append(s[i])
        print(f"Include '{s[i]}' → Current: {''.join(curr)} (i={i})")
        self.helper(s, i+1, curr, res)

        # Backtrack: remove the character
        curr.pop()
        print(f"Backtrack after including '{s[i]}' → Current: {''.join(curr)} (i={i})")

        # Exclude current character
        print(f"Exclude '{s[i]}' → Current: {''.join(curr)} (i={i})")
        self.helper(s, i+1, curr, res)


# main
a = Solution()
ans = a.prinntallsubsequence("312")
print("\nAll Subsequences:", ans)


