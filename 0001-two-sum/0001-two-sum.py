class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map={}
        for i,num in enumerate(nums):
            diff=target-num
            if diff in nums_map:
                return [i,nums_map[diff]]
            nums_map[num]=i
            