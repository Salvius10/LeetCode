class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        hset=set()
        max_count=0
        for right in range(len(s)):
            while s[right] in hset:
                hset.remove(s[left])
                left+=1
            hset.add(s[right])
            max_count=max(max_count,right-left+1)               
        return max_count