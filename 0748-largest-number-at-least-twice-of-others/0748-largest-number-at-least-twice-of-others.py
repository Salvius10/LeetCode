class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max1=-inf
        max2=-inf
        idx=-1
        for i in range(len(nums)):
            if max1<nums[i]:
                max2=max1
                max1=nums[i]
                idx=i
            elif max2<nums[i]:
                max2=nums[i]
        if max1>=2*max2:
            return idx
        return -1