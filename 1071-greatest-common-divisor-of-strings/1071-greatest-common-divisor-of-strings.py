class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1,len2=len(str1),len(str2)

        def isDivisor(l):
            if len1%l or len2%l:
                return False
            base=str1[:l]
            return base*(len1//l)==str1 and base*(len2//l)==str2
        for l in range(min(len1,len2),0,-1):
            if isDivisor(l):
                return str1[:l]
        return ""