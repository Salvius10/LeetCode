class Solution:
    def largestGoodInteger(self, num: str) -> str:
        result=[]
        for i in range(2,len(num)):
            string=""
            if num[i]==num[i-1]==num[i-2]:
                result.append(num[i]*3)
        if result:
            max_val=result[0]
            for i in range(1,len(result)):
                if result[i]>max_val:
                    max_val=result[i]
            return max_val
        else:
            return ""