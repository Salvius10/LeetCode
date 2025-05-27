class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1=[]
        count_div=0
        count_notdiv=0
        for i in range(1,n+1):
            num1.append(i)
        for i in range(len(num1)):
            if num1[i]%m==0:
                count_div+=num1[i]
            else:
                count_notdiv+=num1[i]
        return count_notdiv-count_div