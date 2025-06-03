class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic={}
        for ind,ele in enumerate(nums):
            if ele in dic and ind-dic[ele]<=k:
                return True
            dic[ele]=ind
        return False