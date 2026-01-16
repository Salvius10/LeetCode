class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK=0xFFFFFFFF
        MAX=0x7FFFFFFF
        while b!=0:
            c=(a&b)&MASK
            a=(a^b)&MASK
            b=((c)<<1)&MASK
        return a if a<=MAX else ~(a^MASK)