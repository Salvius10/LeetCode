class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count={}
        ele=''
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch]=1
        for ch in t:
            if ch not in count:
                ele=ch
            else:
                count[ch]-=1
        
        if ele=='':
            for key,val in count.items():
                if val!=0:
                    ele=key
        return ele

        