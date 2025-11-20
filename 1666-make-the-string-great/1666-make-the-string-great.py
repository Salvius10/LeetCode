class Solution:
    def makeGood(self, s: str) -> str:
        res=[]
        for i in s:
            if res:
                last=res[-1]
                if last.lower()==i.lower() and last!=i:
                    res.pop()
                    continue
            res.append(i)
        return "".join(res)
        