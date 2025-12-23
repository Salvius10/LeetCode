class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=0
        left=0
        nums.sort()
        right=len(nums)-1
        while left<right:
            if (nums[left]+nums[right])==k:
                count+=1
                left+=1
                right-=1
            elif (nums[left]+nums[right])>k:
                right-=1
            else:
                left+=1
        return count