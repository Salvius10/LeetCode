class Solution:
    def clearDigits(self, s: str) -> str:
        res=[]
        for i in s:
            if res:
                last=res[-1]
                if i.isdigit() and last.isalpha():
                    res.pop()
                    continue
            res.append(i)
        return "".join(res)