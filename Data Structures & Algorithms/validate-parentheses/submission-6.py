class Solution:
    def isValid(self, s: str) -> bool:
        strList = list(s)
        stack = list()
        counter = {'}':'{', ')':'(', ']':'['}
        for x in strList:
            if x in counter:
                if stack and counter[x] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(x)
        if len(stack) > 0: return False
        else: return True
                #{()[()]}