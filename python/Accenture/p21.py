class Solution:
    def count(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        vc = 0
        cc = 0
        
        for ch in s.lower():  # Convert to lowercase
            if ch.isalpha():   # Only consider alphabet letters
                if ch in vowels:
                    vc += 1
                else:
                    cc += 1
        return vc, cc
    


a = Solution()

print(a.count("hello world"))       # Expected: (3, 7)
print(a.count("AEIOU"))             # Expected: (5, 0)
print(a.count("Python 3.9"))        # Expected: (1, 5)
print(a.count(""))                   # Expected: (0, 0)
print(a.count("bcdfgh"))             # Expected: (0, 6)
print(a.count("aAeEiIoOuU"))         # Expected: (10, 0)