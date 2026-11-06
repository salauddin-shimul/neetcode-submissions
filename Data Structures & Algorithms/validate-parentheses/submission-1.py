class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_par = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        for char in s:
            if char in close_par:
                if stack and stack[-1] == close_par[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        else:
            return True