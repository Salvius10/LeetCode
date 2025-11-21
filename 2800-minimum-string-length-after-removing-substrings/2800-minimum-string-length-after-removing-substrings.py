class Solution:
    def minLength(self, s: str) -> int:
        res=[]
        for i in s:
            if res:
                last=res[-1]
                if last=="A" and i=="B":
                    res.pop()
                    continue
                if last=="C" and i=="D":
                    res.pop()
                    continue
            res.append(i)
        return len(res)