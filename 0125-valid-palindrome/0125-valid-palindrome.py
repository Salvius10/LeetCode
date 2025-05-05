class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s==' ':
            return True
        string=s.lower().strip()
        for i in string:
            if not i.isalpha() and not i.isdigit():
                string=string.replace(i,'')
        return string==string[::-1]

