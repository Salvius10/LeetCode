class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==1:
            return s
        longest=""
        for i in range(n):
            left=i
            right=i
            while left>=0 and right<n and s[left]==s[right]:
                current=s[left:right+1]
                if len(current)>len(longest):
                    longest=current
                left-=1
                right+=1
            left=i
            right=i+1
            while left>=0 and right<n and s[left]==s[right]:
                current=s[left:right+1]
                if len(current)>len(longest):
                    longest=current
                left-=1
                right+=1
        return longest
            