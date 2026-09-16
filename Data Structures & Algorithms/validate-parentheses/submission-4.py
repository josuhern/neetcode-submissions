class Solution:
    def isValid(self, s: str) -> bool:
        strList = list(s)
        stack = list()
        for x in strList:
            if x == '{' or x == '[' or x == '(':
                stack.append(x)
            if len(stack) <= 0: return False
            if x == '}':
                y = stack.pop()
                if y != "{":
                    print(type(y))
                    return False
            if x == ']':
                y = stack.pop()
                if y != '[':
                    return False
            if x == ')':
                y = stack.pop()
                if y != '(':
                    return False
        if len(stack) > 0: return False
        return True
                #{()[()]}