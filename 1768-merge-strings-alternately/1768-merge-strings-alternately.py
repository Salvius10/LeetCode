class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=""
        word1=list(word1)
        word2=list(word2)
        j=0
        k=0
        total_length=len(word1)+len(word2)
        for i in range(total_length):
            if j<len(word1):
                result=result+word1[j]
                j+=1
            if k<len(word2):
                result=result+word2[k]
                k+=1
        return result
