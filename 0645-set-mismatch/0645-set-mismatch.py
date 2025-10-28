class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a=[]
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                dup=i
        for i in range(1,len(nums)+1):
            if i not in count:
                mis=i
        a.append(dup)
        a.append(mis)
        return a