class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n=len(score)
        result=[""]*n
        max1=-inf
        max2=-inf
        max3=-inf
        for i in score:
            if max1<=i:
                max3=max2
                max2=max1
                max1=i
            elif max2<=i:
                max3=max2
                max2=i
            elif max3<=i:
                max3=i
        i1=score.index(max1)
        result[i1]="Gold Medal"
        if n>1:  
            i2=score.index(max2)
            result[i2]="Silver Medal"
        if n>2:
            i3=score.index(max3)
            result[i3]="Bronze Medal"
        for i in range(len(score)):
            if result[i]=="":
                rank=sorted(score,reverse=True).index(score[i])+1
                result[i]=str(rank)
        return result