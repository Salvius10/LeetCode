class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum=0
        index_map={0:-1}
        max_length=0
        for i,num in enumerate(nums):
            prefix_sum+=-1 if num==0 else 1
            if prefix_sum in index_map:
                max_length=max(max_length,i-index_map[prefix_sum])
            else:
                index_map[prefix_sum]=i
            
        return max_length