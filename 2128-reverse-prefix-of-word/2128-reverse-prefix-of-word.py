class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        res=[]
        word=list(word)
        i=0
        flag=0
        while i<len(word):
            if word[i]==ch:
                res.append(word[i])
                i+=1
                flag=1
                break
            res.append(word[i])
            i+=1
        if flag==1:
            res=res[::-1]
            j=i
            while j<len(word):
                res.append(word[j])
                j+=1
            return "".join(res)
        else:
            return "".join(res)