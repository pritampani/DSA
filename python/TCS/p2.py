#2. Toggle Bits After MSB

class Solution:
    def toggleAfterMSB(self,n):
        b=bin(n)[2:]
        msb=b[0]
        rest=b[1:]
        toggleed=''.join('1' if x=='0' else '0' for x in rest)

        fin_bin=msb+toggleed
        return int(fin_bin,2)
    
a=Solution()
print(a.toggleAfterMSB(10))   # 13
print(a.toggleAfterMSB(5))    # 6
print(a.toggleAfterMSB(12))   # 11
print(a.toggleAfterMSB(19))   # 28