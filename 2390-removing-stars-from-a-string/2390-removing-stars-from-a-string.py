class Solution:
    def removeStars(self, s: str) -> str:
        result=[]
        for i in s:
            if i=='*':
                result.pop()
                continue
            else:
                result.append(i)
        return ''.join(result)