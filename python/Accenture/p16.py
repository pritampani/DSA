#Count Handshakes


class Solution:
    def count_handshake(self,n):
        return n*(n-1)//2


a = Solution()

print(a.count_handshake(2))   # Expected: 1
print(a.count_handshake(3))   # Expected: 3
print(a.count_handshake(4))   # Expected: 6
print(a.count_handshake(5))   # Expected: 10
print(a.count_handshake(10))  # Expected: 45
print(a.count_handshake(1))   # Expected: 0
print(a.count_handshake(0))   # Expected: 0