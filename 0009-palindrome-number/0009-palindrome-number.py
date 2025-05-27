class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        if x==0:
            return True
        i=x
        result=""
        while i!=0:
            result=result+str(i%10)
            i=i//10
        return x==int(result)