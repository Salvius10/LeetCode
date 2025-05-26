class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        temp=0
        while temp<=n:
            if temp in nums:
                temp+=1
            else:
                return temp