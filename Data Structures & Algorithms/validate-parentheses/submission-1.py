class Solution:
    def isValid(self, s: str) -> bool:
        maps = { ')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c not in maps:
                stack.append(c)
            else:
                if stack and maps[c] ==stack[-1]:
                    stack.pop()
                    
                else:
                    return False
        return stack == []

        