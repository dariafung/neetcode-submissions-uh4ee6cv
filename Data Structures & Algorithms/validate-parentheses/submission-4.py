class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False

        stack = []
        
        for c in s:
            if stack and c == ')' and stack[-1] == '(':
                stack.pop()
            elif stack and c == ']' and stack[-1] == '[':
                stack.pop()
            elif stack and c == '}' and stack[-1] == '{':
                stack.pop()
            elif c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                return False
        
        if stack:
            return False

        return True