class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
       result=[]
       nums.sort() 
       check_sum=0
       sums_val=0
       for i in range(len(nums)-1,-1,-1):
        check_sum=0
        sums_val+=nums[i]
        result.append(nums[i])
        for j in range(0,i):
            check_sum+=nums[j]
        if sums_val>check_sum:
            return result
       

        
        