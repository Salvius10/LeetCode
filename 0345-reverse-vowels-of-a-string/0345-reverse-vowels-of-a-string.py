class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_list=['a','e','i','o','u','A','E','I','O','U']
        left=0
        string_list=list(s)
        right=len(string_list)-1
        while left<right:
            while left<right and string_list[left] not in vowel_list:
                left=left+1
            while right>left and string_list[right] not in vowel_list:
                right=right-1
            string_list[left],string_list[right]=string_list[right],string_list[left]
            left=left+1
            right=right-1
        string=''.join(string_list)
        return string
        