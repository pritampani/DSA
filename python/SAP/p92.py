	# .	Reverse Words in a String

	# •	Input: "I love coding" → "coding love I"
class Solution:
    def reverse_string(self, s):
        a = []
        word = ""
        s += " "  # add a space to capture last word
        for ch in s:
            if ch != ' ':
                word += ch
            else:
                if word:
                    a.append(word)
                    word = ""
        a.reverse()
        return ' '.join(a)
    
a = Solution()
print(a.reverse_string("hello world from python"))



