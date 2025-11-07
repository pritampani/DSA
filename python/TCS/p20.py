#Check Anagram Strings



class Solution:
    def is_anagram(self, s1, s2):
        # Quick length check
        if len(s1) != len(s2):
            return False
        
        # Frequency array for 26 lowercase letters
        freq = [0] * 26
        
        for ch1, ch2 in zip(s1, s2):
            freq[ord(ch1) - ord('a')] += 1
            freq[ord(ch2) - ord('a')] -= 1
        
        # If all zeros → anagram
        return all(f == 0 for f in freq)



a = Solution()

print(a.is_anagram("listen", "silent"))     # True
print(a.is_anagram("triangle", "integral")) # True
print(a.is_anagram("apple", "pale"))        # False
print(a.is_anagram("aabbcc", "abcabc"))     # True
print(a.is_anagram("", ""))                 # True
print(a.is_anagram("abcd", "abce"))         # False