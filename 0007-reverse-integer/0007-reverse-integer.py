class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        reverse=0
        i=abs(x)
        while i>0:
            reverse=reverse*10+i%10
            i=i//10
        reverse=reverse*sign
        if reverse<-2**31 or reverse>2**31:
            return 0
        return reverse

        