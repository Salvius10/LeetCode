class Solution:
    def reverseWords(self, s: str) -> str:
        s_list=s.strip().split()
        reversed_list=s_list[::-1]
        return " ".join(reversed_list)
