class Solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        count=0
        while i<len(s):
            if i+1<len(s) and roman_numerals[s[i]]<roman_numerals[s[i+1]]:
                count+=roman_numerals[s[i+1]]-roman_numerals[s[i]]
                i=i+2
            else:
                count+=roman_numerals[s[i]]
                i=i+1
        return count