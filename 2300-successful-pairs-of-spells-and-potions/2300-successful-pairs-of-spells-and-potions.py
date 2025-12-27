class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        result=[]
        m=len(potions)
        for s in spells:
            target=(success+s-1)//s
            idx=m
            left=0
            right=m-1
            while left<=right:
                mid=(left+right)//2
                if potions[mid]>=target:
                    right=mid-1
                    idx=mid
                else:
                    left=mid+1
            result.append(m-idx)
        return result