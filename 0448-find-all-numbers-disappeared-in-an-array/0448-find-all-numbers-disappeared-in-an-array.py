class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        all_num=set(range(1,n+1))
        arr_set=set(nums)
        result=list(all_num-arr_set)
        return result