class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        size=len(nums)
        flag=0
        for i in range(len(nums)):
            if nums[i]==target:
                flag=1
                return i
        if flag==0:
            for j in range(len(nums)):
                if nums[j]>target:
                    return j
        return size