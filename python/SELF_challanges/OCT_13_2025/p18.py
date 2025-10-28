
"""
Given an integer n, the task is to generate all binary strings of size n without consecutive 1's.

Examples: 

Input : n = 4
Output : 0000 0001 0010 0100 0101 1000 1001 1010

Input : n = 3
Output : 000 001 010 100 101

"""

class Solution:
    def p18(self,n):
        i=0
        res=[]
        self.helper(n,i,res)
        return res
    def helper(self,n,i,res):


        #base case

        