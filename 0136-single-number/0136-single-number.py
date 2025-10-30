class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        count={}
        for i in nums:
            if i not in count:
                count[i]=1
            else:
                count[i]+=1
        for key,val in count.items():
            if val==1:
                return key
        