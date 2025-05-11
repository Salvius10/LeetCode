class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count=0
        i=0
        while i<len(nums):
            count=0
            for j in range(i):
                if nums[i]==nums[j]:
                    count+=1
            if count>=2:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
        