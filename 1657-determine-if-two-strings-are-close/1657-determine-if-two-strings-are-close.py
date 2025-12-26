class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        dic1={}
        dic2={}
        for i in word1:
            dic1[i]=dic1.get(i,0)+1
        for i in word2:
            dic2[i]=dic2.get(i,0)+1
        if set(dic1.keys())!=set(dic2.keys()):
            return False
        if sorted(dic1.values())!=sorted(dic2.values()):
            return False
        return True

        