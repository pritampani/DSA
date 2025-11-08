#Convert a Number to Hexadecimal	


class Solution:
    def convert_digit_hexa_dec(self,n):
        return hex(n)

a=Solution()

a = Solution()

print(a.convert_digit_hexa_dec(0))        # Expected: 0x0
print(a.convert_digit_hexa_dec(1))        # Expected: 0x1
print(a.convert_digit_hexa_dec(10))       # Expected: 0xa
print(a.convert_digit_hexa_dec(15))       # Expected: 0xf
print(a.convert_digit_hexa_dec(16))       # Expected: 0x10
