class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        max_dif=0
        nums.sort()
        for i in range(len(nums)-1):
            if (nums[i+1]-nums[i]>max_dif):
                max_dif=nums[i+1]-nums[i]
        return max_dif