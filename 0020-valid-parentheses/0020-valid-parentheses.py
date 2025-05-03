class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for char in s:
            if char=='(' or char=='{' or char=='[':
                stack.append(char)
            elif char==')' or char=='}' or char==']':
                if len(stack)==0:
                    return False
                k=stack.pop() 
                if (char == ')' and k != '(') or (char == '}' and k != '{') or (char == ']' and k != '['):
                    return False
        return len(stack)==0